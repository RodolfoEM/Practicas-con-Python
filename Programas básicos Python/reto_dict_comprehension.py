"""Crear, con un dictionary comprehension, un diccionario cuyas llaves 
sean los 1000 primeros números naturales con sus raíces cuadradas como valores"""
import math

def run():
    dictionary = {i:round((math.sqrt(i)),2) for i in range(1,1001)}

    print(dictionary)

if __name__ == '__main__':
    run()