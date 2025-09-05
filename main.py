from biblioteca import Biblioteca
from libro import Libro
from revista import Revista
from periodico import Periodico
from material import Material




if __name__ == "__main__":
    # Se crea una biblioteca
    biblioteca = Biblioteca()

    # Se instancian los materiales (Libro, Revista, Periódico)
    libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 15000, 471)
    revista = Revista("National Geographic", "Varios", 5000, 202)
    periodico = Periodico("El Mercurio", "Redacción", 1000, "04/09/2025")

    # Se usa el setter para modificar el precio de la revista
    revista.set_precio(6000)

    # Se agregan los materiales a la biblioteca
    biblioteca.agregar_material(libro)
    biblioteca.agregar_material(revista)
    biblioteca.agregar_material(periodico)

    # Se muestra el catálogo completo
    biblioteca.mostrar_catalogo()