class Persona():

    def __init__(self, nombre, edad, lugarResidencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = lugarResidencia

    def Descripcion(self):
         print("Nombre: ",self.nombre,"\nEdad: ",self.edad,"\nLugar de residencia: ",self.residencia)

class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombreE, edadE,residenciaE):
        super().__init__(nombreE,edadE,residenciaE)
        self.salario = salario
        self.antiguedad = antiguedad

    def Descripcion(self):
        print("Nombre: ",self.nombre,"\nEdad: ",self.edad,"\nLugar de residencia: ",self.residencia,"\nSueldo mensual: ",self.salario,"\nAntigüedad: ",self.antiguedad)

Eantonio = Empleado (1200,3,"Antonio",27,"España")
Eantonio.Descripcion()
