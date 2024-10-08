class persona():
    #Constructor
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura


    #Atributos
    def saludar(self):
     print( f"La persona {self.nombre} esta saludando")
    nombre = "Santiago"
    Edad = 19
    altura = 1.66

#Main
nombre = input("Digite su nombre: ")
edad=input("Digite su edad: ")
altura= input("Digite su altura en m: ")
persona1 = persona("santiago", 19, 1.66)
persona2 = persona("Esmeralda",17,1.70)

print(persona1.saludar)
#print(persona1.nombre)
print(persona2.nombre)

persona1.nombre = "Esmeralda"
print(persona1.nombre)

