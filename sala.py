class Sala:
    def __init__(self, id, nombre, ubicacion):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.obras = []

    def asignar_obra(self, obra):
        self.obras.append(obra)

    def listar_obras(self):
        return self.obras