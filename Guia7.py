"""Ejercicio 4. Usando las funciones de python min y max resolver:
En una plantacion de pinos, de cada arbol se conoce la altura expresada en metros. 
El peso de un pino se puede estimar
a partir de la altura de la siguiente manera:
3 kg por cada centımetro hasta 3 metros,
2 kg por cada centımetro arriba de los 3 metros.
Por ejemplo:
2 metros pesan 600 kg, porque 200 * 3 = 600
5 metros pesan 1300 kg, porque los primeros 3 metros pesan 900 kg y los 
siguientes 2 pesan los 400 restantes.
Los pinos se usan para llevarlos a una fabrica de muebles, a la que le sirven 
arboles de entre 400 y 1000 kilos, un pino
fuera de este rango no le sirve a la fabrica.
Definir las siguientes funciones, deducir que parametros tendran a partir 
del enunciado. Se pueden usar funciones auxiliares
si fuese necesario para aumentar la legibilidad."""
# 1. Definir la funcion peso pino
def peso_pino(altura: float) -> int:
    peso = 0
    if altura <= 3:
        peso = altura*100*3
    else:
        peso = 900
        peso += (altura-3)*100*2
    return peso

# 2. Definir la funcion es peso util, recibe un peso en kg y responde si un pino 
# de ese peso le sirve a la fabrica.
def peso_util(peso: int) -> bool:
    if peso <= 1000 and peso >= 400:
        return True
    else:
        return False
    
# 3. Definir la funcion sirve pino, recibe la altura de un pino y responde si un 
# pino de ese peso le sirve a la fabrica.
# 4. Definir sirve pino usando composicion de funciones.
def sirve_pino(altura: float) -> bool:
    return peso_util(peso_pino(altura))


"""Ejercicio 5. Implementar los siguientes problemas de alternativa condicional (if). 
Intenta especificarlos alguno de ellos (todos los que te salgan) 
en lenguaje semiformal y formal sin utilizar IfThenElseFi."""
# 1. devolver el doble si es par(un numero). Debe devolver el mismo numero en caso 
#de no ser par.
def devolver_el_doble_si_es_par(numero: int) -> int:
    if numero % 2 == 0:
        return numero*2
    else:
        return numero
    
# 2. devolver valor si es par sino el que sigue(un numero). Analizar distintas formas 
# de implementacion (usando un if-then-else, y 2 if), ¿todas funcionan?
def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    if numero % 2 == 0:
        return numero
    else:
        return numero+1
    
# 3. devolver el doble si es multiplo3 el triple si es multiplo9(un numero). En otro 
# caso devolver el numero original. Analizar distintas formas de implementacion 
# (usando un if-then-else, y 2 if, usando alguna opcion de operacion
# logica), ¿todas funcionan?.
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_mutliplo9(numero: int) -> int:
    if numero % 9 == 0:
        return numero*2
    if numero % 3 == 0:
        return numero*2
    
# 4. Dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga 
# “Tu nombre tiene muchas letras!” y # sino, “Tu nombre tiene menos de 5 caracteres”.
def tiene_muchas_letras(nombre: str) -> str:
    if len(nombre) >= 5:
        return "Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres"
    
# 5. En Argentina una persona del sexo femenino se jubila a los 60 a˜nos, mientras que 
# aquellas del sexo masculino se jubilan
# a los 65 a˜nos. Quienes son menores de 18 años se deben ir de vacaciones junto al 
# grupo que se jubila. Al resto de
# las personas se les ordena ir a trabajar. Implemente una funcion que, dados los 
# parametros de sexo (F o M) y edad,
# imprima la frase que corresponda segun el caso: “Anda de vacaciones” o “Te toca 
# trabajar”"""
def vacaciones_o_trabajar(sexo: str, edad: int) -> str:
    if (edad < 18) or (edad >= 60 and sexo == "F") or (edad >= 65 and sexo == "M"):
        return "Anda de vacaciones"
    else:
        return "Te toca trabajar"
    
# Ejercicio 6. Implementar las siguientes funciones usando repeticion condicional while:
# 1. Escribir una funcion que imprima los numeros del 1 al 10.
def numeros_1_al_10():
    numero = 1
    while numero <= 10:
        print(numero)
        numero += 1
        
# 2. Escribir una funcion que imprima los numeros pares entre el 10 y el 40.
def numeros_1_al_40():
    numero = 1
    while numero <= 40:
        print(numero)
        numero += 1
    
# 3. Escribir una funcion que imprima la palabra “eco” 10 veces.
def eco_10():
    numero = 1
    while numero <= 10:
        print("eco")
        numero += 1
        
# 4. Escribir una funcion de cuenta regresiva para lanzar un cohete. Dicha
# funcion ira imprimiendo desde el numero que
# me pasan por parametro (que sera positivo) hasta el 1, y por ultimo “Despegue”.
def cuenta_regresiva(numero: int):
    while numero >= 1:
        print(numero)
        numero -= 1
    print("Despegue")
    
# 5. Hacer una funcion que monitoree un viaje en el tiempo. Dicha funcion recibe 
# dos parametros, “el a˜no de partida” y
# “algun a˜no de llegada”, siendo este ultimo parametro siempre mas chico que 
# el primero. El viaje se realizara de a saltos
# de un a˜no y la funcion debe mostrar el texto: “Viajo un a˜no al pasado, 
# estamos en el ano: <ano>” cada vez que se realice un salto de a˜no.
def viaje_en_el_tiempo(partida: int, llegada: int):
    while partida >= llegada:
        print("Estamos en el año: " + str(partida))
        partida -= 1
        
# 6. Implementar de nuevo la funcion de monitoreo de viaje en el tiempo, 
# pero desde el a˜no de partida hasta lo mas cercano
# al 384 a.C., donde conoceremos a Aristoteles. Y para que sea mas rapido el viaje, 
# ¡vamos a viajar de a 20 a˜nos en cada salto
def viaje_a_aristoteles(partida: int):
    while partida > (-374):
        partida -=20
        if partida >= 0:
            print("Estamos en el año: " + str(partida))
        else:
            print("Estamos en el año: " + str(-partida) + " a.C.")
            
# Ejercicio 7. Implementar las funciones del ejercicio 6 utilizando for num in range(i,f,p):. Recordar que la funcion
# range para generar una secuencia de numeros en un rango dado, con un valor inicial i, un valor final f y un paso p. Ver
# documentacion: https://docs.python.org/es/3/library/stdtypes.html#typesseq-range


# Ejercicio 8. Realizar la ejecucion simbolica de los siguientes codigos:
# 1. x=5 ; y=7
"""x@1 = 5;
    x@2 = 5, y@2 = 7"""
# 2. x=5 ; y=7 ; z=x+y
""" x@1 = 5
    x@2 = 5, y@2 = 7
    x@3 = 5, y@3 = 7, z@3 = 12"""
# 3. x=5 ; x=‘‘hora’’
# 4. x=True ; y=False ; res=x and y
# 5. x=False ; res=not(x)

# Ejercicio 9. Sea el siguiente codigo:
def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g
#1. ¿Cual es el resultado de evaluar tres veces seguidas ro(1)?
# g = 1; g = 2; g = 3 && x+g = 4
#2. ¿Cual es el resultado de evaluar tres veces seguidas rt(1, 0)?
# x+g = 2, no almacena valores externos
#3. En cada funcion, realizar la ejecucion simbolica.
# 4. Dar la especificacion en lenguaje natural para cada funcion, rt y ro|