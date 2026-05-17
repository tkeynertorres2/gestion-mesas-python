import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
import ctypes
import threading
import speech_recognition as sr

# --- CONFIGURACIÓN INICIAL ---
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

# Función para clics directos mediante la API de Windows (más rápido y preciso)
def win_click(tipo="left"):
    if tipo == "left":
        ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0) # Left down
        ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0) # Left up
    elif tipo == "right":
        ctypes.windll.user32.mouse_event(0x0008, 0, 0, 0, 0) # Right down
        ctypes.windll.user32.mouse_event(0x0010, 0, 0, 0, 0) # Right up
    elif tipo == "doble":
        # Ejecuta dos clics rápidos para abrir apps
        for _ in range(2):
            ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
            ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)
            time.sleep(0.05)

# --- HILO DE VOZ ---
comando_voz = ""
escuchando = True

def escuchar_voz():
    global comando_voz, escuchando
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while escuchando:
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
                texto = r.recognize_google(audio, language="es-ES").lower()
                comando_voz = texto
                print(f"🎙️ Voz: {texto}")
            except: pass

threading.Thread(target=escuchar_voz, daemon=True).start()

# --- CONFIGURACIÓN MEDIAPIPE ---
webcam = cv2.VideoCapture(0)
cam_w, cam_h = 640, 480
webcam.set(3, cam_w)
webcam.set(4, cam_h)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)

screen_w, screen_h = pyautogui.size()
margen = 100
prev_x, prev_y = 0, 0
suavizado = 5
frames_juntos = 0
ultimo_click = 0

while True:
    exito, imagen = webcam.read()
    if not exito: break

    imagen = cv2.flip(imagen, 1)
    rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
    resultado = hands.process(rgb)
    ahora = time.time()

    # --- PROCESAR COMANDOS DE VOZ ---
    if comando_voz:
        cv2.putText(imagen, f"VOZ: {comando_voz}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        if "clic" in comando_voz or "seleccionar" in comando_voz: win_click("left")
        if "derecho" in comando_voz: win_click("right")
        if "doble" in comando_voz or "abrir" in comando_voz: win_click("doble")
        if "cerrar" in comando_voz: pyautogui.hotkey('alt', 'f4')
        comando_voz = ""

    # --- PROCESAR GESTOS DE MANO ---
    if resultado.multi_hand_landmarks:
        for hand_landmarks in resultado.multi_hand_landmarks:
            mp_draw.draw_landmarks(imagen, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm = hand_landmarks.landmark

            # Coordenadas de los dedos (Índice y Medio)
            x8, y8 = int(lm[8].x * cam_w), int(lm[8].y * cam_h)
            x12, y12 = int(lm[12].x * cam_w), int(lm[12].y * cam_h)

            # Detectar si los dedos están levantados
            indice_arriba = lm[8].y < lm[6].y
            medio_arriba = lm[12].y < lm[10].y
            anular_arriba = lm[16].y < lm[14].y

            # 1. MOVER (Solo índice arriba)
            if indice_arriba and not medio_arriba:
                nx = np.interp(x8, [margen, cam_w - margen], [0, screen_w])
                ny = np.interp(y8, [margen, cam_h - margen], [0, screen_h])
                
                curr_x = prev_x + (nx - prev_x) / suavizado
                curr_y = prev_y + (ny - prev_y) / suavizado
                
                # Movimiento de alta precisión
                ax = int(curr_x * 65535 / screen_w)
                ay = int(curr_y * 65535 / screen_h)
                ctypes.windll.user32.mouse_event(0x0001 | 0x8000, ax, ay, 0, 0)
                
                prev_x, prev_y = curr_x, curr_y
                cv2.circle(imagen, (x8, y8), 15, (255, 0, 255), cv2.FILLED)
                frames_juntos = 0

            # 2. CLIC / DOBLE CLIC (Índice y Medio JUNTOS)
            elif indice_arriba and medio_arriba and not anular_arriba:
                distancia = np.hypot(x12 - x8, y12 - y8)
                
                if distancia < 40: # Dedos pegados
                    frames_juntos += 1
                    cv2.line(imagen, (x8, y8), (x12, y12), (0, 255, 0), 5)
                    
                    if frames_juntos == 5: # Un clic normal al unir
                        win_click("left")
                    
                    if frames_juntos == 20: # Mantener unidos para Doble Clic (Abrir App)
                        win_click("doble")
                        cv2.circle(imagen, (x8, y8), 30, (0, 255, 0), cv2.FILLED)
                else:
                    frames_juntos = 0 # Si los separas, se resetea el contador

            # 3. SCROLL (Tres dedos arriba)
            elif indice_arriba and medio_arriba and anular_arriba:
                if y8 < cam_h // 2: pyautogui.scroll(20) # Arriba
                else: pyautogui.scroll(-20) # Abajo
                cv2.putText(imagen, "SCROLL", (x8, y8-20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    # Dibujar rectángulo de área de control
    cv2.rectangle(imagen, (margen, margen), (cam_w - margen, cam_h - margen), (255, 0, 0), 2)
    
    cv2.imshow("Control por Gestos + Voz", imagen)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

escuchando = False
webcam.release()
cv2.destroyAllWindows()