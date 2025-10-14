import matplotlib
class Estudiante():
    def __ini__(self , nombre , nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print(f"Nombre:{self.nombre} \nNota: {self.nota}")

    def resultados(self):
        if self.nota >= 7:
            print("Has APROBADO!")
        else:
            print("Has REPROBADO!")

estudiante1=Estudiante("Pedro" , 5)
estudiante1.imprimir()
estudiante1.resultados()

estudiante2=Estudiante("Elizabeth" , 7)
estudiante2.imprimir()
estudiante2.resultados()