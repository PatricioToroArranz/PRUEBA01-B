from material import Material

class Biblioteca:
    def __init__(self):
        self.materiales = []
    # agrega materiales a la biblioteca
    def agregar_material(self, material):
        print(f"Agregando material: {material.titulo}")
        self.materiales.append(material)

    def mostrar_catalogo(self):
        total = 0
        print("Catálogo de la Biblioteca:")
        for material in self.materiales:
            print(f"{material.descripcion()} | Precio: ${material.get_precio():.2f}")
            total += material.get_precio()
        print(f"Valor total del catálogo: ${total:.2f}")