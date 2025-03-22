class Automovil:
    """Clase que representa un automóvil."""

    def __init__(self, marca, modelo, año, color):
        """
        Inicializa los atributos del automóvil.

        Args:
            marca (str): Marca del automóvil.
            modelo (str): Modelo del automóvil.
            año (int): Año del automóvil.
            color (str): Color del automóvil.
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def mostrar_informacion(self):
        """Muestra la información del automóvil."""
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")


# Crear una instancia de la clase Automovil
automovil1 = Automovil("Toyota", "Corolla", 2020, "Rojo")

# Usar el método de la clase
automovil1.mostrar_informacion()
