from Listas import *

class Vehiculo:
    def __init__(self, placa, propietario, horaEntrada, horaSalida = None): 
        self._placa = placa
        self._propietario = propietario
        self._horaEntrada = horaEntrada
        self._horaSalida = horaSalida
    
    @property
    def placa(self): #Getter Placa
        return self._placa
    
    @placa.setter
    def placa(self, nuevaPlaca): #Setter Placa
        self._placa = nuevaPlaca

    @property
    def propietario(self): #Getter Propietario
        return self._propietario

    @propietario.setter
    def propietario(self, nuevoPropietario): #Setter Propietario
        self._propietario = nuevoPropietario

    @property
    def horaEntrada(self): #Getter horaEntrada
        return self._horaEntrada

    @horaEntrada.setter #Setter horaEntrada
    def horaEntrada(self, nuevaHoraEntrada):
        self._horaEntrada = nuevaHoraEntrada
    
    @property
    def horaSalida(self): #Getter horaSalida
        return self._horaSalida

    @horaSalida.setter
    def horaSalida(self, nuevaHoraSalida): #Setter horaSalida
        self._horaSalida = nuevaHoraSalida

    def __str__(self): #ToString
        return f"{self._placa}, {self._propietario}, {self._horaEntrada}, {self._horaSalida or 'No especificada'})"

vehiculos = ListaEnlazada()
def agregarVehiculos(vehiculo):
    vehiculos.agregar(vehiculo)

def eliminarVehiculos(vehiculo):
    if (vehiculos.eliminar(vehiculo)):
        print ("Vehiculo eliminado con exito")
    else:
        print("No se pudo eliminar el vehiculo o no se encontró")
    