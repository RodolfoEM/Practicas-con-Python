"""Codigo que busca hacer una lista con los primeros 100 números naturales 
elevados al cuadrado y que no sean divisibles entre 3. La opcion 1 es
separando el código(vease el codigo comentado) y la opción 2 es usando
list comprehension(ejecutando el codigo dentro de la lista)"""

def run():
    #squares = [] 
    ## squares es el nombre denuestra lista vacía
    #for i in range(1,101):
    #    if i % 3 != 0:
    #        squares.append(i**2)
    #    # append agrega un elemento de cualquier tipo al final de una lista.

    squares = [i**2 for i in range(1,101) if i % 3 !=0]
    print(squares)


if __name__ == '__main__':
    run()