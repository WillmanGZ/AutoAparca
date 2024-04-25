import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from Vehiculo import *

# Configura el estilo de customtkinter
ctk.set_appearance_mode("System")  # Puede ser "System", "Dark", o "Light"
ctk.set_default_color_theme("blue")  # Tema de color (hay varios temas disponibles)


tablero = ctk.CTk() 
tablero.title ("tablero")
tablero.resizable(False,False)
window_width = 1080 # cmb xx
window_height = 720


center_x = (tablero.winfo_screenwidth() - window_width) // 2
center_y = (tablero.winfo_screenheight() - window_height) // 2
tablero.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#Frame sobre el que están las cosas en el login
frame_tab = ctk.CTkFrame(master=tablero,width=1080, height=720, corner_radius=15)
frame_tab.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#titulo
titulo = ctk.CTkLabel(frame_tab, text="parqueadero", font=("Century Gothic", 36))
titulo.place(x=90, y=45)

#IngresarPlaca
def getplaca(value):
    placa = value
    print (placa)
    return placa

IngresarPlaca = ctk.CTkEntry(frame_tab, width=220, placeholder_text="Digita la placa del vehiculo")
IngresarPlaca.place(x=120, y=250)

#
def getCombobox(value):
    s = value
    print (value)
#

#Ingresar tipo de vehiculo
Ingresartipov = ctk.CTkComboBox(frame_tab, width=220, values=["carro","Moto","movilidad reducida"], command=getCombobox)
Ingresartipov.place(x=120, y=320)



#ingresar hora de etrada 
IngresarHoradeEntrada = ctk.CTkEntry(frame_tab, width=220, placeholder_text="Digita la hora de entrada")
IngresarHoradeEntrada.place(x=120, y=390)

#ingresar nombre propietario
IngNombre = ctk.CTkEntry(frame_tab, width=220, placeholder_text="Digita el nombre del propietario del vehiculo")
IngNombre.place(x=120, y=430)

#INICIO BOTON confirmar
def boton_click(): # pq da errorrrrrrrrrrrrr????
    v = Vehiculo(IngresarPlaca.get,Ingresartipov.get,IngNombre.get,IngresarHoradeEntrada.get)
    print(v)
boton_login= ctk.CTkButton(frame_tab, width=220 , text="confirmar", corner_radius = 6, command= boton_click)
boton_login.place(x=120, y=470)
#FIN BOTON confirmar

tablero.mainloop()
