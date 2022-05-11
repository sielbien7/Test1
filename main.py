import datetime
from datetime import date

def getArchivo (urlArchivo):
    r=requests.get(urlArchivo)
        fileName= "cacaPath"
         with open(fileName, 'wb') as f:
             f.write(r.content)
              print("Archivo guardado")


x = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'
print()

