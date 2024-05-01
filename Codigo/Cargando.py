
from tkinter import *
from PIL import Image, ImageTk
import time
from Login import Login

class Cargando:
    def __init__(self) -> None:
        self.principal=Tk()
        width_of_window = 427
        height_of_window = 250
        screen_width = self.principal.winfo_screenwidth()
        screen_height = self.principal.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        self.principal.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
        self.principal.overrideredirect(1) #Para que no haya titulo en la barra superior

        #Frame para base de color
        Frame(self.principal, width=427, height=250, bg='#272727').place(x=0,y=0)

        #Crea y carga los objetos para las imagenes
        image_a=ImageTk.PhotoImage(Image.open('imagenes/c2.png'))
        image_b=ImageTk.PhotoImage(Image.open('imagenes/c1.png'))
        carrito_img_path = "imagenes/carrito.png"
        carrito_photo = self.create_photo_image(carrito_img_path)

        #Canvas sobre el que se pone la imagen para poder usar transparencia
        canvas = Canvas(self.principal, width=450, height=250, bg='#272727')
        canvas.place(relx=0.490, rely=0.5, anchor=CENTER)

        #Mantener referencia de la imagen
        canvas.carrito_photo = carrito_photo 
        canvas.create_image(225, 90, image=canvas.carrito_photo) #Crea la imagen del carrito sobre el canvas
        canvas.create_text(225, 150, text="AutoAparca", fill="white", font=("Game Of Squids", 24, "bold")) #Crea el titulo Auto aparca sobre el canvas
        label1=Label(self.principal, text='Cargando...', fg='white', bg='#272727') #Crea el label de cargando... sobre el frame principal
        label1.configure(font=("Calibri", 11))
        label1.place(x=10,y=215)

        #Hace la animacion de cargar actualizando cada frame las imagenes
        for i in range(4): 
            l1=Label(self.principal, image=image_a, border=0, relief=SUNKEN).place(x=180, y=175)
            l2=Label(self.principal, image=image_b, border=0, relief=SUNKEN).place(x=200, y=175)
            l3=Label(self.principal, image=image_b, border=0, relief=SUNKEN).place(x=220, y=175)
            l4=Label(self.principal, image=image_b, border=0, relief=SUNKEN).place(x=240, y=175)
            self.principal.update_idletasks() #Se necesita para actualizar elementos de la interfaz de usuario durante una operación prolongada
            time.sleep(0.5)

            l1=Label(self.principal, image=image_b, border=0, relief=SUNKEN).place(x=180, y=175)
            l2=Label(self.principal, image=image_a, border=0, relief=SUNKEN).place(x=200, y=175)
            l3=Label(self.principal, image=image_b, border=0, relief=SUNKEN).place(x=220, y=175)
            l4=Label(self.principal, image=image_b, border=0, relief=SUNKEN).place(x=240, y=175)
            self.principal.update_idletasks()
            time.sleep(0.5)

            l1=Label(self.principal, image=image_b, border=0, relief=SUNKEN).place(x=180, y=175)
            l2=Label(self.principal, image=image_b, border=0, relief=SUNKEN).place(x=200, y=175)
            l3=Label(self.principal, image=image_a, border=0, relief=SUNKEN).place(x=220, y=175)
            l4=Label(self.principal, image=image_b, border=0, relief=SUNKEN).place(x=240, y=175)
            self.principal.update_idletasks()
            time.sleep(0.5)

            l1=Label(self.principal, image=image_b, border=0, relief=SUNKEN).place(x=180, y=175)
            l2=Label(self.principal, image=image_b, border=0, relief=SUNKEN).place(x=200, y=175)
            l3=Label(self.principal, image=image_b, border=0, relief=SUNKEN).place(x=220, y=175)
            l4=Label(self.principal, image=image_a, border=0, relief=SUNKEN).place(x=240, y=175)
            self.principal.update_idletasks()
            time.sleep(0.5)
        
        self.cargarLogin()
        self.principal.mainloop()
        
    
    #Para asegurarse que la img tiene fondo transparente, re dimensionarla y ponerla en mejor calidad
    def create_photo_image(self, file_path):
        img = Image.open(file_path)
        img = img.convert("RGBA")  # Asegura que está en modo RGBA para transparencia
        img = img.resize((120, 140), Image.BICUBIC)  # Usa BICUBIC para mejor calidad
        return ImageTk.PhotoImage(img)
    
    #Para que se destruya despues de que termine
    def cargarLogin(self):
        self.principal.destroy()
        Login()
        