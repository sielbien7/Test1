from imports import *
#M:/Documents/2022/pythonProjects/ProyectoCool/

#Cod_Loc,IdProvincia,IdDepartamento,Observaciones,categoria,subcategoria,provincia,localidad,nombre,
# direccion,piso,CP,cod_area,telefono,Mail,Web,Latitud,Longitud,TipoLatitudLongitud,Info_adicional,fuente,jurisdiccion,año_inauguracion,actualizacion



header_viejo_museos=[
    'Cod_Loc','IdProvincia','IdDepartamento','categoria',
    'provincia','localidad','nombre','direccion',
    'CP','telefono','Mail','Web'
]

museos= pd.read_csv("Data/museos/2022-mayo/museos-12-5-2022.csv")
nuevas_columnas= museos[header_viejo_museos]
print(nuevas_columnas.head())

crear_tabla_normalizada()
tabla_normalizada = nuevas_columnas.to_csv("datanormalizada/tabla-normalizada.csv",mode='a',header=False)




