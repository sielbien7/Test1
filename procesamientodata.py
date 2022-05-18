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
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    13: "",
    14: "",
    15: "",
    16: "",
    17: "",
    18: "",
    19: ""
    20: "",
    21: "",
    22: "",
    23: "",
    24: "",


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
        df
        df.to_csv("dataprocesada/info-cines-procesada.csv",mode='a', header=True,index=False)


def llenartabla_cines():

