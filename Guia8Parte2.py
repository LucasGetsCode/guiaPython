# 2. Segunda Parte
# Ejercicio 2. Implementar las siguientes funciones sobre secuencias pasadas por par ́ametro:
import random
from Guia8Parte1 import *
lista_ejemplo = [1,2,3,4,5,61,1,1,]
texto_ejemplo = "Hola Don José, hola Don Pepito."
# 1. Implementar una funci ́on que dada una lista de n ́umeros, en las posiciones pares borra el valor original y coloca un
# cero. Esta funci ́on modifica el par ́ametro ingresado. Nota: La lista ser ́a un tipo inout
def ceros_por_pares(numeros: list([int])) -> list([int]):
    i = 0
    while i < len(numeros):
        if i % 2 == 0:
            numeros[i] = 0
        i += 1
    return numeros

# 2. Implementar la funci ́on del punto anterior pero esta vez sin modificar la lista original, devolviendo una nueva lista,
# igual a la anterior pero con las posiciones pares en cero. Nota: La lista ser ́a de tipo in
def ceros_por_pares_in(numeros_in: list([int])) -> list([int]):
    i = 0
    numeros_out = numeros_in.copy()
    while i < len(numeros_out):
        if i % 2 == 0:
            numeros_out[i] = 0
        i += 1
    return numeros_out

# print("Original:", lista_ejemplo)
# ceros_por_pares_in(lista_ejemplo)
# print("Luego del in:", lista_ejemplo)
# ceros_por_pares(lista_ejemplo)
# print("Luego del inout:", lista_ejemplo)

# 3. Implementar una funci ́on que dada una cadena de texto de entrada (in) devuelva una cadena igual a la anterior, pero
# sin las vocales. Nota: No agrega espacios, sino que borra la vocal y concatena a continuaci ́on
def sacar_vocales(texto: str) -> str:
    texto_nuevo = ""
    for letra in texto:
        if not letra in "aeiouAEIOUàèìòùáéíóúÁÉÍÓÚÀÈÌÒÙ":
            texto_nuevo = texto_nuevo + letra
    return texto_nuevo

# print(sacar_vocales(texto_ejemplo))
# print(texto_ejemplo)

# 4. problema reemplazaVocales (in s:seq<Char>) : seq<Char> {
#   requiere: { True }
#   asegura: { (∀i : Z)(0 ≤ i < |res| → (pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = ‘ ’) ∨
#       (¬ pertenece(<‘a’,‘e’,‘i’,‘o’,‘u’>, s[i]) ∧ res[i] = s[i] ) ) } }
def reemplaza_vocales(texto: str) -> str:
    texto_nuevo = ""
    for letra in texto:
        if not letra in "aeiouAEIOUàèìòùáéíóúÁÉÍÓÚÀÈÌÒÙ":
            texto_nuevo += letra
        else:
            texto_nuevo += "_"
    return texto_nuevo

# print(reemplaza_vocales(texto_ejemplo))
# print(texto_ejemplo)

# 5. problema daVueltaStr (in s:seq<Char>) : seq<Char> {
#   requiere: { True }
#   asegura: { (∀i : Z)(0 ≤ i < |res| → (res[i]=s[|s|-i-1]) }
# }
def da_vuelta_str(texto: str) -> str:
    texto_nuevo = ""
    i = len(texto) - 1
    while i >= 0:
        texto_nuevo += texto[i]
        i -= 1
    return texto_nuevo

# print(da_vuelta_str(texto_ejemplo))
# print(texto_ejemplo)

# Ejercicio 3. Vamos a elaborar programas interactivos (usando la funci ́on input()1) que nos permita solicitar al usuario
# informaci ́on cuando usamos las funciones.
# 1. Implementar una funci ́on para construir una lista con los nombres de mis estudiantes. La funci ́on solicitar ́a al usuario
# los nombres hasta que ingrese la palabra “listo”. Devuelve la lista con todos los nombres ingresados.
def lista_estudiantes() -> list([str]):
    lista_estudiantes = []
    estudiante = input("Nombre estudiante (ingrese 'listo' para terminar): ")
    while estudiante != "listo":
        lista_estudiantes.append(estudiante)
        estudiante = input("Nombre estudiante: ")
    return lista_estudiantes

# print(lista_estudiantes())

# 2. Implementar una funci ́on que devuelve una lista con el historial de un monedero electr ́onico (por ejemplo la SUBE).
# El usuario debe seleccionar en cada paso si quiere:
# “C” = Cargar cr ́editos,
# “D” = Descontar cr ́editos,
# “X” = Finalizar la simulaci ́on (terminar el programa).# 2
# En los casos de cargar y descontar cr ́editos, el programa debe adem ́as solicitar el monto para la operaci ́on. Vamos a
# asumir que el monedero comienza en cero. Para guardar la informaci ́on grabaremos en el historial tuplas que representen
# los casos de cargar (“C”, monto a cargar) y descontar cr ́edito (“D”, monto a descontar)
def monedero() -> list([(str, int)]):
    monto_total = 0
    historial_acciones = []
    accion = input("Acción a realizar (ingrese 'X' para terminar): ")
    while accion.capitalize() != "X":
        if accion in "Cc":
            monto = input("Monto a cargar: ")
            monto_total += int(monto)
        elif accion in "Dd":
            monto = input("Monto a descontar: ")
            monto_total -= int(monto)
        historial_acciones.append((accion, int(monto)))
        accion = input("Acción a realizar: ")
    historial_acciones.append(("X", monto_total))
    return historial_acciones

# print(monedero())

# 3. Vamos a escribir un programa para simular el juego conocido como 7 y medio. El mismo deber ́a generar un n ́umero
# aleatorio entre 0 y 12 (excluyendo el 8 y 9) y deber ́a luego preguntarle al usuario si desea seguir sacando otra “carta”
# o plantarse. En este  ́ultimo caso el programa debe terminar. Los n ́umeros aleatorios obtenidos deber ́an sumarse seg ́un
# el n ́umero obtenido salvo por las “figuras” (10,11 y 12) que sumar ́an medio punto cada una. El programa deber ́a
# ir acumulando los valores y si se pasa de 7.5 deber ́a informar que el usuario ha perdido. Al finalizar la funci ́on
# devuelve el historial de “cartas” que hizo que el mular el juego conocido como 7 y medio. El mismo deber ́a generar un n ́umero
# aleatorio entre 0 y 12 (excluyendo el 8 y 9) y deber ́a luego preguntarle al usuario si desea seguir sacando otra “carta”
# o plantarse. En este  ́ultimo caso el programa debe terminar. Los n ́umeros aleatorios obtenidos deber ́an sumarse seg ́un
# el n ́umero obtenido salvo por las “figuras” (10,11 y 12) que sumar ́an medio punto cada una. El programa deber ́a
# ir acumulando los valores y si se pasa de 7.5 deber ́a informar que el usuario ha perdido. Al finalizar la funci ́on
# devuelve el historial de “cartas” que hizo que el usuario gane o pierda. 
# Nota: Para esta funci ́on utilizaremos la funci ́on random.randint(1,12) para generar n ́umeros aleatorios entre 1 y 12. 
# Nota: La funci ́on random.choice() puede ser de gran ayuda a la hora de repartir cartas
def juego_7_y_medio() -> list([int]):
    def generar_numero() -> int:
        numero = random.randint(1,12)
        while numero in [8,9]:
            numero = random.randint(1,12)
        return numero
    
    def valor(n: int) -> int:
        if n >= 10:
            return 0.5
        else:
            return n

    cartas = []
    suma_total = 0
    accion = input("¿Quiere empezar? ")
    while accion.lower() not in ["no", "n", "nop", "mmm"] and suma_total <= 7.5:
        numero = generar_numero()
        suma_total += valor(numero)
        print("Carta: " + str(numero) + ". Suma: " + str(suma_total))
        cartas.append(numero)
        if suma_total <= 7.5:
            accion = input("¿Desea seguir sacando cartas? ")
    if suma_total <= 7.5:
        print("Has ganado.")
    else:
        print("Has perdido.")
    return cartas


# print(juego_7_y_medio())
# Ejercicio 4. Implementar las siguientes funciones sobre listas de listas:
# 1. problema perteneceACadaUno (in s:seq<seq<Z>>, in e:Z, out res: seq<Bool>) {
# requiere: { True }
# asegura: { (∀i : Z)(0 ≤ i < |res| → (res[i] = true ↔ pertenece(s[i],e)) ) }
# }
# Nota: Reutilizar la funci ́on pertenece() implementada previamente para listas

def pertenece_a_cada_uno(listas: list([list]), n: int) -> list([bool]):

    lista_bools = []
    for i in listas:
        if pertenece(n, i):
            lista_bools.append(True)
        else:
            lista_bools.append(False)
    return lista_bools

# print(pertenece_a_cada_uno([[1,2,3,4,5], [5,4,3,2,1], [3,4,5,6]], 2))

# 2. problema esMatriz (in s:seq<seq<Z>>) : Bool {
# requiere: { True }
# asegura: { res = true ↔ (|s| > 0) ∧ (|s[0]| > 0) ∧ (∀i : Z)(0 ≤ i < |s| → |s[i]| = |s[0]|)) } }
def es_matriz(matriz: list([list])) -> bool:
    if len(matriz) == 0: return False
    longitud_base = len(matriz[0])
    if longitud_base == 0: return False
    for linea in matriz:
        if len(linea) != longitud_base: return False
    return True

# print(es_matriz([[1,2,3], [4,5,6], [6,7,8]]))
# print(es_matriz([[1,2,3], [4,5,6], [6,7,8], [9, 10]]))

# 3. problema filasOrdenadas (in m:seq<seq<Z>>, out res: seq<Bool>) {
# requiere: { esMatriz(m)}
# asegura: { (∀i : Z)(0 ≤ i < |res| → (res[i] = true ↔ ordenados(s[i]) ) ) } }
# Nota: Reutilizar la funci ́on ordenados() implementada previamente para listas
def filas_ordenadas(filas: list([list])) -> list([bool]):

    lista_bools = []
    for fila in filas:
        if esta_ordenado(fila):
            lista_bools.append(True)
        else:
            lista_bools.append(False)
    return lista_bools
    
print(filas_ordenadas([[1,2,3,4], [4,5,6,7], [1], [1,2,3,1]]))
