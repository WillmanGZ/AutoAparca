from functools import partial
import os
import random
import re 
import time
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
from datetime import datetime  
from pathlib import Path
from VehiculoClass import Vehiculo
import math

class Parqueadero:
    def __init__(self):
        self.principal = ctk.CTk()
        window_width = 1000
        window_height = 600
        # Calcular la posición x y y para centrar la ventana, y aplicarla
        center_x = (self.principal.winfo_screenwidth() - window_width) // 2
        center_y = (self.principal.winfo_screenheight() - window_height) // 2
        self.principal.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.principal.title("AutoAparca V1")
        self.principal.resizable(False,False)
        ruta_icono = os.path.join(os.path.dirname(__file__), '..', 'icon.ico')
        self.principal.iconbitmap(ruta_icono)
        ctk.set_appearance_mode("System")  # Puede ser "System", "Dark", o "Light"
        ctk.set_default_color_theme("blue")  # Tema de color (hay varios temas disponibles)
        
        #Instanciar los pisos con sus respectivos espacios
        self.pisos = {
                1: {"carros1": [], "motos1": [], "movilidadreducida1":[]}, 
                2: {"carros2": [], "motos2": [], "movilidadreducida2":[]}, 
                3: {"carros3": [], "motos3": [], "movilidadreducida3":[]}}
        
        #Generar posiciones vacias en los carros
        for i in range(80):
            self.pisos[1]["carros1"].append(None)
            self.pisos[2]["carros2"].append(None)
            self.pisos[3]["carros3"].append(None)
        
        #Generar posiciones vacias en las motos
        for i in range(120):
            self.pisos[1]["motos1"].append(None)
            self.pisos[2]["motos2"].append(None)
            self.pisos[3]["motos3"].append(None)
        
        #Generar posiciones vacias en movilidad reducida
        for i in range(10):
            self.pisos[1]["movilidadreducida1"].append(None)
            self.pisos[2]["movilidadreducida2"].append(None)
            self.pisos[3]["movilidadreducida3"].append(None)
        
        #Listas para los botones del parqueadero
        self.infoCarro1 = self.pisos[1]["carros1"]
        self.infoCarro2 = self.pisos[2]["carros2"]
        self.infoCarro3 = self.pisos[3]["carros3"]
        self.infoMoto1 = self.pisos[1]["motos1"]
        self.infoMoto2 = self.pisos[2]["motos2"]
        self.infoMoto3 = self.pisos[3]["motos3"]
        self.infoMR1 = self.pisos[1]["movilidadreducida1"]
        self.infoMR2 = self.pisos[2]["movilidadreducida2"]
        self.infoMR3 = self.pisos[3]["movilidadreducida3"]
        
        #Panel que se usará para centrar los botones de disponibilidad de los pisos
        self.panel1 = ctk.CTkFrame(master=self.principal,
                             height= 580,
                             width= 670,
                             corner_radius= 15,
                             )
        self.panel1.place(relx=0.345, rely=0.5, anchor=ctk.CENTER)
        
         #Imagen del carrito
        base_path = Path(__file__).parent
        image_path = base_path / "imagenes" / "carrito.png"
        imagen= Image.open(image_path)
        self.img = ImageTk.PhotoImage(imagen)

        self.img_logo = ctk.CTkLabel(master=self.panel1, image=self.img, text="")
        self.img_logo.place(relx = 0.5, rely = 0.5, anchor=ctk.CENTER)
        
        #Titulo del programas
        self.titulo_programa = ctk.CTkLabel(master= self.panel1,
                                       text="AutoAparca V1",
                                       font=("Copperplate Gothic Bold", 32))
        self.titulo_programa.place(relx = 0.5, rely= 0.770, anchor=ctk.CENTER)
        
        #Mnesaje de bienvenida
        self.bienvenido_titulo = ctk.CTkLabel(master= self.panel1,
                                       text="Bienvenido",
                                       font=("Arial", 14))
        self.bienvenido_titulo.place(relx = 0.5, rely= 0.820, anchor=ctk.CENTER)
        
         #Label para saber en qué piso te encuentras
        self.piso_label = ctk.CTkLabel(master= self.panel1,
                                    font= ("Arial", 16),
                                    text= "Piso: Sin seleccionar"
                                    )
        self.piso_label.place(relx = 0.150, rely = 0.05, anchor = ctk.CENTER)
        
        #Label para saber en qué seccion te encuentras
        self.seccion_label = ctk.CTkLabel(master= self.panel1,
                                    font= ("Arial", 16),
                                    text= "Sección: Sin seleccionar"
                                    )
        self.seccion_label.place(relx = 0.150, rely = 0.1, anchor = ctk.CENTER)
        
        #Boton ver seccion
        self.boton_verSeccion = ctk.CTkButton(master=self.panel1,
                                       text= "Ver Sección",
                                       command=self.verSeccion,
                                       height= 25,
                                       width= 180,
                                       corner_radius= 15
                                       )
        self.boton_verSeccion.place(relx = 0.450, rely = 0.05 , anchor = ctk.CENTER)
        
        #Boton cambiar sección
        self.boton_cambiarSeccion = ctk.CTkButton(master=self.panel1,
                                       text= "Cambiar sección",
                                       command=self.cambiarSeccion,
                                       height= 25,
                                       width= 180,
                                       corner_radius= 15
                                       )
        self.boton_cambiarSeccion.place(relx = 0.450, rely = 0.1 , anchor = ctk.CENTER)
        self.boton_cambiarSeccion.configure(state=ctk.DISABLED) #inactivo al principio pq no estás viendo nada al iniciar el programa
        self.seccion_estado = False #Para saber si alguna seccion está activa, falso pq al principio el usuario no ve nada
        
        #Boton que al presionarlo, mostrará la disponibilidad de puestos del piso 1
        self.boton_piso1 = ctk.CTkButton(master=self.panel1,
                                    text= "Piso 1",
                                    command= self.botonPiso1,
                                    height= 25,
                                    width= 50,
                                    corner_radius= 15,
                                    )
        self.boton_piso1.place(relx = 0.7, rely = 0.05, anchor = ctk.CENTER)
        
        #Boton que al presionarlo, mostrará la disponibilidad de puestos del piso 2
        self.boton_piso2 = ctk.CTkButton(master=self.panel1,
                                    text= "Piso 2",
                                    command= self.botonPiso2,
                                    height= 25,
                                    width= 50,
                                    corner_radius= 15
                                    )
        self.boton_piso2.place(relx = 0.8, rely = 0.05, anchor = ctk.CENTER)
        
        #Boton que al presionarlo, mostrará la disponibilidad de puestos del piso 3
        self.boton_piso3 = ctk.CTkButton(master=self.panel1,
                                    text= "Piso 3",
                                    command= self.botonPiso3,
                                    height= 25,
                                    width= 50,
                                    corner_radius=15
                                    )
        self.boton_piso3.place(relx = 0.9, rely = 0.05, anchor = ctk.CENTER)
        
        #Boton para seleccionar carro
        self.boton_carro = ctk.CTkButton(master=self.panel1,
                                    text= "Carro",
                                    command= self.botonCarro,
                                    height= 25,
                                    width= 50,
                                    corner_radius=15
                                    )
        self.boton_carro.place(relx = 0.7, rely = 0.1, anchor = ctk.CENTER)
        
        #Boton para seleccionar moto
        self.boton_moto = ctk.CTkButton(master=self.panel1,
                                    text= "Moto",
                                    command= self.botonMoto,
                                    height= 25,
                                    width= 50,
                                    corner_radius=15
                                    )
        self.boton_moto.place(relx = 0.8, rely = 0.1, anchor = ctk.CENTER)
        
        #Boton para seleccionar movilidad reducida
        self.boton_mr = ctk.CTkButton(master=self.panel1,
                                    text= "MR",
                                    command= self.botonMR,
                                    height= 25,
                                    width= 50,
                                    corner_radius=15
                                    )
        self.boton_mr.place(relx = 0.9, rely = 0.1, anchor = ctk.CENTER)
        
        self.panel2 = ctk.CTkFrame(master= self.panel1,
                              height=480,
                              width=650,
                              corner_radius=15
                              )
        self.panel2.place(relx = 0.5, rely = 0.570, anchor = ctk.CENTER)
        self.panel2.configure(height= 0, width=0)
        #############################################################################################################
        #Panel que se usará para ingresar nuevos vehiculos
        self.panel3 = ctk.CTkFrame(master=self.principal,
                              height=280,
                              width=300,
                              corner_radius=15
                              )
        self.panel3.place(relx = 0.840, rely = 0.25, anchor = ctk.CENTER)
        
        
        #Titulo agregar vehiculo
        agregar_vehiculo_titulo = ctk.CTkLabel(master=self.panel3,
                                            text= "Agregar vehículo",
                                            font=("Arial", 24)
                                            )
        agregar_vehiculo_titulo.place(relx = 0.5, rely = 0.1, anchor = ctk.CENTER)
        
        #Para seleccionar el tipo de vehiculo
        self.opciones = ["Tipo de vehículo", "Carro", "Moto"]
        self.agregar_carro_moto = ctk.CTkComboBox(master=self.panel3,
                                     height= 25,
                                     width= 180,
                                     corner_radius=15,
                                     values= self.opciones,
                                     dropdown_hover_color= "gray",
                                     justify="center",
                                     state="readonly",
                                     )
        self.agregar_carro_moto.set(self.opciones[0])
        self.agregar_carro_moto.place(relx = 0.5, rely = 0.250, anchor = ctk.CENTER)
               
        #TextField de placa para la busqueda de un vehiculo
        self.agregar_placa = ctk.CTkEntry(master= self.panel3,
                                    height= 25,
                                    width= 180,
                                    corner_radius= 15,
                                    placeholder_text= "          Placa del vehículo",
                                    placeholder_text_color= "gray"                          
                                    )
        self.agregar_placa.place(relx = 0.5, rely = 0.4, anchor = ctk.CENTER)
        
         #Checkbox para movilidad reducida
        self.agregar_movilidad_reducida = ctk.CTkCheckBox(master=self.panel3,
                                             height=3,
                                             width=3,
                                             corner_radius=5,
                                             text= "Movilidad Reducida")
        self.agregar_movilidad_reducida.place(relx = 0.5, rely = 0.550, anchor = ctk.CENTER)
        
        #Boton para agregar vehiculo
        agregar_vehiculo = ctk.CTkButton(master= self.panel3,
                                        height=25,
                                        width=180,
                                        text="Agregar vehículo",
                                        corner_radius= 15,
                                        command=self.agregarVehiculo
                                        )
        agregar_vehiculo.place(relx = 0.5, rely = 0.7, anchor = ctk.CENTER)
        
        #Widget para la hora
        self.time_label = ctk.CTkLabel(master=self.panel3,
                                       font=("Bold", 16)
                                       )
        self.time_label.place(relx = 0.5, rely= 0.860 , anchor=ctk.CENTER)
        ##############################################################################################################
        #Panel que se usará para buscar vehiculos
        self.panel4 = ctk.CTkFrame(master=self.principal,
                              height=290,
                              width=300,
                              corner_radius=15
                              )
        self.panel4.place(relx = 0.840, rely = 0.740, anchor = ctk.CENTER)
        
        #Texto que mostrará la informacion del vehiculo
        self.informacion_vehiculo = ctk.CTkLabel(master= self.panel4,
                                            text= "Información del vehículo",
                                            height=30,
                                            width=50,
                                            font=("Arial", 20)
                                            )
        self.informacion_vehiculo.place(relx = 0.5, rely = 0.15, anchor = ctk.CENTER)
        self.informacion_vehiculo.place_forget()
        
        #Titulo Buscar vehiculo
        self.informacion_vehiculo_titulo = ctk.CTkLabel(master=self.panel4,
                                            text= "Buscar vehículo",
                                            font=("Arial", 24)
                                            )
        self.informacion_vehiculo_titulo.place(relx = 0.5, rely = 0.2, anchor = ctk.CENTER)
        
        #Titulo detalles
        self.tituloDetalles = ctk.CTkLabel(master=self.panel4,
                                           text="Detalles",
                                           font=("Arial", 24)) 
             
        #TextField de placa para la busqueda de un vehiculo
        self.buscar_placa = ctk.CTkEntry(master= self.panel4,
                                    height= 25,
                                    width= 180,
                                    corner_radius= 15,
                                    placeholder_text= "          Placa del vehículo",
                                    placeholder_text_color= "gray"                          
                                    )
        self.buscar_placa.place(relx = 0.5, rely = 0.420, anchor = ctk.CENTER)
        
        #Boton para buscar vehiculo mediante la placa
        self.buscar_vehiculo_boton = ctk.CTkButton(master= self.panel4,
                                        height=25,
                                        width=180,
                                        text="Buscar vehículo",
                                        corner_radius= 15,
                                        command=self.buscarVehiculo
                                        )
        self.buscar_vehiculo_boton.place(relx = 0.5, rely = 0.550, anchor = ctk.CENTER)
        
        #Boton pagar fianza
        self.eliminar_carro = ctk.CTkButton(master=self.panel4,
                                       text= "Pagar fianza",
                                       command=self.eliminarVehiculo,
                                       height= 25,
                                       width= 180,
                                       corner_radius= 15
                                       )
        self.eliminar_carro.configure(state=ctk.DISABLED)
        
        #Boton buscar otro vehículo
        self.buscarOtroVehiculo = ctk.CTkButton(master=self.panel4,
                                       text= "Buscar otro vehículo",
                                       command=self.buscar_otrovehiculo,
                                       height= 25,
                                       width= 180,
                                       corner_radius= 15
                                       )
        self.buscarOtroVehiculo.place_forget()
        
       
        
        #Piso seleccionado por el usuario, empieza none pq al principio el usuario no ha seleccionado nada
        self.pisoSeleccionado = None
        
        #Vehiculo seleccionado por el usuario, empieza none pq al principio el usuario no ha seleccionado nada
        self.vehiculoSeleccionado = None
        
        #Lista de los botones carro
        self.botonesCarro = []
        #Lista de los botones moto
        self.botonesMoto = []
        #Lista de los botones movilidad reducida
        self.botonesMR = []
        
        #Para seleccionar vehiculos y eliminarlos despues
        self.resultadoBusqueda = None
        
        self.update_time()
        self.principal.mainloop()
    
    def update_time(self):
        now = datetime.now()  # Usar datetime.now() para obtener la hora actual
        current_time = now.strftime("%H:%M:%S")
        self.time_label.configure(text=f"""Hora actual
{current_time}""")
        self.principal.after(1000, self.update_time)  # Actualiza la hora cada segundo
    
    def verSeccion(self):
        if self.pisoSeleccionado == None and self.vehiculoSeleccionado == None:
            messagebox.showwarning("Elija una sección para ver", "Debe elegir un piso y una sección del estacionamiento para ver")
        elif self.pisoSeleccionado == None:
            messagebox.showwarning("Elija un piso para ver", "Debe elegir un piso del estacionamiento para ver")
        elif self.vehiculoSeleccionado == None:
            messagebox.showwarning("Elija una sección para ver", "Debe una sección del estacionamiento para ver")
        else:
            self.panel2.configure(height= 480, width=650)
            self.estacionamiento()
            self.boton_piso1.configure(state= ctk.DISABLED)
            self.boton_piso2.configure(state=ctk.DISABLED)
            self.boton_piso3.configure(state=ctk.DISABLED)
            self.boton_carro.configure(state=ctk.DISABLED)
            self.boton_moto.configure(state=ctk.DISABLED)
            self.boton_mr.configure(state=ctk.DISABLED)
            self.boton_verSeccion.configure(state=ctk.DISABLED)
            self.boton_cambiarSeccion.configure(state=ctk.NORMAL)
            self.img_logo.place_forget()
            self.titulo_programa.place_forget()
            self.bienvenido_titulo.place_forget()
            self.seccion_estado = True
    
    def cambiarSeccion(self):
        if self.seccion_estado == True:
            # Destruir botones existentes
            for boton in self.botonesCarro:
                boton.destroy()
            self.botonesCarro.clear()

            for boton in self.botonesMoto:
                boton.destroy()
            self.botonesMoto.clear()

            for boton in self.botonesMR:
                boton.destroy()
            self.botonesMR.clear()
            #Volver a habilitar los botones
            self.panel2.configure(height= 0, width=0)
            self.boton_piso1.configure(state= ctk.NORMAL)
            self.boton_piso2.configure(state=ctk.NORMAL)
            self.boton_piso3.configure(state=ctk.NORMAL)
            self.boton_carro.configure(state=ctk.NORMAL)
            self.boton_moto.configure(state=ctk.NORMAL)
            self.boton_mr.configure(state=ctk.NORMAL)
            self.boton_verSeccion.configure(state=ctk.NORMAL)
            self.boton_cambiarSeccion.configure(state=ctk.DISABLED)
            self.piso_label.configure(text= f"Piso: Sin seleccionar")
            self.pisoSeleccionado = None
            self.seccion_label.configure(text = f"Sección: Sin seleccionar")
            self.vehiculoSeleccionado = None
            self.informacion_vehiculo.configure(text="Información del vehículo", font= ("Arial", 20))
            self.img_logo.place(relx = 0.5, rely = 0.5, anchor=ctk.CENTER)
            self.titulo_programa.place(relx = 0.5, rely= 0.770, anchor=ctk.CENTER)
            self.bienvenido_titulo.place(relx = 0.5, rely = 0.820, anchor = ctk.CENTER)
            self.bienvenido_titulo.configure(state=ctk.NORMAL)
            self.buscar_otrovehiculo()
    
            self.seccion_estado = False
                        

    def botonPiso1(self):
        self.pisoSeleccionado = 1
        if self.pisoSeleccionado == None:
            self.piso_label.configure(text= f"Piso: Sin seleccionar")
        else:
            self.piso_label.configure(text= f"Piso: {self.pisoSeleccionado}")
        if self.vehiculoSeleccionado == None:
            self.seccion_label.configure(text = f"Sección: Sin seleccionar") 
        else:  
            self.seccion_label.configure(text = f"Sección: {self.vehiculoSeleccionado}")
        
        
    
    def botonPiso2(self):
        self.pisoSeleccionado = 2
        if self.pisoSeleccionado == None:
            self.piso_label.configure(text= f"Piso: Sin seleccionar")
        else:
            self.piso_label.configure(text= f"Piso: {self.pisoSeleccionado}")
        if self.vehiculoSeleccionado == None:
            self.seccion_label.configure(text = f"Sección: Sin seleccionar") 
        else:  
            self.seccion_label.configure(text = f"Sección: {self.vehiculoSeleccionado}")
        
    
    def botonPiso3(self):
        self.pisoSeleccionado = 3
        if self.pisoSeleccionado == None:
            self.piso_label.configure(text= f"Piso: Sin seleccionar")
        else:
            self.piso_label.configure(text= f"Piso: {self.pisoSeleccionado}")
        if self.vehiculoSeleccionado == None:
            self.seccion_label.configure(text = f"Sección: Sin seleccionar") 
        else:  
            self.seccion_label.configure(text = f"Sección: {self.vehiculoSeleccionado}")
        
    
    def botonCarro(self):
        self.vehiculoSeleccionado = "Carro"
        if self.pisoSeleccionado == None:
            self.piso_label.configure(text= f"Piso: Sin seleccionar")
        else:
            self.piso_label.configure(text= f"Piso: {self.pisoSeleccionado}")
        if self.vehiculoSeleccionado == None:
            self.seccion_label.configure(text = f"Sección: Sin seleccionar") 
        else:  
            self.seccion_label.configure(text = f"Sección: {self.vehiculoSeleccionado}")
        
        
    def botonMoto(self):
        self.vehiculoSeleccionado = "Moto"
        if self.pisoSeleccionado == None:
            self.piso_label.configure(text= f"Piso: Sin seleccionar")
        else:
            self.piso_label.configure(text= f"Piso: {self.pisoSeleccionado}")
        if self.vehiculoSeleccionado == None:
            self.seccion_label.configure(text = f"Sección: Sin seleccionar") 
        else:  
            self.seccion_label.configure(text = f"Sección: {self.vehiculoSeleccionado}")
        
        
    def botonMR(self):
        self.vehiculoSeleccionado = "Movilidad Reducida"
        if self.pisoSeleccionado == None:
            self.piso_label.configure(text= f"Piso: Sin seleccionar")
        else:
            self.piso_label.configure(text= f"Piso: {self.pisoSeleccionado}")
        if self.vehiculoSeleccionado == None:
            self.seccion_label.configure(text = f"Sección: Sin seleccionar") 
        else:  
            self.seccion_label.configure(text = f"Sección: {self.vehiculoSeleccionado}")
        
        
    def buscarVehiculo(self):
        placa = self.buscar_placa.get().upper()
        if self.verificarPlaca2(placa):
            self.buscar_vehiculo(placa)

    
    def agregarVehiculo(self):
        placa = self.agregar_placa.get().upper()
        if self.verificarPlacaAgregar(placa):
            if self.buscar_placa_method(placa) == None:
                tipo_vehiculo = self.agregar_carro_moto.get()
                movilidad_reducida = self.agregar_movilidad_reducida.get()
                # Obtener la hora actual y formatearla como cadena solo de hora
                now = datetime.now()
                hora_entrada = now.strftime("%H:%M:%S")

                # Crear un objeto datetime con la fecha actual y la hora obtenida
                fecha_hora_entrada = datetime.strptime(f"{now.date()} {hora_entrada}", "%Y-%m-%d %H:%M:%S")
                nuevoVehiculo = Vehiculo(placa, tipo_vehiculo, movilidad_reducida)
                nuevoVehiculo.horaEntrada = fecha_hora_entrada
            
                espacio_encontrado = False
                while not espacio_encontrado:
                    if tipo_vehiculo == "Carro" and movilidad_reducida == 0:
                        piso = random.randint(1, 3)
                        posicion = random.randint(0,79)
                        posicionParqueadero = self.index_to_position2(posicion, piso, tipo_vehiculo, movilidad_reducida)
                        nuevoVehiculo.posicion = posicionParqueadero
                        if self.pisos[piso][f"carros{piso}"][posicion] == None:
                            self.pisos[piso][f"carros{piso}"][posicion] = nuevoVehiculo
                            self.pisoSeleccionado = piso
                            self.vehiculoSeleccionado = tipo_vehiculo
                            espacio_encontrado = True
                
                    elif tipo_vehiculo == "Moto" and movilidad_reducida == 0:
                        piso = random.randint(1, 3)
                        posicion = random.randint(0,119)
                        posicionParqueadero = self.index_to_position2(posicion, piso, tipo_vehiculo, movilidad_reducida)
                        nuevoVehiculo.posicion = posicionParqueadero
                        if self.pisos[piso][f"motos{piso}"][posicion] == None:
                            self.pisos[piso][f"motos{piso}"][posicion] = nuevoVehiculo
                            self.pisoSeleccionado = piso
                            self.vehiculoSeleccionado = tipo_vehiculo
                            espacio_encontrado = True
                
                    elif movilidad_reducida == 1:
                        piso = random.randint(1, 3)
                        posicion = random.randint(0,9)
                        posicionParqueadero = self.index_to_position2(posicion, piso, tipo_vehiculo, movilidad_reducida)
                        nuevoVehiculo.posicion = posicionParqueadero
                        if self.pisos[piso][f"movilidadreducida{piso}"][posicion] == None:
                            self.pisos[piso][f"movilidadreducida{piso}"][posicion] = nuevoVehiculo
                            self.pisoSeleccionado = piso
                            self.vehiculoSeleccionado = tipo_vehiculo
                            espacio_encontrado = True
            
                if espacio_encontrado:
                    if movilidad_reducida == 1:
                        seccion = "Movilidad Reducida"
                    else:
                        seccion = tipo_vehiculo
                    messagebox.showinfo("Vehiculo estacionado", f"El vehículo fué estacionado correctamente en el piso {piso}, sección: {seccion}, posición {nuevoVehiculo.posicion}. Su hora de entrada fué: {nuevoVehiculo.horaEntrada}")
                    if movilidad_reducida == 1:
                        self.vehiculoSeleccionado = "Movilidad Reducida"
                    self.verSeccion()
                    self.piso_label.configure(text= f"Piso: {self.pisoSeleccionado}")
                    self.seccion_label.configure(text = f"Sección: {self.vehiculoSeleccionado}")
                else:
                    messagebox.showerror("Sin espacio", "No se encontró espacios disponibles en el estacionamiento")
        self.agregar_carro_moto.set(self.opciones[0])
        self.agregar_movilidad_reducida.deselect()
        self.agregar_placa.delete(0, ctk.END)
       
    
    def calcular_tarifa(self,vehiculo):
        tarifa_por_media_hora = 1000  # Suponiendo que la tarifa por hora es 2000
        fecha_hora_entrada = vehiculo.horaEntrada
        fecha_hora_salida = datetime.now()

        # Calcular la diferencia en tiempo
        diferencia = fecha_hora_salida - fecha_hora_entrada
        
        # Convertir la diferencia en medias horas y redondear hacia arriba
        medias_horas = diferencia.total_seconds() / (30 * 60)
        medias_horas_cobradas = math.ceil(medias_horas)
        
        # Calcular el costo
        costo = medias_horas_cobradas * tarifa_por_media_hora
        
        return costo


    def eliminarVehiculo(self):
        if self.resultadoBusqueda == None:
            messagebox.showerror("No ha seleccionado ningun vehículo", "Seleccione un vehículo para eliminar")
        else:
            vehiculoSeleccionado = self.resultadoBusqueda
            costo = self.calcular_tarifa(vehiculoSeleccionado)
            messagebox.showinfo("Costo a pagar", f"El costo a pagar es de: {costo}")
            placa = vehiculoSeleccionado.placa
            
            c = 0
            for vehiculo in self.pisos[1]["carros1"]:
                if vehiculo is not None and vehiculo.placa == placa:
                    self.pisos[1]["carros1"][c] = None
                    messagebox.showinfo("Vehículo eliminado", "El vehículo fué eliminado exitosamente")
                c +=1
            c= 0
            for vehiculo in self.pisos[2]["carros2"]:
                if vehiculo is not None and vehiculo.placa == placa:
                    self.pisos[2]["carros2"][c]= None
                    messagebox.showinfo("Vehículo eliminado", "El vehículo fué eliminado exitosamente")
                c +=1
            c= 0
            for vehiculo in self.pisos[3]["carros3"]:
                if vehiculo is not None and vehiculo.placa == placa:
                    self.pisos[3]["carros3"][c]= None
                    messagebox.showinfo("Vehículo eliminado", "El vehículo fué eliminado exitosamente")
                c +=1
            c= 0
            for vehiculo in self.pisos[1]["motos1"]:
                if vehiculo is not None and vehiculo.placa == placa:
                    self.pisos[1]["motos1"][c]= None
                    messagebox.showinfo("Vehículo eliminado", "El vehículo fué eliminado exitosamente")
                c +=1
            c= 0
            for vehiculo in self.pisos[2]["motos2"]:
                if vehiculo is not None and vehiculo.placa == placa:
                    self.pisos[2]["motos2"][c]= None
                    messagebox.showinfo("Vehículo eliminado", "El vehículo fué eliminado exitosamente")
                c +=1
            c= 0
            for vehiculo in self.pisos[3]["motos3"]:
                if vehiculo is not None and vehiculo.placa == placa:
                    self.pisos[3]["motos3"][c]= None
                    messagebox.showinfo("Vehículo eliminado", "El vehículo fué eliminado exitosamente")
                c +=1
            c= 0
            for vehiculo in self.pisos[1]["movilidadreducida1"]:
                if vehiculo is not None and vehiculo.placa == placa:
                    self.pisos[1]["movilidadreducida1"][c]= None
                    messagebox.showinfo("Vehículo eliminado", "El vehículo fué eliminado exitosamente")
                c +=1
            c= 0
            for vehiculo in self.pisos[2]["movilidadreducida2"]:
                if vehiculo is not None and vehiculo.placa == placa:
                    self.pisos[2]["movilidadreducida2"][c]= None
                    messagebox.showinfo("Vehículo eliminado", "El vehículo fué eliminado exitosamente")
                c +=1
            c= 0
            for vehiculo in self.pisos[3]["movilidadreducida3"]:
                if vehiculo is not None and vehiculo.placa == placa:
                    self.pisos[3]["movilidadreducida3"][c]= None
                    messagebox.showinfo("Vehículo eliminado", "El vehículo fué eliminado exitosamente")
                c +=1
            self.estacionamiento()
            self.resultadoBusqueda = None
            self.informacion_vehiculo.configure(text="Información del vehículo", font= ("Arial", 20))
            self.eliminar_carro.configure(state=ctk.DISABLED)
            self.buscar_otrovehiculo()
            
    
    
    def buscar_placa_method(self, placa):
        carros1 = self.pisos[1]["carros1"]
        carros2 =self.pisos[2]["carros2"]
        carros3 = self.pisos[3]["carros3"]
        motos1 = self.pisos[1]["motos1"]
        motos2 = self.pisos[2]["motos2"]
        motos3 = self.pisos[3]["motos3"]
        mr1= self.pisos[1]["movilidadreducida1"]
        mr2= self.pisos[2]["movilidadreducida2"]
        mr3 = self.pisos[3]["movilidadreducida3"]
        
        for vehiculo in carros1:
            if vehiculo is not None and vehiculo.placa == placa:
                messagebox.showerror("Vehículo existente", "La placa del vehículo ya se encuentra registrada")
                return vehiculo
        
        for vehiculo in carros2:
            if vehiculo is not None and vehiculo.placa == placa:
                messagebox.showerror("Vehículo existente", "La placa del vehículo ya se encuentra registrada")
                return vehiculo
            
        for vehiculo in carros3:
            if vehiculo is not None and vehiculo.placa == placa:
                messagebox.showerror("Vehículo existente", "La placa del vehículo ya se encuentra registrada")
                return vehiculo
            
        for vehiculo in motos1:
            if vehiculo is not None and vehiculo.placa == placa:
                messagebox.showerror("Vehículo existente", "La placa del vehículo ya se encuentra registrada")
                return vehiculo
            
        for vehiculo in motos2:
            if vehiculo is not None and vehiculo.placa == placa:
                messagebox.showerror("Vehículo existente", "La placa del vehículo ya se encuentra registrada")
                return vehiculo
            
        for vehiculo in motos3:
            if vehiculo is not None and vehiculo.placa == placa:
                messagebox.showerror("Vehículo existente", "La placa del vehículo ya se encuentra registrada")
                return vehiculo
            
        for vehiculo in mr1:
            if vehiculo is not None and vehiculo.placa == placa:
                messagebox.showerror("Vehículo existente", "La placa del vehículo ya se encuentra registrada")
                return vehiculo
            
        for vehiculo in mr2:
            if vehiculo is not None and vehiculo.placa == placa:
                messagebox.showerror("Vehículo existente", "La placa del vehículo ya se encuentra registrada")
                return vehiculo
            
        for vehiculo in mr3:
            if vehiculo is not None and vehiculo.placa == placa:
                messagebox.showerror("Vehículo existente", "La placa del vehículo ya se encuentra registrada")
                return vehiculo
        
        return None
    
    def buscar_vehiculoPaEliminar(self, placa):
        carros1 = self.pisos[1]["carros1"]
        carros2 =self.pisos[2]["carros2"]
        carros3 = self.pisos[3]["carros3"]
        motos1 = self.pisos[1]["motos1"]
        motos2 = self.pisos[2]["motos2"]
        motos3 = self.pisos[3]["motos3"]
        mr1= self.pisos[1]["movilidadreducida1"]
        mr2= self.pisos[2]["movilidadreducida2"]
        mr3 = self.pisos[3]["movilidadreducida3"]
        
        for vehiculo in carros1:
            if vehiculo is not None and vehiculo.placa == placa:
                return vehiculo
        
        for vehiculo in carros2:
            if vehiculo is not None and vehiculo.placa == placa:
                return vehiculo
            
        for vehiculo in carros3:
            if vehiculo is not None and vehiculo.placa == placa:
                return vehiculo
            
        for vehiculo in motos1:
            if vehiculo is not None and vehiculo.placa == placa:
                return vehiculo
            
        for vehiculo in motos2:
            if vehiculo is not None and vehiculo.placa == placa:
                return vehiculo
            
        for vehiculo in motos3:
            if vehiculo is not None and vehiculo.placa == placa:
                return vehiculo
            
        for vehiculo in mr1:
            if vehiculo is not None and vehiculo.placa == placa:
                return vehiculo
            
        for vehiculo in mr2:
            if vehiculo is not None and vehiculo.placa == placa:
                return vehiculo
            
        for vehiculo in mr3:
            if vehiculo is not None and vehiculo.placa == placa:
                return vehiculo
        
        return None
    
    
    #Metodo del boton buscar vehiculo
    def buscar_vehiculo(self, placa):
        vehiculo = self.buscar_vehiculoPaEliminar(placa)
        if vehiculo == None:
            messagebox.showerror("Vehículo no registrado", "La placa digitada no se encuentra registrada")
        else:
            self.informacion_vehiculo.configure(text=f"""Posición: {vehiculo.posicion}
Placa: {vehiculo.placa}
Tipo: {vehiculo.tipoVehiculo}
Ingreso: {vehiculo.horaEntrada}""", font= ("Arial", 18))
            messagebox.showinfo("Vehículo encontrado", "El vehículo ha sido encontrado con éxito, puede ver su información en pantalla")
            self.resultadoBusqueda = vehiculo
            self.eliminar_carro.configure(state=ctk.NORMAL)
            self.informacion_vehiculo.place(relx = 0.5, rely = 0.4, anchor = ctk.CENTER)
            self.informacion_vehiculo_titulo.place_forget()
            self.buscar_placa.delete(0, ctk.END)
            self.buscar_placa.place_forget()
            self.buscar_vehiculo_boton.place_forget()
            self.eliminar_carro.place(relx = 0.5, rely=0.75, anchor = ctk.CENTER)
            self.buscarOtroVehiculo.place(relx = 0.5, rely = 0.85 , anchor = ctk.CENTER)
            self.tituloDetalles.place(relx = 0.5, rely = 0.150, anchor = ctk.CENTER)
            
            
    def buscar_otrovehiculo(self):
        self.eliminar_carro.place_forget()
        self.buscarOtroVehiculo.place_forget()
        self.informacion_vehiculo_titulo.place(relx = 0.5, rely = 0.1, anchor = ctk.CENTER)
        self.buscar_placa.place(relx = 0.5, rely = 0.400, anchor = ctk.CENTER)
        self.buscar_vehiculo_boton.place(relx = 0.5, rely = 0.550, anchor = ctk.CENTER)
        self.informacion_vehiculo.place_forget()
        self.tituloDetalles.place_forget()
            
    #Para verificar si la placa es valida
    def verificarPlacaAgregar(self, placa):
        if placa == "":
            messagebox.showwarning("Digite su placa", "Porfavor digite su placa")
            return False
        else:
            if self.agregar_carro_moto.get() == "Carro":
                if self.formatoPlacaCarro(placa):
                    return True
                else:
                    messagebox.showerror("Formato Incorrecto", "Por favor, digite una placa con el formato XXX000 (Sin espacios entre los dígitos)")
                    return False
            elif self.agregar_carro_moto.get() == "Moto":
                if self.formatoPlacaMoto(placa):
                    return True
                else:
                    messagebox.showerror("Formato incorrecto", "Por favor, digite una placa con el formato XXX000 o XXX 00X (Sin espacios entre los dígitos)")
                    return False
            else:
                messagebox.showwarning("Elegir tipo de vehículo", "Debe elegir el tipo de vehículo")
                return False
    
    #Para verificar si la placa es valida
    def verificarPlaca(self, placa):
        if placa == "":
            messagebox.showwarning("Digite su placa", "Porfavor digite su placa")
            return False
        else:
            if self.carro_moto.get() == "Carro":
                if self.formatoPlacaCarro(placa):
                    return True
                else:
                    messagebox.showerror("Formato Incorrecto", "Por favor, digite una placa con el formato XXX000 (Sin espacios entre los dígitos)")
                    return False
            elif self.carro_moto.get() == "Moto":
                if self.formatoPlacaMoto(placa):
                    return True
                else:
                    messagebox.showerror("Formato incorrecto", "Por favor, digite una placa con el formato XXX000 o XXX 00X (Sin espacios entre los dígitos)")
                    return False
            else:
                messagebox.showwarning("Elegir tipo de vehículo", "Debe elegir el tipo de vehículo")
                return False
        
    def verificarPlaca2(self, placa):
        if placa == "":
            messagebox.showwarning("Digite su placa", "Por favor digite su placa")
            return False
        elif self.formatoPlacaCarro(placa):
            return True
        elif self.formatoPlacaMoto(placa):
            return True
        else:
            messagebox.showerror("Formato Incorrecto", "Por favor, digite una placa con el formato de carro (XXX000) o de moto (XXX000 o XXX 00X)")
            return False

    def formatoPlacaCarro(self, placa):
        # Expresión regular para verificar el formato de placa colombiano
        patron = r'^[A-Z]{3}\d{3}$'
        return re.match(patron, placa) is not None
    
        #Expresión Regular: ^[A-Z]{3}\d{3}$
        #^ indica el inicio de la línea.
        #[A-Z]{3} verifica que hay tres letras mayúsculas.
        #\d{3} verifica que hay tres dígitos.
        #$ indica el final de la línea.
        #re.match(patron, placa): Comprueba si la cadena placa coincide con el patrón. Retorna un objeto de coincidencia si la placa es válida, y None si no lo es.
        
    def formatoPlacaMoto(self, placa):
        # Expresión regular para placas de motocicletas: tres letras, dos dígitos, y un dígito o letra al final
        patron = r'^[A-Z]{3}\d{2}[A-Z0-9]$'
        return re.match(patron, placa) is not None
    
        #Expresión Regular: ^[A-Z]{3}\d{2}[A-Z0-9]$
        #^ indica el inicio de la cadena.
        #[A-Z]{3} asegura que los primeros tres caracteres sean letras mayúsculas.
        #\d{2} asegura que los siguientes dos caracteres sean dígitos.
        #[A-Z0-9] el último carácter puede ser un dígito o una letra mayúscula.
        #$ indica el final de la cadena. 
    
    def estadoBotones(self, posicion):
        piso = self.pisoSeleccionado
        vehiculo = self.vehiculoSeleccionado
        if piso == 1 and vehiculo == "Carro":
            carros1 = self.pisos[1]["carros1"]
            estado = carros1[posicion]
        elif piso == 1 and vehiculo == "Moto":
            motos1 = self.pisos[1]["motos1"]
            estado = motos1[posicion]
        elif piso == 1 and vehiculo == "Movilidad Reducida":
            mr1 = self.pisos[1]["movilidadreducida1"]
            estado = mr1[posicion]
        
        if piso == 2 and vehiculo == "Carro":
            carros2 = self.pisos[2]["carros2"]
            estado = carros2[posicion]
        elif piso == 2 and vehiculo == "Moto":
            motos2 = self.pisos[2]["motos2"]
            estado = motos2[posicion]
        elif piso == 2 and vehiculo == "Movilidad Reducida":
            mr2 = self.pisos[2]["movilidadreducida2"]
            estado = mr2[posicion]
            
        if piso == 3 and vehiculo == "Carro":
            carros3 = self.pisos[3]["carros3"]
            estado = carros3[posicion]
        elif piso == 3 and vehiculo == "Moto":
            motos3 = self.pisos[3]["motos3"]
            estado = motos3[posicion]
        elif piso == 3 and vehiculo == "Movilidad Reducida":
            mr3 = self.pisos[3]["movilidadreducida3"]
            estado = mr3[posicion]
        
        return estado
    
    def index_to_position(self, index):
        # Asegúrate de que el índice esté en el rango permitido
        if self.vehiculoSeleccionado == "Carro":
            if index < 0 or index >= 80:
                return "Índice fuera de rango"

         # Calcula la fila y la columna
            piso = self.pisoSeleccionado
            fila = index // 8
            columna = (index % 8) + 1

         # Convierte el índice de fila a letra (A=65 en ASCII)
            letra_fila = chr(fila + 65)

            # Formatea la salida como 'A1', 'B2', etc.
            return f"P{piso}{letra_fila}{columna}"
        
        
        if self.vehiculoSeleccionado == "Moto":
            if index < 0 or index >= 120:
                return "Índice fuera de rango"

         # Calcula la fila y la columna
            piso = self.pisoSeleccionado
            fila = index // 8
            columna = (index % 8) + 1

         # Convierte el índice de fila a letra (A=65 en ASCII)
            letra_fila = chr(fila + 65)

            # Formatea la salida como 'A1', 'B2', etc.
            return f"P{piso}{letra_fila}{columna}"
        
        if self.vehiculoSeleccionado == "Movilidad Reducida":
            if index < 0 or index >= 10:
                return "Índice fuera de rango"

         # Calcula la fila y la columna
            piso = self.pisoSeleccionado
            fila = index // 5
            columna = (index % 5) + 1

         # Convierte el índice de fila a letra (A=65 en ASCII)
            letra_fila = chr(fila + 65)

            # Formatea la salida como 'A1', 'B2', etc.
            return f"P{piso}{letra_fila}{columna}"
        
    def index_to_position2(self, index, piso, tipo, movilidad):
        # Asegúrate de que el índice esté en el rango permitido
        if tipo == "Carro" and movilidad == 0:
            if index < 0 or index >= 80:
                return "Índice fuera de rango"

         # Calcula la fila y la columna
            fila = index // 8
            columna = (index % 8) + 1

         # Convierte el índice de fila a letra (A=65 en ASCII)
            letra_fila = chr(fila + 65)

            # Formatea la salida como 'A1', 'B2', etc.
            return f"P{piso}{letra_fila}{columna}"
        
        
        if tipo == "Moto" and movilidad == 0:
            if index < 0 or index >= 120:
                return "Índice fuera de rango"

         # Calcula la fila y la columna
            fila = index // 8
            columna = (index % 8) + 1

         # Convierte el índice de fila a letra (A=65 en ASCII)
            letra_fila = chr(fila + 65)

            # Formatea la salida como 'A1', 'B2', etc.
            return f"P{piso}{letra_fila}{columna}"
        
        if movilidad == 1:
            if index < 0 or index >= 10:
                return "Índice fuera de rango"

         # Calcula la fila y la columna
            fila = index // 5
            columna = (index % 5) + 1

         # Convierte el índice de fila a letra (A=65 en ASCII)
            letra_fila = chr(fila + 65)

            # Formatea la salida como 'A1', 'B2', etc.
            return f"P{piso}{letra_fila}{columna}"  
        
    def boton_presionado(self, event, id):
        a = self.index_to_position(id)
        if self.vehiculoSeleccionado == "Carro" and self.pisoSeleccionado == 1:
            vehiculo = self.infoCarro1[id]
        if self.vehiculoSeleccionado == "Moto" and self.pisoSeleccionado == 1:
            vehiculo = self.infoMoto1[id]
        if self.vehiculoSeleccionado == "Movilidad Reducida" and self.pisoSeleccionado == 1:
            vehiculo = self.infoMR1[id]
            
        if self.vehiculoSeleccionado == "Carro" and self.pisoSeleccionado == 2:
            vehiculo = self.infoCarro2[id]
        if self.vehiculoSeleccionado == "Moto" and self.pisoSeleccionado == 2:
            vehiculo = self.infoMoto2[id]
        if self.vehiculoSeleccionado == "Movilidad Reducida" and self.pisoSeleccionado == 2:
            vehiculo = self.infoMR2[id]
            
        if self.vehiculoSeleccionado == "Carro" and self.pisoSeleccionado == 3:
            vehiculo = self.infoCarro3[id]
        if self.vehiculoSeleccionado == "Moto" and self.pisoSeleccionado == 3:
            vehiculo = self.infoMoto3[id]
        if self.vehiculoSeleccionado == "Movilidad Reducida" and self.pisoSeleccionado == 3:
            vehiculo = self.infoMR3[id]
            
        if vehiculo == None:
            self.informacion_vehiculo.configure(text=a, font= ("Arial", 24))
            self.resultadoBusqueda = None
            self.eliminar_carro.configure(state=ctk.NORMAL)
            self.informacion_vehiculo.place(relx = 0.5, rely = 0.4, anchor = ctk.CENTER)
            self.informacion_vehiculo_titulo.place_forget()
            self.buscar_placa.delete(0, ctk.END)
            self.buscar_placa.place_forget()
            self.buscar_vehiculo_boton.place_forget()
            self.eliminar_carro.place_forget()
            self.buscarOtroVehiculo.place(relx = 0.5, rely = 0.85 , anchor = ctk.CENTER)
            self.tituloDetalles.place(relx = 0.5, rely = 0.150, anchor = ctk.CENTER)
            
        else:
            self.tituloDetalles.place(relx = 0.5, rely = 0.150, anchor = ctk.CENTER)
            self.informacion_vehiculo.configure(text=f"""Posición: {a}
Placa: {vehiculo.placa}
Tipo: {vehiculo.tipoVehiculo}
Ingreso: {vehiculo.horaEntrada}""", font= ("Arial", 18))
            self.resultadoBusqueda = vehiculo
            self.eliminar_carro.configure(state=ctk.NORMAL)
            self.informacion_vehiculo.place(relx = 0.5, rely = 0.4, anchor = ctk.CENTER)
            self.informacion_vehiculo_titulo.place_forget()
            self.buscar_placa.delete(0, ctk.END)
            self.buscar_placa.place_forget()
            self.buscar_vehiculo_boton.place_forget()
            self.eliminar_carro.place(relx = 0.5, rely=0.75, anchor = ctk.CENTER)
            self.buscarOtroVehiculo.place(relx = 0.5, rely = 0.85 , anchor = ctk.CENTER)
                
        
    
    def estacionamiento(self):
        piso = self.pisoSeleccionado
        vehiculo = self.vehiculoSeleccionado

        # Piso 1 y Carro
        if piso == 1 and vehiculo == "Carro":
            num_columnas = 8  
            num_filas = 10     
            contador = 0
            # Destruir botones existentes
            for boton in self.botonesCarro:
                boton.destroy()
            self.botonesCarro.clear()

            for boton in self.botonesMoto:
                boton.destroy()
            self.botonesMoto.clear()

            for boton in self.botonesMR:
                boton.destroy()
            self.botonesMR.clear()

            # Crear nuevos botones
            for i in range(80):  
                if self.estadoBotones(i) == None:
                    texto = "Disponible"
                else:
                    texto = "Ocupado"
                boton = ctk.CTkButton(master=self.panel2,
                                    text=texto,
                                    height=35,
                                    width=20)
                boton.grid(row=contador // num_columnas, column=contador % num_columnas, padx=5, pady=5)
                boton.id = i  # Asignar un identificador personalizado a cada botón
                boton.bind("<Button-1>", partial(self.boton_presionado, id=i))
                if texto == "Disponible":
                    boton.configure(fg_color="green", hover_color="#006400")
                else:
                    boton.configure(fg_color="red", hover_color = "#CC0000")
                    self.infoCarro1.append(self.estadoBotones(i))
                contador += 1
                self.botonesCarro.append(boton)

        # Piso 1 y Motos
        if piso == 1 and vehiculo == "Moto":
            num_columnas = 8  
            num_filas = 15     
            contador = 0
            # Destruir botones existentes
            for boton in self.botonesCarro:
                boton.destroy()
            self.botonesCarro.clear()

            for boton in self.botonesMoto:
                boton.destroy()
            self.botonesMoto.clear()

            for boton in self.botonesMR:
                boton.destroy()
            self.botonesMR.clear()

            # Crear nuevos botones
            for i in range(120):  
                if self.estadoBotones(i) == None:
                    texto = "Disponible"
                else:
                    texto = "Ocupado"
                boton = ctk.CTkButton(master=self.panel2,
                                    text=texto,
                                    height=27,
                                    width=10)
                boton.grid(row=contador // num_columnas, column=contador % num_columnas, padx=2, pady=2)
                contador += 1
                boton.id = i  # Asignar un identificador personalizado a cada botón
                boton.bind("<Button-1>", partial(self.boton_presionado, id=i))
                if texto == "Disponible":
                    boton.configure(fg_color="green", hover_color="#006400")
                else:
                    boton.configure(fg_color="red", hover_color = "#CC0000")
                    self.infoMoto1.append(self.estadoBotones(i))
                self.botonesMoto.append(boton)

        # Piso 1 y Movilidad Reducida
        if piso == 1 and vehiculo == "Movilidad Reducida":
            num_columnas = 5 
            num_filas = 2     
            contador = 0
            # Destruir botones existentes
            for boton in self.botonesCarro:
                boton.destroy()
            self.botonesCarro.clear()

            for boton in self.botonesMoto:
                boton.destroy()
            self.botonesMoto.clear()

            for boton in self.botonesMR:
                boton.destroy()
            self.botonesMR.clear()

            # Crear nuevos botones
            for i in range(10): 
                if self.estadoBotones(i) == None:
                    texto = "Disponible"
                else:
                    texto = "Ocupado"
                boton = ctk.CTkButton(master=self.panel2,
                                     text=texto,
                                    height=30,
                                    width=20)
                boton.grid(row=contador // num_columnas, column=contador % num_columnas, padx=2, pady=2)
                contador += 1
                boton.id = i  # Asignar un identificador personalizado a cada botón
                boton.bind("<Button-1>", partial(self.boton_presionado, id=i))
                if texto == "Disponible":
                    boton.configure(fg_color="green", hover_color="#006400")
                else:
                    boton.configure(fg_color="red", hover_color = "#CC0000")
                    self.infoMR1.append(self.estadoBotones(i))
                self.botonesMR.append(boton)
                
                
            # Piso 2 y Carro
        if piso == 2 and vehiculo == "Carro":
            num_columnas = 8  
            num_filas = 10     
            contador = 0
            # Destruir botones existentes
            for boton in self.botonesCarro:
                boton.destroy()
            self.botonesCarro.clear()

            for boton in self.botonesMoto:
                boton.destroy()
            self.botonesMoto.clear()

            for boton in self.botonesMR:
                boton.destroy()
            self.botonesMR.clear()

            # Crear nuevos botones
            for i in range(80):  
                if self.estadoBotones(i) == None:
                    texto = "Disponible"
                else:
                    texto = "Ocupado"
                boton = ctk.CTkButton(master=self.panel2,
                                    text=texto,
                                    height=35,
                                    width=20)
                boton.grid(row=contador // num_columnas, column=contador % num_columnas, padx=5, pady=5)
                contador += 1
                boton.id = i  # Asignar un identificador personalizado a cada botón
                boton.bind("<Button-1>", partial(self.boton_presionado, id=i))
                if texto == "Disponible":
                    boton.configure(fg_color="green", hover_color="#006400")
                else:
                    boton.configure(fg_color="red", hover_color = "#CC0000")
                    self.infoCarro2.append(self.estadoBotones(i))
                self.botonesCarro.append(boton)

        # Piso 2 y Motos
        if piso == 2 and vehiculo == "Moto":
            num_columnas = 8  
            num_filas = 15   
            contador = 0
            # Destruir botones existentes
            for boton in self.botonesCarro:
                boton.destroy()
            self.botonesCarro.clear()

            for boton in self.botonesMoto:
                boton.destroy()
            self.botonesMoto.clear()

            for boton in self.botonesMR:
                boton.destroy()
            self.botonesMR.clear()

            # Crear nuevos botones
            for i in range(120):  
                if self.estadoBotones(i) == None:
                    texto = "Disponible"
                else:
                    texto = "Ocupado"
                boton = ctk.CTkButton(master=self.panel2,
                                    text=texto,
                                    height=27,
                                    width=10)
                boton.grid(row=contador // num_columnas, column=contador % num_columnas, padx=2, pady=2)
                contador += 1
                boton.id = i  # Asignar un identificador personalizado a cada botón
                boton.bind("<Button-1>", partial(self.boton_presionado, id=i))
                if texto == "Disponible":
                    boton.configure(fg_color="green", hover_color="#006400")
                else:
                    boton.configure(fg_color="red", hover_color = "#CC0000")
                    self.infoMoto2.append(self.estadoBotones(i))
                self.botonesMoto.append(boton)

        # Piso 2 y Movilidad Reducida
        if piso == 2 and vehiculo == "Movilidad Reducida":
            num_columnas = 5 
            num_filas = 2     
            contador = 0
            # Destruir botones existentes
            for boton in self.botonesCarro:
                boton.destroy()
            self.botonesCarro.clear()

            for boton in self.botonesMoto:
                boton.destroy()
            self.botonesMoto.clear()

            for boton in self.botonesMR:
                boton.destroy()
            self.botonesMR.clear()

            # Crear nuevos botones
            for i in range(10):
                if self.estadoBotones(i) == None:
                    texto = "Disponible"
                else:
                    texto = "Ocupado"
                boton = ctk.CTkButton(master=self.panel2,
                                     text=texto,
                                    height=30,
                                    width=20)
                boton.grid(row=contador // num_columnas, column=contador % num_columnas, padx=2, pady=2)
                contador += 1
                boton.id = i  # Asignar un identificador personalizado a cada botón
                boton.bind("<Button-1>", partial(self.boton_presionado, id=i))
                if texto == "Disponible":
                    boton.configure(fg_color="green", hover_color="#006400")
                else:
                    boton.configure(fg_color="red", hover_color = "#CC0000")
                    self.infoMR2.append(self.estadoBotones(i))
                self.botonesMR.append(boton)
                
        # Piso 3 y Carro
        if piso == 3 and vehiculo == "Carro":
            num_columnas = 8  
            num_filas = 10     
            contador = 0
            # Destruir botones existentes
            for boton in self.botonesCarro:
                boton.destroy()
            self.botonesCarro.clear()

            for boton in self.botonesMoto:
                boton.destroy()
            self.botonesMoto.clear()

            for boton in self.botonesMR:
                boton.destroy()
            self.botonesMR.clear()

            # Crear nuevos botones
            for i in range(80):
                if self.estadoBotones(i) == None:
                    texto = "Disponible"
                else:
                    texto = "Ocupado"
                boton = ctk.CTkButton(master=self.panel2,
                                    text=texto,
                                    height=35,
                                    width=20)
                boton.grid(row=contador // num_columnas, column=contador % num_columnas, padx=5, pady=5)
                contador += 1
                boton.id = i  # Asignar un identificador personalizado a cada botón
                boton.bind("<Button-1>", partial(self.boton_presionado, id=i))
                if texto == "Disponible":
                    boton.configure(fg_color="green", hover_color="#006400")
                else:
                    boton.configure(fg_color="red", hover_color = "#CC0000")
                    self.infoCarro3.append(self.estadoBotones(i))
                self.botonesCarro.append(boton)

        # Piso 3 y Motos
        if piso == 3 and vehiculo == "Moto":
            num_columnas = 8  
            num_filas = 15     
            contador = 0
            # Destruir botones existentes
            for boton in self.botonesCarro:
                boton.destroy()
            self.botonesCarro.clear()

            for boton in self.botonesMoto:
                boton.destroy()
            self.botonesMoto.clear()

            for boton in self.botonesMR:
                boton.destroy()
            self.botonesMR.clear()

            # Crear nuevos botones
            for i in range(120): 
                if self.estadoBotones(i) == None:
                    texto = "Disponible"
                else:
                    texto = "Ocupado" 
                boton = ctk.CTkButton(master=self.panel2,
                                    text=texto,
                                    height=27,
                                    width=10)
                boton.grid(row=contador // num_columnas, column=contador % num_columnas, padx=2, pady=2)
                contador += 1
                boton.id = i  # Asignar un identificador personalizado a cada botón
                boton.bind("<Button-1>", partial(self.boton_presionado, id=i))
                if texto == "Disponible":
                    boton.configure(fg_color="green", hover_color="#006400")
                else:
                    boton.configure(fg_color="red", hover_color = "#CC0000")
                    self.infoMoto3.append(self.estadoBotones(i))
                self.botonesMoto.append(boton)

        # Piso 3 y Movilidad Reducida
        if piso == 3 and vehiculo == "Movilidad Reducida":
            num_columnas = 5 
            num_filas = 2     
            contador = 0
            # Destruir botones existentes
            for boton in self.botonesCarro:
                boton.destroy()
            self.botonesCarro.clear()

            for boton in self.botonesMoto:
                boton.destroy()
            self.botonesMoto.clear()

            for boton in self.botonesMR:
                boton.destroy()
            self.botonesMR.clear()

            # Crear nuevos botones
            for i in range(10):
                if self.estadoBotones(i) == None:
                    texto = "Disponible"
                else:
                    texto = "Ocupado"   
                boton = ctk.CTkButton(master=self.panel2,
                                     text=texto,
                                    height=30,
                                    width=20)
                boton.grid(row=contador // num_columnas, column=contador % num_columnas, padx=2, pady=2)
                contador += 1
                boton.id = i  # Asignar un identificador personalizado a cada botón
                boton.bind("<Button-1>", partial(self.boton_presionado, id=i))
                if texto == "Disponible":
                    boton.configure(fg_color="green", hover_color="#006400")
                else:
                    boton.configure(fg_color="red", hover_color = "#CC0000")
                    self.infoMR3.append(self.estadoBotones(i))
                self.botonesMR.append(boton)
              
crazy = Parqueadero()