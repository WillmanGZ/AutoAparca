import customtkinter as ctk
import tkinter as tk
from pathlib import Path
from tkinter import messagebox
import os

from Parqueadero import Parqueadero
class Login:
    def __init__(self):
         #Creacion de la ventana Login
        self.login = ctk.CTk()
        self.login.title ("Inicio de Sesión")
        self.login.resizable(False,False)
        window_width = 600
        window_height = 440
        base_path = Path(__file__).parent
        ruta_icono = os.path.join(os.path.dirname(__file__), '..', 'icon.ico')
        self.login.iconbitmap(ruta_icono)
        self.database_path = base_path / "database" / "database.txt"
        self.db = open(self.database_path, "r")
        self.d = []
        self.f = []
        for i in self.db:
            self.a,b = i.split(", ")
            self.b = b.strip()
            self.d.append(self.a)
            self.f.append(self.b)
            self.data = dict(zip(self.d, self.f))

        # Configura el estilo de customtkinter
        ctk.set_appearance_mode("System")  # Puede ser "System", "Dark", o "Light"
        ctk.set_default_color_theme("blue")  # Tema de color (hay varios temas disponibles)

        # Calcular la posición x y y para centrar la ventana, y aplicarla
        center_x = (self.login.winfo_screenwidth() - window_width) // 2
        center_y = (self.login.winfo_screenheight() - window_height) // 2
        self.login.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        #Frame sobre el que están las cosas en el login
        self.frame_login = ctk.CTkFrame(master=self.login,width=320, height=360, corner_radius=15)
        self.frame_login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #Titulo "Inicia Sesion"
        titulo = ctk.CTkLabel(self.frame_login, text="Inicia Sesión", font=("Century Gothic", 20))
        titulo.place(x=90, y=45)

        #INICIO CAMPO USUARIO
        self.campo_usuario = ctk.CTkEntry(self.frame_login, width=220, placeholder_text="Digita tu nombre de usuario")
        self.campo_usuario.place(x=50, y=110)

        #INICIO CAMPO CONTRASEÑA
        self.campo_contrasena = ctk.CTkEntry(self.frame_login, width=220, placeholder_text="Digita tu contraseña")
        self.campo_contrasena.place(x=50, y=165)
        self.campo_contrasena.configure(show="*")  #Para ocultar la contraseña
        self.boton_login= ctk.CTkButton(self.frame_login, width=220 , text="Iniciar Sesion", corner_radius = 6, command= self.boton_click)
        self.boton_login.place(x=50, y=240)
        
        self.login.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.login.mainloop()    

    #BOTON INICIO SESION
    def boton_click(self):
        usuario = self.campo_usuario.get()
        usuario = usuario.lower()
        contrasena = self.campo_contrasena.get()
    
        # Abrir el archivo de base de datos en modo lectura
        with open(self.database_path, "r") as db:
            # Leer cada línea del archivo
            for linea in db:
                # Dividir la línea en nombre de usuario y contraseña
                datos = linea.strip().split(", ")
                if len(datos) == 2:
                    usuario_archivo, contrasena_archivo = datos
                    usuario_archivo = usuario_archivo.lower()

                # Verificar si las credenciales ingresadas coinciden con las almacenadas en la base de datos.
                if usuario == usuario_archivo and contrasena == contrasena_archivo:
                    messagebox.showinfo("Inicio de Sesión", f"Usted ha iniciado sesión exitosamente")
                    self.login.destroy()
                    abrirParqueadero = Parqueadero()
                    return

            # Si no se encuentra ninguna coincidencia, se mostrará un mensaje de error.
            messagebox.showerror("Error", "Credenciales incorrectas. Por favor, inténtelo de nuevo.")
    
    def on_closing(self):
        if messagebox.askokcancel("Salir", "¿Quieres salir de la aplicación?"):
            messagebox.showinfo("Créditos", "Desarrollado por:\n\nWillman Giraldo\nSamuel Ramos\nAndrea Parra\nSebastian Jimenez\n\n© 2024 Todos los derechos reservados")
            self.login.destroy()