import requests
import sys
import os
import datetime
from pathlib import Path
from datetime import date
import glob
import csv
import pandas as pd
from obtenciondearchivos import *


#Variables
header_list = [
        'cod_localidad', 'id_provincia', 'id_departamento',
        'categoria', 'provincia', 'localidad', 'nombre', 'domicilio',
        'codigo postal', 'numero de telefono', 'mail', 'web'
    ]
header_viejo_museos=[ #header original del archivo museos
    'Cod_Loc','IdProvincia','IdDepartamento','subcategoria',
    'provincia','localidad','nombre','direccion',
    'CP','telefono','Mail','Web'
]
header_viejo_cines=[
#header original del archivo cines
'Cod_Loc','IdProvincia','IdDepartamento','Categoría',
    'Provincia','Localidad','Nombre','Dirección',
    'CP','Teléfono','Mail','Web'
]
header_viejo_bibliotecas=[
#header original del archivo bibliotecas
'Cod_Loc','IdProvincia','IdDepartamento','Categoría',
    'Provincia','Localidad','Nombre','Domicilio',
    'CP','Teléfono','Mail','Web'
]

#Funciones
def get_latest_month (categoria):
    """obtiene mes mas reciente de la carpeta"""
    path = "Data/"+categoria+"/"
    mes=''
    dir_list = os.listdir(path)
    all_folders = ''
    all_folders = all_folders.join(dir_list) #une nombres de carpetas en un solo string
    for i in range(len(dir_list)):
        for x in range(12, 0, -1):
            if (all_folders.rfind(meses.get(x))) != -1: #revisa que mes encuentra en la string, empezando por el mes 12.
                mes = meses.get(x)
                return mes;

def get_latest_file(categoria):
    """obtiene ruta del archivo mas reciente de la carpeta"""
    ruta='M:/Documents/2022/pythonProjects/ProyectoCool/Data/'+categoria+'/2022-'+get_latest_month(categoria) #crea ruta segun el ultimo mes que se encuentra
    tipo_archivo=r'/*csv'
    print(ruta)
    archivos=glob.glob(ruta+tipo_archivo)
    ultimo_archivo=max(archivos,key=os.path.getctime)
    return ultimo_archivo #devuelve ruta del archivo mas reciente de la carpeta con el mes mas reciente

def crear_tabla_normalizada():
    """funcion que crea la tabla que contendrá la información normalizada"""
    ruta='/datanormalizada/tabla-normalizada.csv'

    with open('datanormalizada/tabla-normalizada.csv','w') as tabla_normalizada:
        dw=csv.DictWriter(tabla_normalizada,delimiter=',',fieldnames=header_list)
        dw.writeheader()

def append_info_normalizada(ruta_ultimo_archivo,header):
    df = pd.read_csv(ruta_ultimo_archivo)
    # guarda valores de la tabla museos de las columnas que se encuentran en header_viejo_museos
    nuevas_columnas = df[header]
    # guarda los valores de las columnas seleccionadas en nueva tabla con headers correspondientes
    tabla_normalizada = nuevas_columnas.to_csv("datanormalizada/tabla-normalizada.csv", mode='a', header=False)




