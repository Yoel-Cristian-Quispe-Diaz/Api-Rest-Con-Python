import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import psutil
from datetime import datetime
import threading
import queue
import sys
import io

class PanelControlAPI:
    def __init__(self):
        self.proceso_api = None
        self.cola_logs = queue.Queue()
        self.configurar_ventana_principal()
        self.configurar_elementos_ui()
        self.configurar_monitoreo()

    def configurar_ventana_principal(self):
        self.root = tk.Tk()
        self.root.title("Monitor de API")
        self.root.geometry("600x700")
        self.root.configure(bg="#f5f6fa")
        self.root.resizable(True, True)
        
        estilo = ttk.Style()
        estilo.configure("TFrame", background="#f5f6fa")
        estilo.configure("TButton", padding=10, font=("Helvetica", 10))
        estilo.configure("TCheckbutton", font=("Helvetica", 10))

    def configurar_elementos_ui(self):
        self.frame_principal = ttk.Frame(self.root)
        self.frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Título
        self.etiqueta_titulo = tk.Label(
            self.frame_principal,
            text="Monitor de API en Tiempo Real",
            font=("Helvetica", 18, "bold"),
            bg="#f5f6fa",
            fg="#2c3e50"
        )
        self.etiqueta_titulo.pack(pady=(0, 20))

        # Frame de Control
        self.frame_control = ttk.Frame(self.frame_principal)
        self.frame_control.pack(fill=tk.X, pady=(0, 10))

        self.var_encendido = tk.BooleanVar()
        self.toggle_encendido = ttk.Checkbutton(
            self.frame_control,
            text="API Activa",
            variable=self.var_encendido,
            command=self.actualizar_estado_api
        )
        self.toggle_encendido.pack(side=tk.LEFT, padx=5)

        self.etiqueta_estado = tk.Label(
            self.frame_control,
            text="Estado: Inactivo",
            font=("Helvetica", 11),
            bg="#f5f6fa",
            fg="#e74c3c"
        )
        self.etiqueta_estado.pack(side=tk.LEFT, padx=20)

        # Frame de Monitoreo
        self.frame_monitoreo = ttk.LabelFrame(self.frame_principal, text="Salida de la API")
        self.frame_monitoreo.pack(fill=tk.BOTH, expand=True, pady=10)

        # Consola de logs con scroll
        self.crear_consola_logs()

        # Botones de Control
        self.frame_botones = ttk.Frame(self.frame_principal)
        self.frame_botones.pack(fill=tk.X, pady=10)

        self.boton_limpiar = ttk.Button(
            self.frame_botones,
            text="Limpiar Consola",
            command=self.limpiar_logs
        )
        self.boton_limpiar.pack(side=tk.LEFT, padx=5)

        self.boton_salir = ttk.Button(
            self.frame_botones,
            text="Cerrar",
            command=self.salir_seguro
        )
        self.boton_salir.pack(side=tk.RIGHT, padx=5)

    def crear_consola_logs(self):
        # Frame para la consola con scrollbar
        self.frame_consola = ttk.Frame(self.frame_monitoreo)
        self.frame_consola.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame_consola)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Área de texto para logs
        self.texto_logs = tk.Text(
            self.frame_consola,
            height=20,
            font=("Consolas", 10),
            bg="#1e1e1e",
            fg="#ffffff",
            wrap=tk.WORD,
            yscrollcommand=self.scrollbar.set
        )
        self.texto_logs.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.texto_logs.yview)

        # Configurar tags para colorear diferentes tipos de mensajes
        self.texto_logs.tag_configure("info", foreground="#4CAF50")
        self.texto_logs.tag_configure("error", foreground="#FF5252")
        self.texto_logs.tag_configure("warning", foreground="#FFC107")
        self.texto_logs.tag_configure("timestamp", foreground="#64B5F6")

    def configurar_monitoreo(self):
        self.root.protocol("WM_DELETE_WINDOW", self.salir_seguro)
        threading.Thread(target=self.procesar_cola_logs, daemon=True).start()

    def actualizar_estado_api(self):
        if self.var_encendido.get():
            self.iniciar_api()
        else:
            self.detener_api()

    def iniciar_api(self):
        try:
            if os.path.isfile("main.py"):
                # Configurar la redirección de salida
                self.proceso_api = subprocess.Popen(
                    ["python", "main.py"],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    bufsize=1,
                    universal_newlines=True
                )
                
                self.etiqueta_estado.config(
                    text="Estado: Activo",
                    fg="#27ae60"
                )
                
                # Iniciar threads para capturar la salida
                threading.Thread(target=self.capturar_salida, 
                               args=(self.proceso_api.stdout, "info"),
                               daemon=True).start()
                               
                threading.Thread(target=self.capturar_salida, 
                               args=(self.proceso_api.stderr, "error"),
                               daemon=True).start()
                
            else:
                raise FileNotFoundError("Archivo 'main.py' no encontrado")
        except Exception as e:
            self.manejar_error(f"Error al iniciar: {str(e)}")

    def capturar_salida(self, pipe, tipo):
        for linea in iter(pipe.readline, ''):
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.cola_logs.put((timestamp, tipo, linea.strip()))
        pipe.close()

    def procesar_cola_logs(self):
        while True:
            try:
                timestamp, tipo, mensaje = self.cola_logs.get(timeout=0.1)
                self.agregar_log(timestamp, tipo, mensaje)
            except queue.Empty:
                pass
            if not self.root.winfo_exists():
                break

    def agregar_log(self, timestamp, tipo, mensaje):
        if not mensaje:
            return
            
        self.texto_logs.insert(tk.END, f"[{timestamp}] ", "timestamp")
        
        if tipo == "error":
            self.texto_logs.insert(tk.END, f"{mensaje}\n", "error")
        elif tipo == "warning":
            self.texto_logs.insert(tk.END, f"{mensaje}\n", "warning")
        else:
            self.texto_logs.insert(tk.END, f"{mensaje}\n", "info")
            
        self.texto_logs.see(tk.END)

    def detener_api(self):
        if self.proceso_api:
            try:
                parent = psutil.Process(self.proceso_api.pid)
                for child in parent.children(recursive=True):
                    child.terminate()
                parent.terminate()
                self.proceso_api = None
                self.etiqueta_estado.config(
                    text="Estado: Inactivo",
                    fg="#e74c3c"
                )
            except Exception as e:
                self.manejar_error(f"Error al detener: {str(e)}")

    def limpiar_logs(self):
        self.texto_logs.delete(1.0, tk.END)

    def manejar_error(self, mensaje_error):
        messagebox.showerror("Error", mensaje_error)
        self.var_encendido.set(False)
        self.etiqueta_estado.config(
            text="Estado: Error",
            fg="#e74c3c"
        )
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.agregar_log(timestamp, "error", mensaje_error)

    def salir_seguro(self):
        if self.proceso_api:
            self.detener_api()
        self.root.quit()

    def ejecutar(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PanelControlAPI()
    app.ejecutar()