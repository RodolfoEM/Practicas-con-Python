"""Programa en el que guardemos en un diccionario los números del 1
al 100 elevados al cubo, que no sean multiplos de 3. en la llave 
se debe colocar el número que se está elevando al cubo."""

def run():
    #my_dict = {}

    #for i in range(1, 101):
    #    if i % 3 !=0:
    #        my_dict[i] = i**3

    my_dict = {i: i**3 for i in range(1,101) if i % 3 !=0}

    print(my_dict)



if __name__ == '__main__':
    run()
