from Vehiculo import Vehiculo
import random

class Parqueadero:
    def __init__(self):
        self.pisos = {1: {'autos': {}, 'motos': {}, 'movilidad_reducida': {}},
                      2: {'autos': {}, 'motos': {}, 'movilidad_reducida': {}},
                      3: {'autos': {}, 'motos': {}, 'movilidad_reducida': {}}}
        self.crear_espacios()

    def crear_espacios(self): #Llena los diccionarios con posiciones nulas que luego serán rellenadas
        for piso in self.pisos: 
            # Crear espacios para autos
            for i in range(1, 81):
                #El f"" sirve para concatenar cadenas
                self.pisos[piso]['autos'][f"P{piso}A{i}"] = None
            # Crear espacios para motos
            for i in range(1, 121):
                self.pisos[piso]['motos'][f'P{piso}M{i}'] = None
            # Crear espacios para movilidad reducida
            for i in range(1, 11):
                self.pisos[piso]['movilidad_reducida'][f'P{piso}MR{i}'] = None

    def registrar_ingreso(self, placa,tipo, propietario, movilidad_reducida, horaEntrada):
     categoria = 'movilidad_reducida' if movilidad_reducida else tipo
     nuevo_vehiculo = Vehiculo(placa, tipo, propietario, horaEntrada)

     for piso in self.pisos:
        espacios = self.pisos[piso][categoria]
        espacios_disponibles = [espacio for espacio, estado in espacios.items() if estado is None]
        
        if espacios_disponibles:
            espacio_elegido = random.choice(espacios_disponibles)  # Selecciona un espacio aleatoriamente
            espacios[espacio_elegido] = nuevo_vehiculo
            print(f'Vehículo con placa {nuevo_vehiculo._placa} asignado a {espacio_elegido}')
            return
    print('No hay espacios disponibles')
