class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        if not self.cabeza: #Verifica si la lista enlazada está vacía, es decir, si no hay ningún nodo en la lista
            self.cabeza = Nodo(dato)
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(dato) #Mete un nodo al ultimo de la lista, cuando actual.siguiente = null

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        
        while actual:
            if actual.dato == dato:
                if anterior:
                    anterior.siguiente = actual.siguiente  # Conectar el nodo anterior con el siguiente de actual
                else:
                    self.cabeza = actual.siguiente  # Actualizar la cabeza si el nodo a eliminar es la cabeza
                return True  # Valor encontrado y eliminado
            anterior = actual
            actual = actual.siguiente
        return False  # Valor no encontrado en la lista
    
    def to_list(self):  # Convertir la lista enlazada a una lista de Python
        datos = []
        actual = self.cabeza
        while actual:
            datos.append(actual.dato) #Agrega el dato del nodo al final de la lista
            actual = actual.siguiente
        return datos

    def __str__(self):
        datos = self.to_list()
        return " -> ".join(map(str, datos)) #El map pasa los datos a STRING, el join hace que los datos se separen por el string que lo antecede