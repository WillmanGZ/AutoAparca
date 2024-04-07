import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from Database import *

# Configura el estilo de customtkinter
ctk.set_appearance_mode("System")  # Puede ser "System", "Dark", o "Light"
ctk.set_default_color_theme("blue")  # Tema de color (hay varios temas disponibles)

#Creacion de la ventana Login
login = ctk.CTk()
login.title ("Inicio de Sesion")
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
titulo = ctk.CTkLabel(frame_login, text="Inicia Sesion", font=("Century Gothic", 20))
titulo.place(x=90, y=45)

#INICIO CAMPO USUARIO
campo_usuario = ctk.CTkEntry(frame_login, width=220, placeholder_text="Digita tu nombre de usuario")
campo_usuario.place(x=50, y=110)

#INICIO CAMPO CONTRASEÑA
campo_contraseña = ctk.CTkEntry(frame_login, width=220, placeholder_text="Digita tu contraseña")
campo_contraseña.place(x=50, y=165)

#INICIO BOTON REGISTRARTE
boton_registrarse = ctk.CTkLabel(frame_login, text="Registrarse", font=("Century Gothic", 12), text_color="gray")
boton_registrarse.place(x=200, y=195)

def boton_registrarse_click(event):
    print("Click registrarse")

def on_enter_registrarte(event):
    boton_registrarse.configure(text_color='white')  # Cambiar de color al pasar el mouse

def on_leave_registrarte(event):
    boton_registrarse.configure(text_color='gray')  # Volver al color original al salir el mouse

boton_registrarse.bind("<Button-1>", boton_registrarse_click)
boton_registrarse.bind("<Enter>", on_enter_registrarte)
boton_registrarse.bind("<Leave>", on_leave_registrarte)
#FIN BOTON REGISTRARSE

#INICIO BOTON INICIO SESION
def boton_click():
    usuario = campo_usuario.get()
    contraseña = campo_contraseña.get()
    if(verificar_usuario_contrasena(conexion_usuarios, usuario, contraseña) == True):
        print("Pasó la verificacion")
    else:
        messagebox.showerror("Error de Inicio de Sesión", "El nombre de usuario o la contraseña son incorrectos")
    print(usuario)
    print(contraseña)

boton_login= ctk.CTkButton(frame_login, width=220 , text="Iniciar Sesion", corner_radius = 6, command= boton_click)
boton_login.place(x=50, y=240)
#FIN BOTON INICIO SESION


login.mainloop()


