#! /usr/bin/python

#-*- coding: utf-8 -*-

class Cultivo: # Creamos la clase con class y asignaos el nombre de la clase, de preferencia se nombre con letra mayuscula.
    """Cultivo de alimentos general""" # Configuramos la estrucutra básica de la clase
    
    # constructor de la clase: adicionamos el método de construcción.
    
    def __init__(self, tasa_crecimiento, luz_necesaria, agua_necesaria):
        
        # Agregan atributos al método de contrucción con un valor inicial
        # Todos los atributos siempre s inician con **self.**
        
        self.crecimiento = 0
        self.dias_crecimiento = 0
        self.tasa_crecimiento = tasa_crecimiento
        self.luz_necesaria = luz_necesaria
        self.agua_necesaria = agua_necesaria
        self.status = "semilla"
        self.tipo = "genérico"
        
        #Publicos
        
        # Los atributos pueden publicos o privados, es decir se puede acceder a ellos desde otra clase o no, respectivamente.
        
        #Privados: para hacerlos privados debemos colocar un guion bajo antes del nombre del atributo
        
        self._crecimiento = 0
        self._dias_creciendo = 0
        self._tasa_crecimiento = tasa_crecimiento
        self._luz_necesaria = luz_necesaria
        self._agua_necesaria = agua_necesaria
        self._status = "semilla"
        self._tipo = "Generico"
    
    # A este proceso se le conoce como Encapsulation = Encapsulacion
    # EL objetivo de la encapsulacion es ocultar los detalles de la implementacion de un método
    # al usuario. resulta util cuando no necesitas entender como el metodo funciono sino simplemente como controlarla mediante la interfaz.
    
    # Instantiation: generacion de objetos o instancias de nuestra clase.
    # Adicionamos una funcion main() a nuestro modulo de clase.
    
    # Adicionar METODOS a nuestra clase Cultivo.
    
    def necesidades(self):
        # Generar un diccionario que contenga las necesidades de luz y de agua para nuestro cultivo.
        return {'luz necesaria':self._luz_necesaria, 'agua necesaria':self._agua_necesaria }
    
    # Metodo para reportar el estado actual de nuestro cultivo.
    def reporte(self):
        return{'tipo':self._tipo, 'status':self._status, 'crecimiento':self._crecimiento, 'dias de crecimiento':self._dias_creciendo}
    
    
    # Adicionaremos un segundo metodo para ir actualizando el crecimiento del cultivo
    # este nuevo metodo necesitara de dos parametros
    # la luz diposinble actual y el agua disponible actual: representan las condiciones ambientales actuales de un dia particular.
    # si el cultivo recive las cantidades de agua y luz necesarias por dia, este, crecera basado en la taza de creceiminto.
    
    def _actual_status(self):
        # Adiciona funcionalidad al metodo 'actual_status'
        if self._crecimiento > 15:
            self._status = "Viejo"
        elif self._crecimiento > 10:
            self._status = "Maduro"
        elif self._crecimiento > 5:
            self._status = "Joven"
        elif self._crecimiento > 0:
            self._status = "Plantulas"
        elif self._crecimiento == 0:
            self._status = "Semilla"

# adicionamos el metodo
def crecer(self, luz, agua):
    if luz >= self._luz_necesaria and agua >= self._agua_necesaria:
        self._crecimiento += self._tasa_crecimiento
        #Incremento del crecimiento en dias
        self._dias_creciendo += 1
        #actualizacion del status
        self._actual_status()

# Adicionar funciones automaticas
# Ahora generaremos una funcion ara evauar el cultivo sobre un periodo de tiempo largo.
# Nosotors aportaremos en esta funcion un unmero de dias que nosotros deseamos para que el cultivo crezca.
# y este, generare aleatoriamente una cantidad de luz y de agua por cada dia. una vez que los valores de agua y luz estan designados
# esta funcion llamara al metodo grow de nuestro objeto "cultivo", y este proceso se repetira por el numero de dias deaseado.

def auto_crecer(cultivo, dias):
    # crecimineto del cultivo
    for dia in range(dias):
        luz =  random.randint(1,10)
        agua = random.randint(1,10)
        # Adicionamos la funcion para mandar llamar al metodo cultivo aleatorio
        cultivo.crecer(luz, agua)

def main():
    #Instanciamos la clase
    nuevo_cultivo = Cultivo(2, 5, 10)
    # Evaluar el nuevo objeto revisando los valores de sus atributos iniciales
    print(nuevo_cultivo.necesidades())
    # podemos idexar un valor especifico de nuestro nuevo metodo
    # print(nuevo_cultivo.necesidades()['luz necesaria'])
    print(nuevo_cultivo.reporte())
    #hacemos pasar la funcion
    auto_crecer(nuevo_cultivo,30)
    print(nuevo_cultivo.reporte())


# Ahora haremos una funcion en la cual nos permita realizar un crecimiento manual que nos proveera de valores especificos
# por lo que nosotros podremos evaluar dichos valores en un rango apropuado y analizar si lo realiza de la forma esperada
# cuando recive un par de valores particulares de agua y de luz, es decir, evaliar el crecimiento en funcion de un predictor.
# Adicionamos la funcion "manual_crecer al modulo"

def manual_crecer(cultivo):
    # pedir los valores de luz y agua al usuario:
    valid =  False
    while not valid:
        try:
            # Adicionamos un codigo para pedirle al usuario el valor de luz.
            # Adicionaremos una condicion cuando el valor agregado no este dentro del rango indicado.
            luz = int(input("Por favor ingrese el valor de la cantidad de luz en un rango de (1-10): "))
            if 1 <= luz <= 10:
                valid = True
            else:
                print("Valor ingresado no valido - por favor ingrese un valor entre 1 y 10")
        except ValueError:
            print("Valor ingresado no valido - por favor ingrese un valor entre 1 y 10")
    valid =  False
    while not valid:
        # adicionamos una excepcion para manipular la iteracion de la funcion en la variable agua.
        try:
            agua = int(input("Por favor ingrese un valor de la candidad de agua en un rango de (1-10): "))
            if 1 <= agua <= 10:
                valid = True
            else:
                print("Valor ingresado no valido - por favor ingrese un valor entre 1 y 10")
        except ValueError:
            print("Valor ingresado no valido - por favor ingrese un valor entre 1 y 10")
    # Crecimiento del cultivo: adicionamos el codigo para preguntarle al usuario por el valor de agua
    cultivo.crecer(luz, agua)

# Adicionamos una nueva funcion llamada mostrar_menu()

def mostrar_menu():
    print("1. Crecimiento manual para un dia")
    print("2. Crecimiento automatico por 30 dias")
    print("3. Reportar el status")
    print("0. Salir de la evaluacion del programa")
    print()
    print("Por favor selecciona una opcion del menu anterior")

# Para que se nos muestren las opciones del menu adicionamos una nueva funcion llamada obt_opciones_menu ()

def obt_opciones_menu():
    opcion_valid = False
    while not opcion_valid:
        try:
            opcion = int(input("Opcion seleccionada"))
            if 0 <= opcion <= 4:
                opcion_valid = True
            else:
                print("Por favor ingresa una opcion valida")
        except ValueError:
            print("Por favor ingresa una opcion valida")
    return opcion

# Finalente necesitamos una funcion para manipular de funcion anterior

def man_cultivo(cultivo):
    print("Este es el programa para controlar el cultivo")
    print()
    sin_salida = True
    while sin_salida:
        mostrar_menu()
        opcion = obt_opciones_menu()
        print()
        if opcion == 1:
            manual_crecer(cultivo)
            print()
        elif opcion == 2:
            auto_crecer(cultivo,30)
            print()
        elif opcion == 3:
            print(cultivo.reporte())
            print()
        elif opcion == 0:
            sin_salida = False
            print()
    print("Gracias por usar el programa Control del cultivo")


def main():
    #Instanciamos la clase
    nuevo_cultivo = Cultivo(1, 4, 3)
    man_cultivo(nuevo_cultivo)


if __name__ == "__main__":
    main()

###################################################

# Pero más allá de tener solo un cultivo generico la pregunta aqui seria: ¿No seria mejor si nosotros pudieramos tener un tipo particular de Cultivo?
# ¿Como Trigo o Papas?

# HERENCIA Y POLIMORFISMO

# ¿Que podriamos hacer?
# Podemos crear-escribir nuevas clases para cada uno de estos cultivo en especial ¿NO?, sin embargo eso nos haria
# desperdiciar nuestro trabajo que generamos de un cultivo generico, en especial considerando que todos los cultivo
# tienen cuertas caractericticas y comportamientos en comun.

# HERENCIA: provee un mecanismo que permite contruir sobre nuetro trabajo existente, asegurando que todos los cultivos
# compartan aquellas caracteristica y comportamientos que tiene en comun. La Relacion entre las clases que se benefician
# por la herencia es similar a la existente entre padres e hijos.
# Es decir una clase hijo que hereda la funcionalidad de una clase padre tendra todos los mimso atribustos y metodos como
# la clase padre. Esto quiere decir que si nosotros queremos cambiar estos atributos o metodos, nosotros podemos hacerlo
# en la clase padre y que los cambios staran inmediatamente disponivles en todas las clases hijas. Esto es un gran beneficio comparado
# a escribir cada clase de forma separada.

#  Ademas, la clase hija puede extender la funcionalidad de la clase padre mediante la adicion de atributos y metodos
# que son unicos de la clase hija.

# POLIMORFISMO
# En una calse hijo, nosotros podemos cambiar como algunos metodos funcionan, mientras que podemos mantener el mismo nombre
# Esto es lo que se conoce como polimorfismo o predominancia (overriding) y es util por que nosotors no queremos seguir introduciendo
# nuevos nombres de metodos para la funcionalidad que es muy similar en cada clase. Consideremos a nuestra clase "Cultivo",
# la cual tiene el metodo crecer(). El pseudo codigo para su actual funcionalidad es:

# La clase niño denominada "Trigo" también necesitaría crecer dependiendo ddel aporte de la luz y del agua
# pero quizás desearemos cambiar algunos paramtros de esta nueva clase en relacion a cómo crecera.
# Con el objetivo de simular de forma mas precisa cómo el Trigo crece en el mundo real.

# Primero: creamos un nuevo modulo llamado clase_papas()
# Para tener acceso a la clase cultivo, debemos mandarla llamar, entonces importamos la clase cultivo() en la parte inicial del nuevo modulo.

from clase_cultivo import *

# Configuramos la estructura de la clase Papas.
class Papas(Cultivo):
    """ Un cultivo de papas """
    
    # Adicionamos el metodo contructor __init__()
    # Constructor
    def __init__(self):
        # generamos una superclase contructor
        # Llammar a la clase contructora padre con los valores por defecto para nuestra clase Papa.
        # La tasa de crecmimiento = 1; luz necesaria = 3; agua necesaria = 6.
        super().__init__(1,3,6)
        self._tipo = "Papas"
    
    # Predominancia del metodo crecimiento() para darle una funcionalidad diferente.
    # Predominancia del metodo crecimiento para la subclase
    def crecimiento(self, luz, agua):
        if luz >= self._luz_necesaria and agua >= self._agua_necesaria
            if self.status == "Plantula" and agua > self._agua_necesaria:
                self._crecer += self._tasa_crecer * 1.5
            elif self._status == "Joven" y agua > self._agua_necesaria:
                self._crecer += self._tasa_crecer * 1.5
            else:
                self._crecer += self._tasa_Crecer
        # Incremento de crecimiento por dia
        self._dias_creciendo += 1
        # Status actualizado
        self._status_actual()


def main():
    # Crear un nuveo cultivo de papas
    cultivo_papas = Papas()
    print(cultivo_papas.reporte())
    # Hacer crecer el cultivo manualmente
    manual_manual(cultivo_papas)
    print(cultivo_papas.reporte())


if __name__ == "__main__":
    main()
