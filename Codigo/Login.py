import customtkinter as ctk
import tkinter as tk
from pathlib import Path
from tkinter import messagebox

base_path = Path(__file__).parent
database_path = base_path / "database" / "database.txt"
db = open(database_path, "r")
d = []
f = []
for i in db:
    a,b = i.split(", ")
    b = b.strip()
    d.append(a)
    f.append(b)
    data = dict(zip(d, f))

# Configura el estilo de customtkinter
ctk.set_appearance_mode("System")  # Puede ser "System", "Dark", o "Light"
ctk.set_default_color_theme("blue")  # Tema de color (hay varios temas disponibles)

#Creacion de la ventana Login
login = ctk.CTk()
login.title ("Inicio de Sesión")
login.resizable(False,False)
window_width = 600
window_height = 440

# Calcular la posición x y y para centrar la ventana, y aplicarla
center_x = (login.winfo_screenwidth() - window_width) // 2
center_y = (login.winfo_screenheight() - window_height) // 2
login.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#Frame sobre el que están las cosas en el login
frame_login = ctk.CTkFrame(master=login,width=320, height=360, corner_radius=15)
frame_login.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#Titulo "Inicia Sesion"
titulo = ctk.CTkLabel(frame_login, text="Inicia Sesión", font=("Century Gothic", 20))
titulo.place(x=90, y=45)

#INICIO CAMPO USUARIO
campo_usuario = ctk.CTkEntry(frame_login, width=220, placeholder_text="Digita tu nombre de usuario")
campo_usuario.place(x=50, y=110)

#INICIO CAMPO CONTRASEÑA
campo_contrasena = ctk.CTkEntry(frame_login, width=220, placeholder_text="Digita tu contraseña")
campo_contrasena.place(x=50, y=165)
campo_contrasena.configure(show="*")  #Para ocultar la contraseña

#BOTON INICIO SESION
def boton_click():
    usuario = campo_usuario.get()
    usuario = usuario.lower()
    contrasena = campo_contrasena.get()
    
     # Abrir el archivo de base de datos en modo lectura
    with open(database_path, "r") as db:
        # Leer cada línea del archivo
        for linea in db:
            # Dividir la línea en nombre de usuario y contraseña
            datos = linea.strip().split(", ")
            if len(datos) == 2:
                usuario_archivo, contrasena_archivo = datos
                usuario_archivo = usuario_archivo.lower()

            # Verificar si las credenciales ingresadas coinciden con las almacenadas en la base de datos.
            if usuario == usuario_archivo and contrasena == contrasena_archivo:
                messagebox.showinfo("Inicio de Sesión", f"Bienvenido, {usuario}!")
                return

        # Si no se encuentra ninguna coincidencia, se mostrará un mensaje de error.
        messagebox.showerror("Error", "Credenciales incorrectas. Por favor, inténtelo de nuevo.")


boton_login= ctk.CTkButton(frame_login, width=220 , text="Iniciar Sesion", corner_radius = 6, command= boton_click)
boton_login.place(x=50, y=240)

#FIN BOTON INICIO SESION

login.mainloop()