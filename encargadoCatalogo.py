from usuario import Usuario


class EncargadoCatalogo(Usuario):
    def __init__(self, id, nombre, clave, catalogo):
        super().__init__(id, nombre, "encargado_catalogo", clave)
        self.catalogo = catalogo

    def _encontrar_obra_por_id(self, id_obra):
        for obra in self.catalogo.obras:
            if obra.id == id_obra:
                return obra
        return None

    def registrar_obra(self, obra):
        self.catalogo.agregar_obra(obra)

    def editar_obra(self, id_obra, titulo, autor, periodo, estado):
        obra = self._encontrar_obra_por_id(id_obra)
        if obra is None:
            return False
        obra.titulo = titulo
        obra.autor = autor
        obra.periodo = periodo
        obra.estado = estado
        return True

    def eliminar_obra(self, id_obra):
        obra = self._encontrar_obra_por_id(id_obra)
        if obra is None:
            return False
        self.catalogo.obras.remove(obra)
        return True

    def clasificar_obra(self, id_obra, periodo):
        obra = self._encontrar_obra_por_id(id_obra)
        if obra is None:
            return False
        obra.periodo = periodo
        return True

    def asignar_sala(self, id_obra, sala):
        obra = self._encontrar_obra_por_id(id_obra)
        if obra is None:
            return False
        obra.sala = sala
        return True

    def listar_obras_por_sala(self, sala):
        return [obra for obra in self.catalogo.obras if getattr(obra, "sala", None) == sala]
