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
from normalizarinfo import *



header_cantidad_registros=[
]
#def crear_tabla_cantidad_registros():
    #with open('Data/dataprocesada/cantidad_de_registros.csv','w') as file:
     #   pass
    #cant_registros=pd.to_csv(header=)

#def get_registros(header,ultimo_archivo):

urlmuseos="https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv"
urlcines="https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv"
urlbiblio="https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv"

get_archivo(urlmuseos)
get_archivo(urlcines)
get_archivo(urlbiblio)

crear_tabla_normalizada()

append_info_normalizada(get_latest_file("museos"),header_viejo_museos)
#append_info_normalizada(get_latest_file("salas-de-cine"),header_viejo_cines)
#append_info_normalizada(get_latest_file("bibliotecas-populares"),header_viejo_bibliotecas)










