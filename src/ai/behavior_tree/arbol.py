class Nodo:
    def __init__(self):
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def ejecutar(self):
       pass
class Selector(Nodo):
    def ejecutar(self):
        for hijo in self.hijos:
            if hijo.ejecutar():
                return True
        return False

class Secuencia(Nodo):
    def ejecutar(self):
        for hijo in self.hijos:
            if not hijo.ejecutar():
                return False
        return True

class Accion(Nodo):
    def __init__(self, accion):
        super().__init__()
        self.accion = accion

    def ejecutar(self):
        return self.accion()

class Buscar(Nodo):
    def __init__(self, buscar):
        super().__init__()
        self.accion = buscar

    def ejecutar(self):
        return self.buscar()
