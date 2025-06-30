# cliente_con_jitter_monitor.py
import socket
import tkinter as tk
import time

HOST = '192.168.0.105'  # Cambiar por IP real del servidor
PORT = 65432

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

errores = 0
umbral_ms = 80  # Umbral de tiempo máximo aceptable (latencia límite)

def enviar_senal():
    global errores
    try:
        # 🔒 Desactivar el botón temporalmente
        boton_enviar.config(state="disabled")

        inicio = time.time()  # Tiempo de envío
        cliente.sendall(b"Sensor: Evento detectado")
        label_estado.config(text="SEÑAL ENVIADA", bg="orange")

        respuesta = cliente.recv(1024).decode()
        fin = time.time()  # Tiempo de recepción

        latencia_ms = (fin - inicio) * 1000
        print(f"[Cliente] Latencia registrada: {latencia_ms:.1f} ms")

        if latencia_ms > umbral_ms:
            errores += 1
            estado = f"⚠️ ERROR {errores} (lat. {latencia_ms:.1f} ms)"
            label_estado.config(text=estado, bg="red")
        else:
            estado = f"OK ({latencia_ms:.1f} ms)"
            label_estado.config(text=estado, bg="green")

        ventana.after(2500, resetear_estado)  # 🕒 Reactivar después de 2.5s
    except:
        label_estado.config(text="Error de conexión", bg="gray")
        boton_enviar.config(state="normal")  # Asegura reactivación en caso de error

def resetear_estado():
    label_estado.config(text="ESPERANDO ACCIÓN", bg="gray")
    boton_enviar.config(state="normal")  # ✅ Reactivar el botón

ventana = tk.Tk()
ventana.title("Sensor con monitoreo de latencia")
ventana.geometry("340x200")

boton_enviar = tk.Button(ventana, text="ENVIAR SEÑAL", font=("Arial", 12),
                         command=enviar_senal, bg="lightblue", width=25, height=2)
boton_enviar.pack(pady=10)

label_estado = tk.Label(ventana, text="ESPERANDO ACCIÓN", bg="gray", fg="white",
                        font=("Arial", 13), width=35, height=3)
label_estado.pack(pady=10)

ventana.mainloop()
