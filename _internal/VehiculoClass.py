class Vehiculo:
    def __init__(self, placa, tipoVehiculo, movilidadReducida): #Los _ de los att representan private
        self._placa = placa
        self._tipoVehiculo = tipoVehiculo
        self._movilidadReducida = movilidadReducida
        self._posicion = None
        self._horaEntrada = None

    @property
    def placa(self): #Getter placa
        return self._placa

    @placa.setter
    def placa(self, nuevaPlaca): #Setter placa
        self._placa = nuevaPlaca

    @property
    def tipoVehiculo(self): #Getter tipovehiculo
        return self._tipoVehiculo

    @tipoVehiculo.setter
    def tipoVehiculo(self, nuevoTipoVehiculo): #Setter tipo vehiculo
        self._tipoVehiculo = nuevoTipoVehiculo

    @property
    def movilidadReducida(self): #Getter movilidad reducida
        return self._movilidadReducida

    @movilidadReducida.setter
    def movilidadReducida(self, movilidadReducida): #Setter movilidad reducida
        self._movilidadReducida = movilidadReducida
        
    @property
    def posicion(self): #Getter posicion
        return self._posicion

    @posicion.setter
    def posicion(self, nuevaPosicion): #Setter posicion
        self._posicion = nuevaPosicion
        
    @property
    def horaEntrada(self): #Getter hora de entrada
        return self._horaEntrada

    @horaEntrada.setter
    def horaEntrada(self, nuevaHora): #Setter hora de entrada
        self._horaEntrada = nuevaHora
    
    def __repr__(self): #Algo asi como el toString
        return f"Vehículo {self._placa}, Tipo: {self._tipoVehiculo}, Movilidad Reducida: {self._movilidadReducida}, Posición: {self._posicion}, Hora de entrada: {self._horaEntrada}"
