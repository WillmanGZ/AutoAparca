import tkinter as tk
from tkinter import messagebox, ttk
from random import choice
from datetime import datetime

class Vehiculo:
    def _init_(self, placa, movilidad_reducida=False):
        self.placa = placa
        self.movilidad_reducida = movilidad_reducida

def asignar_parqueadero():
    piso = choice([1, 2, 3])
    fila = choice(['A', 'B', 'C', 'D'])
    puesto = choice(range(1, 7))
    return f'P{piso}{fila}{puesto}'

def registrar_ingreso():
    placa = placa_entry.get()
    movilidad_reducida = movilidad_reducida_var.get()
    if placa:
        vehiculo = Vehiculo(placa, movilidad_reducida)
        registros.append(vehiculo)
        parqueadero_asignado = asignar_parqueadero()
        parqueaderos.append(parqueadero_asignado)
        hora_ingreso.append(datetime.now())
        messagebox.showinfo("Registro de ingreso", f"El vehículo fue asignado al parqueadero: {parqueadero_asignado}")
    else:
        messagebox.showerror("Error", "Debe ingresar la placa del vehículo")

def mostrar_disponibilidad():
    disponibilidad_window = tk.Toplevel(root)
    disponibilidad_window.title("Disponibilidad de Parqueaderos")
    disponibilidad_window.geometry("320x300")

    canvas = tk.Canvas(disponibilidad_window)
    scrollbar = ttk.Scrollbar(disponibilidad_window, orient="vertical", command=canvas.yview)
    frame = tk.Frame(canvas)

    canvas.create_window((0, 0), window=frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Función para configurar los límites de la barra de desplazamiento vertical
    def _configure_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    for piso in range(1, 4):
        piso_frame = tk.Frame(frame)
        piso_frame.pack(pady=5)

        piso_label = tk.Label(piso_frame, text=f"Piso {piso}")
        piso_label.grid(row=0, column=0, columnspan=6)

        for fila_idx, fila in enumerate(['A', 'B', 'C', 'D'], start=1):
            fila_label = tk.Label(piso_frame, text=fila)
            fila_label.grid(row=fila_idx, column=0, padx=5)

            for puesto in range(1, 7):
                estado = "Ocupado" if f'P{piso}{fila}{puesto}' in parqueaderos else "Disponible"
                color = "red" if estado == "Ocupado" else "green"
                puesto_label = tk.Label(piso_frame, text=puesto, bg=color)
                puesto_label.grid(row=fila_idx, column=puesto, padx=5)

    # Configurar los límites de la barra de desplazamiento vertical
    frame.bind("<Configure>", _configure_scroll_region)

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Parqueadero")
root.geometry("400x300")

# Variables globales
registros = []
parqueaderos = []
hora_ingreso = []

# Widgets
placa_label = tk.Label(root, text="Placa del vehículo:")
placa_label.pack()
placa_entry = tk.Entry(root)
placa_entry.pack()

movilidad_reducida_var = tk.BooleanVar()
movilidad_reducida_check = tk.Checkbutton(root, text="Movilidad reducida", variable=movilidad_reducida_var)
movilidad_reducida_check.pack()

registrar_ingreso_button = tk.Button(root, text="Registrar Ingreso", command=registrar_ingreso)
registrar_ingreso_button.pack()

disponibilidad_button = tk.Button(root, text="Mostrar Disponibilidad", command=mostrar_disponibilidad)
disponibilidad_button.pack()

root.mainloop()