#Testooo
import requests
import sys
import os
import datetime
from pathlib import Path
from datetime import date

def getDate():
    hoy= date.today()
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
    fecha = [str(hoy.day),meses[hoy.month],str(hoy.year)]
    return fecha

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
        fileName= 'M:/Documents/2022/pythonProjects/ProyectoCool'+categoria+'/'+fecha[2]+'-'+fecha[1]+'/'+categoria+'-'+fecha[0]+'-'+fecha[1]+'-'+fecha[2]+'.csv'
        fileNameFormato= Path(fileName)

        if r.status_code == 404:
            print("Error 404, URL Invalida")
        else:
            with open(fileNameFormato, 'wb') as f:
                f.write(r.content)
            print("Archivo guardado")


x='https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'

getArchivo(x)



