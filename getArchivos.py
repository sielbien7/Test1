#Testooo
import requests
import sys
import os
import datetime
from pathlib import Path
from datetime import date

#Variables
meses= {
        1:"enero",
        2:"febrero",
        3:"marzo",
        4:"abril",
        5:"mayo",
        6:"junio",
        7:"julio",
        8:"agosto",
        9:"septiembre",
        10:"octubre",
        11:"noviembre",
        12:"diciembre"
    }
#Clases
class fecha:
    def __init__(self):
        self.dia = date.today().day
        self.mes = date.today().month
        self.mesNombre = meses[date.today().month]
        self.anio = date.today().year

#Funciones
def getDate():
    hoy = fecha()
    return hoy

def crearRuta(ruta):
    try:
        os.makedirs(ruta)
        print("La ruta:", ruta, " fue creada correctamente ")
    except FileExistsError:
        pass

def getCategoria (urlArchivo):
    categoria ='Vacio'
    nombres = ['museos', 'salas-de-cine', 'bibliotecas-populares']
    for i in range(len(nombres)):
        if urlArchivo.rfind(nombres[i]) != -1:
            categoria=nombres[i]
    return categoria

def getArchivo (urlArchivo):
    r=requests.get(urlArchivo)
    categoria=getCategoria(urlArchivo)
    fecha=getDate()
    if categoria == 'Vacio':
        print('Categoria no encontrada, revisar URL')
    else:
        ruta='M:/Documents/2022/pythonProjects/ProyectoCool/Data/'+categoria+'/'+str(fecha.anio)+'-'+fecha.mesNombre
        fileName= 'M:/Documents/2022/pythonProjects/ProyectoCool/Data/'+categoria+'/'+str(fecha.anio)+'-'+fecha.mesNombre+'/'+categoria+'-'+str(fecha.dia)+'-'+str(fecha.mes)+'-'+str(fecha.anio)+'.csv'
        crearRuta(ruta)

        if r.status_code == 404:
            print("Error 404, URL Invalida")
        else:
            with open(fileName, 'wb') as f:
                f.write(r.content)
            print("Archivo guardado")


x='https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'

getArchivo(x)



