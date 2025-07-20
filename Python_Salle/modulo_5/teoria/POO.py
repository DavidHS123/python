# Programación Orientada a Objetos (POO)
# En Python, la POO se basa en la creación de clases y objetos.

# Definiciones:
# - Clase: Es un molde o plantilla para crear objetos. Define atributos y métodos.
# - Objeto: Es una instancia de una clase. Tiene sus propios valores para los atributos
# - Atributo: Es una variable que pertenece a una clase y define el estado del objeto.
# - Método: Es una función definida dentro de una clase que define el comportamiento del objeto.

# Ejemplo de una clase simple
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print("¡Guau! Mi nombre es", self.nombre)
# Método para mostrar la edad del perro
    def mostrar_edad(self):
        print("Tengo", self.edad, "años")

# Creación de un objeto de la clase Perro
mi_perro = Perro("Rex", 5)
# Llamada a los métodos del objeto
mi_perro.ladrar()
mi_perro.mostrar_edad()

# Herencia: Permite crear una nueva clase basada en una clase existente.
class PerroSalchicha(Perro):
    def __init__(self, nombre, edad, longitud_cuerpo):
        super().__init__(nombre, edad)
        self.longitud_cuerpo = longitud_cuerpo

    def mostrar_info(self):
        self.ladrar()
        self.mostrar_edad()
        print("Soy un perro salchicha y mi longitud es de", self.longitud_cuerpo, "cm")

# Creación de un objeto de la clase PerroSalchicha
mi_perro_salchicha = PerroSalchicha("Fido", 3, 30)
mi_perro_salchicha.mostrar_info()