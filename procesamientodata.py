import requests
import sys
import os
import datetime
from pathlib import Path
from datetime import date
import glob
import csv
import pandas as pd
from obtenciondearchivos import  *

provincias ={
    2: "Ciudad Autónoma de Buenos Aires",
    6: "Buenos Aires",
    10: "Catamarca",
    14: "Córdoba",
    18: "Corrientes",
    22: "Chaco",
    26: "Chubut",
    30: "Entre Ríos",
    34: "Formosa",
    38: "Jujuy",
    42: "La Pampa",
    46: "La Rioja",
    50: "Mendoza",
    54: "Misiones",
    58: "Neuquén",
    62: "Río Negro",
    66: "Salta",
    70: "San Juan",
    74: "San Luis",
    78: "Santa Cruz",
    82: "Santa Fe",
    86: "Santiago del Estero",
    90: "Tucumán",
    94: "Tierra del Fuego, Antártida e Islas del Atlántico Sur",



}
header_cine_procesado= [
    #header para tabla con informacion procesada de los cines
    'provincia','cantidad de pantallas','cantidad de butacas','cantidad de espacios INCAA'
]
def creartabla_procesamiento_cines ():
    """funcion que crea la tabla con headers para almacenar la informacion procesada de cines"""
    crear_ruta('dataprocesada')
    with open("dataprocesada/info-cines-procesada.csv","w"):
        df=pd.DataFrame(columns=header_cine_procesado)
        #df
        df.provincia=provincias.values()
        df.to_csv("dataprocesada/info-cines-procesada.csv",mode='a', header=True,index=False)




























