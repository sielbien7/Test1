from imports import *
import csv

#funcion que elija archivo con la fecha mas reciente
#clase con atributos de cada tabla para legibilidad

#Variables
header_list = [
        'cod_localidad', 'id_provincia', 'id_departamento',
        'categoria', 'provincia', 'localidad', 'nombre', 'domicilio',
        'codigo postal', 'numero de telefono', 'mail', 'web'
    ]
#Clases

#Funciones
def get_latest_month (categoria):
    """obtiene mes mas reciente de la carpeta"""
    path = "M:/Documents/2022/pythonProjects/ProyectoCool/Data/"+categoria
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
    ruta='M:/Documents/2022/pythonProjects/ProyectoCool/datanormalizada/tabla-normalizada.csv'

    with open('M:/Documents/2022/pythonProjects/ProyectoCool/datanormalizada/tabla-normalizada.csv','w') as tabla_normalizada:
        dw=csv.DictWriter(tabla_normalizada,delimiter=',',fieldnames=header_list)
        dw.writeheader()



