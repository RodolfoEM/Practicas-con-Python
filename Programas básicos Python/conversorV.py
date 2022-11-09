def conversor(tipo_pesos, valor_dolar):
    peso = input("¿Cuántos pesos" + tipo_pesos + "tienes?: ")
    peso = float (peso)
    dolares = peso / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $"+ dolares + " dólares") 

menu = """
Bienvenido al conversor de moneda👍

1 - Pesos Colombianos
2 - Pesos Argentions
3 - Pesos Mexicnaos 

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3958.85)
elif opcion == 2:
    conversor("Argentinos", 115.75)
elif opcion == 3:
    conversor("Mexicanos", 20.4239)
else:
    print("Ingresa la opción correcta")

