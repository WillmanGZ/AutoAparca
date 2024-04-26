import os
import re 
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

class Parqueadero:
    def __init__(self):
        self.principal = ctk.CTk()
        self.principal.geometry("1000x600")
        self.principal.title("Parqueadero")
        self.principal.resizable(False,False)
        ruta_icono = os.path.join(os.path.dirname(__file__), '..', 'icon.ico')
        self.principal.iconbitmap(ruta_icono)
        ctk.set_appearance_mode("System")  # Puede ser "System", "Dark", o "Light"
        ctk.set_default_color_theme("blue")  # Tema de color (hay varios temas disponibles)
        
        #Instanciar los pisos con sus respectivos espacios
        pisos = {1: {"carros1": [], "motos1": [], "movilidadreducida1":[]}, 
                 2: {"carros2": [], "motos2": [], "movilidadreducida2":[]}, 
                 3: {"carros3": [], "motos3": [], "movilidadreducida3":[]}}
        
        #Generar posiciones vacias en los carros
        for i in range(80):
            pisos[1]["carros1"].append(None)
            pisos[2]["carros2"].append(None)
            pisos[3]["carros3"].append(None)
        
        #Generar posiciones vacias en las motos
        for i in range(120):
            pisos[1]["motos1"].append(None)
            pisos[2]["motos2"].append(None)
            pisos[3]["motos3"].append(None)
        
        #Generar posiciones vacias en movilidad reducida
        for i in range(10):
            pisos[1]["movilidadreducida1"].append(None)
            pisos[2]["movilidadreducida2"].append(None)
            pisos[3]["movilidadreducida3"].append(None)
            
        #Panel que se usará para centrar los botones de disponibilidad de los pisos
        panel1 = ctk.CTkFrame(master=self.principal,
                             height= 580,
                             width= 670,
                             corner_radius= 15,
                             )
        panel1.place(relx=0.345, rely=0.5, anchor=ctk.CENTER)
        
        #Boton que al presionarlo, mostrará la disponibilidad de puestos del piso 1
        boton_piso1 = ctk.CTkButton(master=panel1,
                                    text= "Piso 1",
                                    command= self.botonPiso1,
                                    height= 25,
                                    width= 170,
                                    corner_radius= 15
                                    )
        boton_piso1.place(relx = 0.180, rely = 0.03, anchor = ctk.CENTER)
        
        #Boton que al presionarlo, mostrará la disponibilidad de puestos del piso 2
        boton_piso2 = ctk.CTkButton(master=panel1,
                                    text= "Piso 2",
                                    command= self.botonPiso2,
                                    height= 25,
                                    width= 170,
                                    corner_radius= 15
                                    )
        boton_piso2.place(relx = 0.5, rely = 0.03, anchor = ctk.CENTER)
        
        #Boton que al presionarlo, mostrará la disponibilidad de puestos del piso 3
        boton_piso3 = ctk.CTkButton(master=panel1,
                                    text= "Piso 3",
                                    command= self.botonPiso3,
                                    height= 25,
                                    width= 170,
                                    corner_radius=15
                                    )
        boton_piso3.place(relx = 0.820, rely = 0.03, anchor = ctk.CENTER)
        
        #Boton para seleccionar carro
        boton_carro = ctk.CTkButton(master=panel1,
                                    text= "Carro",
                                    command= self.botonCarro,
                                    height= 25,
                                    width= 170,
                                    corner_radius=15
                                    )
        boton_carro.place(relx = 0.180, rely = 0.1, anchor = ctk.CENTER)
        
        #Boton para seleccionar moto
        boton_moto = ctk.CTkButton(master=panel1,
                                    text= "Moto",
                                    command= self.botonMoto,
                                    height= 25,
                                    width= 170,
                                    corner_radius=15
                                    )
        boton_moto.place(relx = 0.5, rely = 0.1, anchor = ctk.CENTER)
        
        #Boton para seleccionar movilidad reducida
        boton_mr = ctk.CTkButton(master=panel1,
                                    text= "Movilidad Reducida",
                                    command= self.botonMR,
                                    height= 25,
                                    width= 170,
                                    corner_radius=15
                                    )
        boton_mr.place(relx = 0.820, rely = 0.1, anchor = ctk.CENTER)
        
        self.panel2 = ctk.CTkFrame(master= panel1,
                              height=480,
                              width=650,
                              corner_radius=15
                              )
        self.panel2.place(relx = 0.5, rely = 0.570, anchor = ctk.CENTER)
        #self.panel2.pack_propagate(False)  # Deshabilita el ajuste automático del tamaño del frame a su contenido
        #self.panel2.grid_propagate(False)
        
        ##############################################################################################################
        #Panel que se usará para centrar el ingreso/informacion de vehiculos
        panel3 = ctk.CTkFrame(master=self.principal,
                              height=580,
                              width=300,
                              corner_radius=15
                              )
        panel3.place(relx = 0.840, rely = 0.5, anchor = ctk.CENTER)
        
        
        #Titulo "Informacion de vehiculo"
        informacion_vehiculo_titulo = ctk.CTkLabel(master=panel3,
                                            text= "Informacion del vehiculo"
                                            )
        informacion_vehiculo_titulo.place(relx = 0.5, rely = 0.04, anchor = ctk.CENTER)
        
        #Texto que mostrará la informacion del vehiculo
        informacion_vehiculo = ctk.CTkLabel(master= panel3,
                                            text= "Sin informacion"
                                            )
        informacion_vehiculo.place(relx = 0.5, rely = 0.1, anchor = ctk.CENTER)
        
        #Para seleccionar el tipo de vehiculo
        opciones = ["Selecciona una opcion", "Carro", "Moto"]
        self.carro_moto = ctk.CTkComboBox(master=panel3,
                                     height= 25,
                                     width= 180,
                                     corner_radius=15,
                                     values= opciones,
                                     dropdown_hover_color= "gray",
                                     justify="center",
                                     state="readonly",
                                     )
        self.carro_moto.set(opciones[0])
        self.carro_moto.place(relx = 0.5, rely = 0.160, anchor = ctk.CENTER)
               
        #TextField de placa para la busqueda de un vehiculo
        self.buscar_placa = ctk.CTkEntry(master= panel3,
                                    height= 25,
                                    width= 180,
                                    corner_radius= 15,
                                    placeholder_text= "          Placa del vehiculo",
                                    placeholder_text_color= "gray"                          
                                    )
        self.buscar_placa.place(relx = 0.5, rely = 0.220, anchor = ctk.CENTER)
        
         #Checkbox para movilidad reducida
        movilidad_reducida = ctk.CTkCheckBox(master=panel3,
                                             height=3,
                                             width=3,
                                             corner_radius=5,
                                             text= "Movilidad Reducida")
        movilidad_reducida.place(relx = 0.5, rely = 0.280, anchor = ctk.CENTER)
        
        #Boton para buscar vehiculo mediante la placa
        buscar_vehiculo = ctk.CTkButton(master= panel3,
                                        height=25,
                                        width=180,
                                        text="Buscar vehiculo",
                                        corner_radius= 15,
                                        command=self.buscarVehiculo
                                        )
        buscar_vehiculo.place(relx = 0.5, rely = 0.340, anchor = ctk.CENTER)
        
        #Boton eliminar carro
        eliminar_carro = ctk.CTkButton(master=panel3,
                                       text= "Eliminar vehiculo",
                                       command=self.eliminarVehiculo,
                                       height= 25,
                                       width= 180,
                                       corner_radius= 15
                                       )
        eliminar_carro.place(relx = 0.5, rely = 0.400 , anchor = ctk.CENTER)
        
        
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
        
        self.principal.mainloop()
    
    def botonParqueadero(self): #Función que se usará para los botones del parqueadero(Solo los de disponibilidad)
            print("Hola")

    def botonPiso1(self):
        print("Boton Piso 1")
        self.pisoSeleccionado = 1
    
    def botonPiso2(self):
        print("Boton Piso 2")
    
    def botonPiso3(self):
        print("Boton Piso 3")
    
    def botonCarro(self):
        print("Carro")
        self.vehiculoSeleccionado = "Carro"
        self.estacionamiento()
        
    def botonMoto(self):
        print("Moto")
        self.vehiculoSeleccionado = "Moto"
        self.estacionamiento()
        
    def botonMR(self):
        print("Movilidad Reducida")
        self.vehiculoSeleccionado = "Movilidad Reducida"
        self.estacionamiento()
        
    def buscarVehiculo(self):
        placa = self.buscar_placa.get().upper()
        self.verificarPlaca(placa)
       
        
    def eliminarVehiculo(self):
        print("Eliminar vehiculo")
    
    #Para verificar si la placa es valida
    def verificarPlaca(self, placa):
        if placa == "":
            messagebox.showwarning("Digite su placa", "Porfavor digite su placa")
            return False
        else:
            if self.carro_moto.get() == "Carro":
                if self.formatoPlacaCarro(placa):
                    messagebox.showinfo("Correcto", "Formato Correcto")
                    return True
                else:
                    messagebox.showerror("Formato Incorrecto", "Porfavor digite una placa con el formato XXX000 (Sin espacios entre los digitos)")
                    return False
            elif self.carro_moto.get() == "Moto":
                if self.formatoPlacaMoto(placa):
                    messagebox.showinfo("Correcto", "Formato Correcto")
                    return True
                else:
                    messagebox.showerror("Formato incorrecto", "Porfavor digite una placa con el formato XXX000 o XXX 00X (Sin espacios entre los digitos)")
                    return False
            else:
                messagebox.showwarning("Elegir tipo de vehiculo", "Debe elegir el tipo de vehiculo")

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
        if(posicion == None):
            return "Disponible"
        else:
            return "Ocupado"
    
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
                boton = ctk.CTkButton(master=self.panel2,
                                    text=self.estadoBotones(i),
                                    height=35,
                                    width=20)
                boton.grid(row=contador // num_columnas, column=contador % num_columnas, padx=5, pady=5)
                contador += 1
                self.botonesCarro.append(boton)

        # Piso 1 y Motos
        if piso == 1 and vehiculo == "Moto":
            num_columnas = 10  
            num_filas = 12     
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
                boton = ctk.CTkButton(master=self.panel2,
                                    text=self.estadoBotones(i),
                                    height=10,
                                    width=1)
                boton.grid(row=contador // num_columnas, column=contador % num_columnas, padx=2, pady=2)
                contador += 1
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
                boton = ctk.CTkButton(master=self.panel2,
                                     text=self.estadoBotones(i),
                                    height=30,
                                    width=20)
                boton.grid(row=contador // num_columnas, column=contador % num_columnas, padx=2, pady=2)
                contador += 1
                self.botonesMR.append(boton)

        

                
crazy = Parqueadero()