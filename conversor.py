def conversor(tipoPesos, valorDolar):
    pesos = float(input("Cuantos pesos " + tipoPesos + " tienes?: "))
    dolares = pesos / valorDolar 
    dolares = round(dolares, 2)
    print("Tienes $" + str(dolares) + " dolares")


menu = """
Bienvenido al conversor de monedas 🥰

1 - pesos colombianos
2 - pesos argentinos
3 - pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 4541.61)
elif opcion == 2:
    conversor("argentinos", 146.29)
elif opcion == 3:
    conversor("mexicanos", 20.34)
else:
    print("Ingrese una opcion valida!!!")

