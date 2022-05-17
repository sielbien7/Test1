import requests
import sys
import os
import datetime
from pathlib import Path
from datetime import date
import glob
import csv
import pandas as pd

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
class Fecha:
    """objetos fecha"""
    def __init__(self):
        self.dia = date.today().day
        self.mes = date.today().month
        self.mes_nombre = meses[date.today().month]
        self.anio = date.today().year

#Funciones que usa la funcion get_archivo
def get_date():
    """devuelve fecha de hoy"""
    hoy = Fecha()
    return hoy

def crear_ruta(ruta):
    """crea la ruta especificada"""
    try:
        os.makedirs(ruta)
        print("La ruta:", ruta, " fue creada correctamente ")
    except FileExistsError:#ignora error si exista la ruta
        pass

def get_categoria (url_archivo):
    """devuelve categoria de la url pasada"""
    categoria ='Vacio'
    nombres = ['museos', 'cine', 'biblioteca']
    nombres_formato = ['museos', 'salas-de-cine', 'bibliotecas-populares']
    for i in range(len(nombres)):
        if url_archivo.rfind(nombres[i]) != -1:
            categoria=nombres_formato[i]
    return categoria

#Funcion principal

def get_archivo (url_archivo):
    """guarda el archivo en la ruta correspondiente y conel nombre correspondiente"""
    r=requests.get(url_archivo)
    categoria=get_categoria(url_archivo)
    fecha=get_date()
    if categoria == 'Vacio':
        print('Categoria no encontrada, revisar URL')
    else:
        ruta='Data/'+categoria+'/'+str(fecha.anio)+'-'+fecha.mes_nombre
        file_name= 'Data/'+categoria+'/'+str(fecha.anio)+'-'+fecha.mes_nombre+'/'+categoria+'-'+str(fecha.dia)+'-'+str(fecha.mes)+'-'+str(fecha.anio)+'.csv'
        crear_ruta(ruta)

        if r.status_code == 404:
            print("Error 404, URL Invalida")
        else:
            with open(file_name, 'wb') as f:
                f.write(r.content)
            print("Archivo guardado")




