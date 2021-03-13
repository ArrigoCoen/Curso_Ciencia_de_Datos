#Función sin parámetros
def calculadora():
    '''Esta función pregunta al usuario 2 números a y b.
    Realiza operaciones elementales con a y b'''
    a = input("Escribe un número:\n")#Con la función 'input()' se lee lo que escribe el usuario
    b = input("Escribe un número:\n")
    # La 'f' antes de las comillas permite leer la variable que se encuentra en llaves '{}'.
    print(f'{a} + {b} = {float(a)+float(b)}')
    print(f'{a} - {b} = {float(a)-float(b)}')
    print(f'{a} * {b} = {float(a)*float(b)}')
    print(f'{b} / {a} = {round(float(b)/float(a),2)}')


#Función con parámetros
def calculadora2(a,b):
    '''Esta función recibe 2 parámetros, los números a y b.
    Realiza operaciones elementales con a y b'''
    # La 'f' antes de las comillas permite leer la variable que se encuentra en llaves '{}'.
    print(f'{a} + {b} = {float(a)+float(b)}')
    print(f'{a} - {b} = {float(a)-float(b)}')
    print(f'{a} * {b} = {float(a)*float(b)}')
    print(f'{b} / {a} = {float(b)/float(a)}')


dic1 = dict([(1,'agua'),(2,'luz'),(3,'gas'),(4,'teléfono'),(5,'ocio')])


dic2 = {
  "marca": "Ford",
  "automático": False,
  "eléctrico": True,
  "año": 1968,
  "colores": ["rojo", "negro", "azul"]
}


# Clase Padre 1
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludo(self):
        print("Hola, mi nombre es ",self.nombre," y tengo ",self.edad," años.\n")
        
    def despedida(self,amigo):
        print("Adiós ",amigo)


#Clase Padre 2
class Habilidades:
    def __init__(self,hab1,hab2,hab3):
        self.hab1 = hab1
        self.hab2 = hab2
        self.hab3 = hab3
        
    def muestra_hab(self):
        habs = self.hab1,self.hab2,self.hab3 #Tuple
        for i in range(0,len(habs)):
            print("Mi habilidad ",i+1," es: ",habs[i])

#Clase Hijo
class Estudiante(Persona,Habilidades):
    def __init__(self,nombre,edad, #Propiedades de la clase "Persona"
                 hab1,hab2,hab3, #Propiedades de la clase "Habilidades"
                 carrera,num_cuenta):  #Propiedades de la clase "Estudiante"
        
        Persona.__init__(self,nombre,edad) #Constructor de la clase "Persona"
        Habilidades.__init__(self,hab1,hab2,hab3) #Constructor de la clase "Habilidades"
        
        #Propiedades de "Estudiante"
        self.carrera = carrera
        self.num_cuenta= num_cuenta
        
    def datos(self):
        self.saludo()
        self.muestra_hab()
        print("\nEstudio ",self.carrera," y mi número de cuenta es: ",self.num_cuenta)

e1 = Estudiante("Juan",18,"Escribir","Dibujar","Contar","Matemáticas",1234)