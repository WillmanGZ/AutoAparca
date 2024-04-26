import tkinter as tk
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
                                    height= 20,
                                    width= 200,
                                    )
        boton_piso1.grid(row = 0, column = 0)
        
        #Boton que al presionarlo, mostrará la disponibilidad de puestos del piso 2
        boton_piso2 = ctk.CTkButton(master=self.principal,
                                    text= "Piso 2",
                                    command= self.botonPiso2,
                                    height= 20,
                                    width= 200,
                                    )
        boton_piso2.grid(row = 0, column = 1)
        
        #Boton que al presionarlo, mostrará la disponibilidad de puestos del piso 3
        boton_piso3 = ctk.CTkButton(master=self.principal,
                                    text= "Piso 3",
                                    command= self.botonPiso3,
                                    height= 20,
                                    width= 200,
                                    )
        boton_piso3.grid(row = 0, column = 2)
        
        #Panel que se usará para centrar los botones de disponibilidad de los pisos
        panel = ctk.CTkFrame(master=self.principal,
                             height= 560,
                             width= 600,
                             corner_radius= 15,
                             )
        panel.place(relx=0.345, rely=0.515, anchor=ctk.CENTER)
        
        
        
        
        
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
        
        
        
        
crazy = Parqueadero()