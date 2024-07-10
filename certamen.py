import random
import csv

#Ejercicio Preparación Examen:
#Crea una lista con 10 marcas de automóviles
marcas=['toyota','bwm','chevrolet','kia','jack','ferrari','mercedes','maclaren','audi','subaru']
#Crea un lista vacía que almacenará los precios de los automóviles
precios=[]
#Crea una función que genere los 10 precios de forma aleatoria en un rango entre 10000 y 50000
#y agrégalos a la lista
def precios_aleatorios():
    for i in range(10):
        precios.append(random.randint(10000,50000))
#Crea una función que permita mostrar
#los vehículos y sus respectivos precios
def mostrar_vehiculo():
    for i in range(10):
        print(f'{marcas[i]} :{precios[i]}')

#Crea una función que permita mostrar:
#automóvil con precio más bajo
#automóvil con precio más alto
#promedio de precios
def estadisticas():
   minimo=min(precios)
   maximo=max(precios)
   index_min=precios.index(minimo)
   index_max=precios.index(maximo)
   print(f"auto con menor precio {marcas[index_min]} precio: {minimo}")
   print(f"auto con mayor precio {marcas[index_max]} precio: {maximo}")
   prom={sum(precios)/len(precios)}
   print(f"promedio de precios: {prom}")

def imprimir():
            with open (f"autos.csv","w",encoding='utf-8', newline='') as archivo:
                docu=csv.writer(archivo)
                docu.writerow([mostrar_vehiculo()])


#desde programa principal llama a las funciones y muestra los resultados por pantalla

input(precios_aleatorios())
input(mostrar_vehiculo())
input(estadisticas())
input(imprimir())





