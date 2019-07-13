class Persona():
    def __init__(self, Nombre, Edad, Lugar_de_recidencia):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Recidencia = Lugar_de_recidencia

    def Descripcion(self):
        print ("\nNombre: " + self.Nombre + "\nEdad: " + str(self.Edad) + "\nLugar de recidencia: " + self.Recidencia)

class Empleado(Persona):
    def __init__(self, Sueldo, Cargo, nombre, edad, Lrecidencia):
        super().__init__(nombre, edad, Lrecidencia) # super() llama al metodo de la clase padre que corresponda
        self.Sueldo = Sueldo
        self.Cargo = Cargo

    # Esta Descripcion sobre escribe la de Persona debia que si el metodo
    # tiene el mismo nombre que del que hereda, python "corre" primordialmente esta clase.

    #def Descripcion(self):
    #    print("\nNombre: " + self.Nombre + "\nEdad: " + str(self.Edad) + "\nLugar de recidencia: " + self.Recidencia + "\nSueldo: " + str(self.Sueldo) + "\nCargo: " + self.Cargo)

    # Este no lo sobre escribe
    def Descripcion(self):
        super().Descripcion()
        print("Sueldo: " + str(self.Sueldo) + "\nCargo: " + self.Cargo)




TiagoEmpleado = Empleado(1000, "alguno", "santiago", 18, "Pereira")
TiagoEmpleado.Descripcion()
