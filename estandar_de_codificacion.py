class Empleado:

    def __init__(self, nombre, salario_base, horas_extra=0):
        self._nombre = nombre
        self._salario_base = salario_base
        self._horas_extra = horas_extra

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        self._salario_base = salario_base

    @property
    def horas_extra(self):
        return self._horas_extra

    @horas_extra.setter
    def horas_extra(self, horas_extra):
        self._horas_extra = horas_extra

    def calcular_sueldo(self):
        """
        Calcula el sueldo total, incluyendo las horas extras.
        El pago por hora extra es un 50% más que el salario base por hora.
        """
        salario_por_hora = self._salario_base / 160  #jornada de 160 horas al mes.
        pago_extra = self._horas_extra * salario_por_hora * 1.5  # 50% más por cada hora extra.
        return self._salario_base + pago_extra

    def __str__(self):
        return f"Empleado: {self._nombre}, Sueldo Base: {self._salario_base}, Horas Extra: {self._horas_extra}"

empleado1 = Empleado("Carlos Pérez", 2000)
empleado2 = Empleado("Ana Gómez", 1500, 20)

# Mostrar información de los empleados
print(empleado1)
print(empleado2)

# Calcular sueldos
print(f"Sueldo total de {empleado1.nombre}: bs{empleado1.calcular_sueldo():.2f}")
print(f"Sueldo total de {empleado2.nombre}: bs{empleado2.calcular_sueldo():.2f}")
