from material import Material

class Periodico(Material):
    def __init__(self, titulo, autor, precio, fecha_publicacion):
        super().__init__(titulo, autor, precio)
        self.fecha_publicacion = fecha_publicacion

    def descripcion(self):
        return f"Periodico: '{self.titulo}', Autor: {self.autor}, Fecha: {self.fecha_publicacion}"