menu = """
Bienvenido al conversor de moneda

1 - Pesos Colombianos
2 - Pesos Argentions
3 - Pesos Mexicnaos 

Elige una opción: """

opcion = input(menu)

if opcion == 1:
    peso = input("¿Cuántos pesos Colombianos tienes?: ")
    peso = float (peso)
    valor_dolar = 3958.85
    dolares = peso / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $"+ dolares + " dólares") 
elif opcion == 2:
    peso = input("¿Cuántos pesos Argentinos tienes?: ")
    peso = float (peso)
    valor_dolar = 115.75
    dolares = peso / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $"+ dolares + " dólares")
elif opcion ==3:
    peso = input("¿Cuántos pesos(MXN) tienes?: ")
    peso = float (peso)
    valor_dolar = 20.4239
    dolares = peso / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $"+ dolares + " dólares")
else:
    print("Ingresa la opción correcta")

