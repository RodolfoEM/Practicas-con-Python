peso = input("¿Cuántos pesos(MXN) tienes?: ")
peso = float (peso)
valor_dolar = 20.4239
dolares = peso / valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print("Tienes $"+ dolares + " dólares")


dolar = input("¿Cuántos dolares(USD) tienes?: ")
dolar = float (dolar)
valor_peso = 20.4239
peso = dolar * valor_peso
peso = round(peso,2)
peso = str(peso)
print("Tienes $"+ peso + " pesos")