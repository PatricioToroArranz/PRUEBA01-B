class Material:
   
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.__precio = precio  # Atributo encapsulado

    # Getter y Setter para el atributo encapsulado  
    def get_precio(self):
        return self.__precio

    def set_precio(self, nuevo_precio):

        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("El precio debe ser mayor que 0.")

    # Método que será sobreescrito → Polimorfismo
    def descripcion(self):
        return f"Material: Título {self.titulo}, Autor {self.autor}"
