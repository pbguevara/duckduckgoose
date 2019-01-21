import sys

def juego(array, numero):
    if numero <= len(array):
        jugador = array[numero+1]
        return jugador
    else:
        return "No hay tantos jugadores"

#lista = ["Paola", "Sofia", "Mounat", "Blanca", "Laura"]
lista = []
condition = True
while condition:
    jugador = input("Añada un jugador: ")
    if jugador != "0":
        lista.append(jugador)
    else:
        condition = False
numero = int(input("Introduzca el número: "))
resultado = juego(lista, numero)
print("La oca es: ", resultado)
