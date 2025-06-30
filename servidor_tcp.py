# servidor_con_gui.py
import socket
import threading
import tkinter as tk
import random
import time

HOST = '0.0.0.0'
PORT = 65432

# Función para activar el actuador (LED virtual)
def activar_actuador():
    label_estado.config(text="ACTUADOR ACTIVADO", bg="green")

# Función para resetear visualmente
def resetear_actuador():
    label_estado.config(text="EN ESPERA", bg="gray")

# Función que corre el servidor TCP
def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((HOST, PORT))
        servidor.listen()
        print(f"[Servidor] Esperando conexión en el puerto {PORT}...")

        conn, addr = servidor.accept()
        with conn:
            print(f"[Servidor] Conectado con {addr}")
            while True:
                datos = conn.recv(1024).decode()
                if not datos:
                    break
                print(f"[Servidor] Señal recibida: {datos}")
                
                # Activar actuador visualmente
                activar_actuador()
                ventana.after(1500, resetear_actuador)  # Volver a estado normal después de 1.5 s
                
                # Responder al cliente
                # Simular jitter antes de responder

                jitter = random.uniform(0.01, 0.15)
                # print(f"[Servidor] Simulando latencia de {jitter*1000:.1f} ms")
                # time.sleep(jitter)
                
                conn.sendall(b"Actuador activado\n")

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Controlador Industrial (Servidor)")
ventana.geometry("300x150")

label_estado = tk.Label(ventana, text="EN ESPERA", bg="gray", fg="white", font=("Arial", 18), width=20, height=3)
label_estado.pack(pady=20)

# Iniciar el servidor en un hilo paralelo
threading.Thread(target=iniciar_servidor, daemon=True).start()

# Ejecutar GUI
ventana.mainloop()
