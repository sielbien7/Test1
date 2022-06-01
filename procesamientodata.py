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


def procesar_datos_cines():
    """funcion que procesa la info de la tabla cines"""
    df_origen = pd.read_csv(get_latest_file("salas-de-cine"))
    df_destino = pd.read_csv('dataprocesada/info-cines-procesada.csv')
    df_temp = pd.DataFrame
    df_origen.sort_values(by=['IdProvincia'])
    idprov = 2
    pantallas = 0
    butacas = 0
    espacios_INCAA = 0
    index_append = 0
    while idprov <= 94:
        df_temp = df_origen.loc[df_origen.IdProvincia == idprov]
        df_temp = df_temp.astype({"espacio_INCAA": str})
        pantallas = 0
        butacas = 0
        espacios_INCAA = 0
        for index in df_temp.index:
            pantallas += df_temp['Pantallas'][index]
            butacas += df_temp['Butacas'][index]
            if (df_temp['espacio_INCAA'][index].lower()) == 'si':
                espacios_INCAA += 1

        df_destino.at[index_append, 'cantidad de pantallas'] = pantallas
        df_destino.at[index_append, 'cantidad de butacas'] = butacas
        df_destino.at[index_append, 'cantidad de espacios INCAA'] = espacios_INCAA
        index_append += 1
        idprov += 4

        df_destino.to_csv('dataprocesada/info-cines-procesada.csv', header=True, index=False



























