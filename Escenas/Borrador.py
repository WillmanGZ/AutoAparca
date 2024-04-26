import re 
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

class Parqueadero:
    def __init__(self):
        self.principal = ctk.CTk()
        self.principal.geometry("900x600")
        self.principal.title("Parqueadero")
        self.principal.resizable(False,False)
        
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
            
        #Boton que al presionarlo, mostrará la disponibilidad de puestos del piso 1
        boton_piso1 = ctk.CTkButton(master=self.principal,
                                    text= "Piso 1",
                                    command= self.botonPiso1,
                                    height= 25,
                                    width= 200,
                                    corner_radius= 15
                                    )
        boton_piso1.grid(row = 0, column = 0)
        
        #Boton que al presionarlo, mostrará la disponibilidad de puestos del piso 2
        boton_piso2 = ctk.CTkButton(master=self.principal,
                                    text= "Piso 2",
                                    command= self.botonPiso2,
                                    height= 25,
                                    width= 200,
                                    corner_radius= 15
                                    )
        boton_piso2.grid(row = 0, column = 1)
        
        #Boton que al presionarlo, mostrará la disponibilidad de puestos del piso 3
        boton_piso3 = ctk.CTkButton(master=self.principal,
                                    text= "Piso 3",
                                    command= self.botonPiso3,
                                    height= 25,
                                    width= 200,
                                    corner_radius=15
                                    )
        boton_piso3.grid(row = 0, column = 2)
        
        #Panel que se usará para centrar los botones de disponibilidad de los pisos
        panel1 = ctk.CTkFrame(master=self.principal,
                             height= 560,
                             width= 600,
                             corner_radius= 15,
                             )
        panel1.place(relx=0.345, rely=0.515, anchor=ctk.CENTER)
        
        #Panel que se usará para centrar el ingreso/informacion de vehiculos
        panel2 = ctk.CTkFrame(master=self.principal,
                              height=560,
                              width=200,
                              corner_radius=15
                              )
        panel2.place(relx = 0.850, rely = 0.515, anchor = ctk.CENTER)
        
        
        #Titulo "Informacion de vehiculo"
        informacion_vehiculo_titulo = ctk.CTkLabel(master=panel2,
                                            text= "Informacion del vehiculo"
                                            )
        informacion_vehiculo_titulo.place(relx = 0.5, rely = 0.04, anchor = ctk.CENTER)
        
        #Texto que mostrará la informacion del vehiculo
        informacion_vehiculo = ctk.CTkLabel(master= panel2,
                                            text= "Sin informacion"
                                            )
        informacion_vehiculo.place(relx = 0.5, rely = 0.1, anchor = ctk.CENTER)
        
        #Para seleccionar el tipo de vehiculo
        opciones = ["Selecciona una opcion", "Carro", "Moto"]
        self.carro_moto = ctk.CTkComboBox(master=panel2,
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
        self.buscar_placa = ctk.CTkEntry(master= panel2,
                                    height= 25,
                                    width= 180,
                                    corner_radius= 15,
                                    placeholder_text= "          Placa del vehiculo",
                                    placeholder_text_color= "gray"                          
                                    )
        self.buscar_placa.place(relx = 0.5, rely = 0.220, anchor = ctk.CENTER)
        
         #Checkbox para movilidad reducida
        movilidad_reducida = ctk.CTkCheckBox(master=panel2,
                                             height=3,
                                             width=3,
                                             corner_radius=5,
                                             text= "Movilidad Reducida")
        movilidad_reducida.place(relx = 0.5, rely = 0.280, anchor = ctk.CENTER)
        
        #Boton para buscar vehiculo mediante la placa
        buscar_vehiculo = ctk.CTkButton(master= panel2,
                                        height=25,
                                        width=180,
                                        text="Buscar vehiculo",
                                        corner_radius= 15,
                                        command=self.buscarVehiculo
                                        )
        buscar_vehiculo.place(relx = 0.5, rely = 0.340, anchor = ctk.CENTER)
        
        #Boton eliminar carro
        eliminar_carro = ctk.CTkButton(master=panel2,
                                       text= "Eliminar vehiculo",
                                       command=self.eliminarVehiculo,
                                       height= 25,
                                       width= 180,
                                       corner_radius= 15
                                       )
        eliminar_carro.place(relx = 0.5, rely = 0.400 , anchor = ctk.CENTER)
        
        self.principal.mainloop()
    
    def botonParqueadero(self): #Función que se usará para los botones del parqueadero(Solo los de disponibilidad)
            print("Hola")

    def estadoBotones(self, posicion):
        if(posicion == None):
            return False
        else:
            return True
    
    def botonPiso1(self):
        print("Boton Piso 1")
    
    def botonPiso2(self):
        print("Boton Piso 2")
    
    def botonPiso3(self):
        print("Boton Piso 3")
        
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
        
        
crazy = Parqueadero()