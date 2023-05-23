
from typing import Any
"""1. Primera Parte
Ejercicio 1. Codificar en Python las siguientes funciones sobre secuencias:
1. problema pertenece (in s:seq<Z>, in e: Z) : Bool {
requiere: { True }
asegura: { res = true ↔ (∃i : Z)(0 ≤ i < |s| → s[i] = e)}
}
¿Si la especificaramos e implementaramos con tipos gen´ericos, se podr´ıa usar esta misma funci´on para buscar un
caracter dentro de un string?"""
def pertenece (s: list, n: Any) -> bool:
    for i in s:
        if i == n:
            return True
    return False

"""2. problema divideATodos (in s:seq<Z>, in e: Z) : Bool {
requiere: {e 6= 0 }
asegura: { res = true ↔ (∀i : Z)(0 ≤ i < |s| → s[i] mod e = 0)}
}"""
def divideATodos (s: list, e:int) -> bool:
    for i in s:
        if i % e != 0:
            return False
    return True

"""3. problema sumaTotal (in s:seq<Z>) : Z {
requiere: { True }
asegura: { res es la suma de todos los elementos de s}
}
Nota: no utilizar la funci´on sum() nativa"""
def sumaTotal (s:list) -> int:
    suma = 0
    for i in s:
        suma +=i
    return suma

"""4. problema ordenados (in s:seq<Z>) : Bool {
requiere: { True }
asegura: { res = true ↔ (∀i : Z)(0 ≤ i < (|s| − 1) → s[i] < s[i + 1]}
}
"""
def esta_ordenado (s:list) -> bool:
    if len(s) <= 1: return True
    for i in range(len(s)-1):
        if s[i] >= s[i+1]:
            return False
    return True

#5. Dada una lista de palabras, devolver verdadero si alguna palabra tiene longitud mayor a 7
def longMayor7 (s:list) -> bool:
    for i in s:
        if len(i) > 7:
            return True
    return

#6. Dada una cadena de texto (string), devolver verdadero si ´esta es pal´ındroma
# (se lee igual en ambos sentidos), falso en caso contrario
def esPalindromo (texto: str) -> bool:
    for i in range(int(len(texto)/2)):
        if texto[i] != texto[len(texto)-1-i]:
            return False
    return True

"""7. Analizar la fortaleza de una contrase˜na. El par´ametro de entrada ser´a un string con la contrase˜na a analizar, y la salida
otro string con tres posibles valores: VERDE, AMARILLA y ROJA. Nota: en python la “˜n/N” es considerado un ˜
caracter especial y no se comporta como cualquier otra letra.
La contrase˜na ser´a VERDE si:
a) la longitud es mayor a 8 caracteres
b) Tiene al menos 1 letra min´uscula (probar qu´e hace ‘‘a’’<=‘‘A’’<=‘‘z’’)
c) Tiene al menos 1 letra may´uscula Tiene al menos 1 letra min´uscula (probar qu´e hace ‘‘A’’<=‘‘A’’<=‘‘Z’’
)
d) Tiene al menos 1 d´ıgito num´erico (0..9)
1
La contrase˜na ser´a roja si:
a) la longitud es menor a 5 caracteres.
En caso contrario ser´a AMARILLA."""
def fortalezaContraseña (contraseña: str) -> str:
    mayuscula = False
    minuscula = False
    digitos = False
    longitud = 0
    for letra in "abcdefghijklmnopqrstuvwxyz":
        if letra in contraseña:
            minuscula = True
        if letra.upper() in contraseña:
            mayuscula = True
    for numero in "0123456789":
        if numero in contraseña:
            digitos = True
    if mayuscula and minuscula and digitos and len(contraseña) > 8:
        return "VERDE"
    elif len(contraseña) < 5:
        return "ROJA"
    else:
        return "AMARILLO"
    
"""8. Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual.
Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso de
dinero y “R” para retiro de dinero, y adem´as el monto de cada operaci´on. Por ejemplo [(‘‘I’’, 2000), (‘‘R’’,
20),(‘‘R’’, 1000),(‘‘I’’, 300)] -> saldo = 1280."""
def saldoActual(historial: list) -> int:
    saldo = 0
    for movimiento in historial:
        if movimiento[0] == "I":
            saldo += movimiento[1]
        else:
            saldo -= movimiento[1]
    return saldo

# 9. Recorrer una palabra y devolver True si ´esta tiene al menos 3 vocales distintas. En caso contrario devolver False
def vocalesDistintas(palabra: str) -> bool:
    vocales = ["a","e","i","o","u"]
    cantidad = 0
    for letra in palabra:
        if letra.lower() in vocales:
            vocales.remove(letra.lower())
            cantidad += 1
    return cantidad >= 3