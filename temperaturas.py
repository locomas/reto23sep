# El valle del aburrra afronta altas temperaturas. Crea una funcion que permita calc la temp media de la tierra, a partir de recibir 20 datos diarios de temp

numeros = [1,5,1,2,5,2,6,3,6,3,2,6,3,4,6,7,3,4,3,2]
media=0
def calcularTemp(numeros):
    for numero in numeros:
        suma+=numero
        media=suma/20
        media=round(media,2)#redondeamos a 2 decimales
print('La temperatura media de la tierra es de '+str(media))

calcularTemp(numeros)