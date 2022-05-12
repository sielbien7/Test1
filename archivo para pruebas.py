import datetime
from datetime import date

#def getArchivo (urlArchivo):
    #r=requests.get(urlArchivo)
       # fileName= "cacaPath"
        # with open(fileName, 'wb') as f:
          #   f.write(r.content)
        #      print("Archivo guardado")


#x = 'https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv'


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


class fecha:
    def __init__(self):
        self.dia= date.today().day
        self.mes= date.today().month
        self.mesNombre=meses[date.today().month]
        self.anio=date.today().year


def getDate():
   hoy=fecha()
   return hoy



hoyTest=getDate()

print(hoyTest.mesNombre)

