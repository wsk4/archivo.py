import os 
import csv

orden=[]
autos=['ford','toyota','chevrolet']

encabezado=f''' registro de vehiculos
{"-"*120}
{"marca":<15}{"año de fabricacion|":<20}{"kilometraje|":<15}{"costo de reparacion estimado|":<30}{"impuesto  de servicio|":<25}{"costo total|":<20}
{"-"*120}
'''

menu="""
1.registrar vehiculo
2.listar vehiculos
3.imprimir orden de reparacion
4.salir
"""

def registrar_vehiculo():
    while True:
        try:
            marca=input("marca del vehiculo: ").strip().lower()
            año=int(input("año de fabricacion: "))
            kilometraje=int(input("kilometra del auto: "))
            costo=int(input("costo estimado: "))
            if marca in autos and año>0 and kilometraje>0 and costo>0:
                servicio=costo*0.08
                total=costo+servicio
                orden.append([marca,año, kilometraje,costo,servicio,total])
                break
        except Exception as e:
            input(f"excepcion menu principal en: {str(e)}")

def listar_vehiculo():
    salida=encabezado
    for i in orden:
        salida+=f'{i[0]:<15}'
        salida+=f'{i[1]:<20}'
        salida+=f'{i[2]:<15}'
        salida+=f'{i[3]:<30}'
        salida+=f'{i[4]:<25}'
        salida+=f'{i[5]:<20}'
        salida+="\n"
    return(salida)

def listarXmarca(marca):
    salida=encabezado
    for i in orden:
        if marca==i[0]:
            salida+=f'{i[0]:<15}'
            salida+=f'{i[1]:<20}'
            salida+=f'{i[2]:<15}'
            salida+=f'{i[3]:<30}'
            salida+=f'{i[4]:<25}'
            salida+=f'{i[5]:<20}'
            salida+="\n"
        else:
            print("la marca no se encuentra registrada, reingrese...")
    return(salida)

def imprimir():
    marca=input(f"marca a filtar ['todos',{autos}]: ").strip().lower()
    if marca=="todos":
        with open("listado.txt", "w") as archivo:
            archivo.write(listar_vehiculo())
    elif marca in autos:
        with open(marca+".txt", "w") as archivo:
            archivo.write(listarXmarca(marca))
    else:
        input("cargo mal ingresado, revise...")
    
def imprimircsv():
        marca=input(f"pedido a filtrar [{autos}] para imprimir: ")
        if marca in autos:
            with open (f"{marca}.csv","w",encoding='utf-8', newline='') as archivo:
                docu=csv.writer(archivo)
                docu.writerow([encabezado])
                docu.writerows([orden])

while True:
    try:
        opc=input(menu)
        if opc=='4':
            break
        elif opc=='1':
            registrar_vehiculo()
        elif opc=='2':
            input(listar_vehiculo())
        elif opc=='3':
            imprimir()
    except Exception as e:
        input(f"excepcion en:  {str(e)}")