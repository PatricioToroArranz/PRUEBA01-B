from material import Material

class Revista(Material):
    def __init__(self, titulo, autor, precio, edicion):
        super().__init__(titulo, autor, precio)
        self.edicion = edicion

    def descripcion(self):
        return f"Revista: '{self.titulo}', Autor: {self.autor}, Edición: {self.edicion}"