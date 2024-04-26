import customtkinter as ctk
import random
import numpy as np

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Sistema de Gestión de Parqueaderos")
app.geometry("1000x700")

pisos = {
    'piso1': np.full((12, 10), None, dtype=object),
    'piso2': np.full((12, 10), None, dtype=object),
    'piso3': np.full((12, 10), None, dtype=object)
}

def mostrar_informacion(fila, columna, piso):
    espacio = pisos[piso][fila, columna]
    if espacio is None:
        result_label.configure(text=f"Piso {piso}, Fila {fila+1}, Puesto {columna+1}: Libre")
    else:
        result_label.configure(text=f"Piso {piso}, Fila {fila+1}, Puesto {columna+1}: Ocupado")

def asignar_parqueadero(fila, columna, piso):
    if pisos[piso][fila, columna] is None:
        pisos[piso][fila, columna] = {"estado": "Ocupado"}
        actualizar_piso_display(piso)
        result_label.configure(text=f"Parqueadero asignado: {piso} Fila {fila+1} Puesto {columna+1}")
    else:
        result_label.configure(text=f"Espacio ya ocupado: {piso} Fila {fila+1} Puesto {columna+1}")

def actualizar_piso_display(piso):
    for i in range(12):
        for j in range(10):
            estado = pisos[piso][i, j]
            color = "green" if estado is None else "red"
            parqueadero_buttons[i][j].configure(fg_color=color, text='Libre' if estado is None else 'Ocupado')

parqueadero_frame = ctk.CTkFrame(app)
parqueadero_frame.pack(pady=20, expand=True, fill='both')

parqueadero_buttons = [[ctk.CTkButton(parqueadero_frame, text="",
                                       width=80, height=40,
                                       command=lambda i=i, j=j: mostrar_informacion(i, j, piso_actual))
                        for j in range(10)] for i in range(12)]

for i in range(12):
    for j in range(10):
        parqueadero_buttons[i][j].grid(row=i, column=j)

result_label = ctk.CTkLabel(app, text="Seleccione un parqueadero")
result_label.pack(pady=20)

piso_actual = "piso1"

def cambiar_piso(piso):
    global piso_actual
    piso_actual = piso
    actualizar_piso_display(piso)
    result_label.configure(text=f"Mostrando disponibilidad para: {piso}")

piso_buttons = {piso: ctk.CTkButton(app, text=piso, command=lambda piso=piso: cambiar_piso(piso))
                for piso in pisos}
for i, btn in enumerate(piso_buttons.values(), start=1):
    btn.pack(side='left', padx=10)

actualizar_piso_display(piso_actual)

app.mainloop()
