# program.py

sum = 1 + 2
print(sum)

#Impresion en pantalla
print('Hola desde console line')

# Sumar y multiplicar
product= sum * 2
print(product)

#tipos de datos
planetas_en_el_sistema_solar=8 #int
distancia_a_alfa_centauri=4.367 #Float
puede_despegar=True #Boolean
transbordador_que_aterrizo_en_la_luna="Apolo 11" #string

#Detectar tipo de datos de una variable
print(type(planetas_en_el_sistema_solar))
print(type(distancia_a_alfa_centauri))
type(puede_despegar)
type(transbordador_que_aterrizo_en_la_luna)

#Operadores 
# Arigmeticos: Suma (+) Resta(-) Division(/) Multiplicacion(*)

#Asignacion: =   +=    -=    /=    *=

#Fechas: se debe importar el modulo date para poder trabaar con fechas

from datetime import date

print("Today's date is : " + str(date.today()))

#Inputs: entrada del usuario
print("Bienvenido al programa")
name=input("Por Favor, Ingrese su nombre: ")
print("Saludos " + name + ". Buen Dia")

#Inputs: trabajando con numeros
print("Calculadora")
first_number=input("Primer numero: ")
second_number=input("Segundo numero: ")
print(int(first_number) + int(second_number))

#Finaliza sesion 1