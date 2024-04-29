import statistics
import random

def crear_dict(claves:list, num_registros:int):
    diccionario = {}
    for clave  in claves:
        temperaturas = []
        for i in range(num_registros):
            temperatura = round(random.uniform(25,40),2)
            temperaturas.append(temperatura)
        diccionario[clave] = temperaturas

    return diccionario

ciudades = ['CDMX','Guadalajara','Monterrey','Veracruz']

datos_climaticos = crear_dict(claves=ciudades, num_registros=7)
datos_globales = {
    "ciudad_alta":{"ciudad":"","temperatura":0},
    "ciudad_baja":{"ciudad":"","temperatura":100}
    }
for key,value in datos_climaticos.items():
    temp_promedio = round(statistics.mean(value),2)
    temp_max = max(value)
    temp_min = min(value)
    if temp_promedio > datos_globales["ciudad_alta"]['temperatura']:
        datos_globales["ciudad_alta"]['ciudad'] = key 
        datos_globales["ciudad_alta"]['temperatura'] = temp_promedio 
    if temp_promedio < datos_globales["ciudad_baja"]['temperatura']:
        datos_globales["ciudad_baja"]['ciudad'] = key 
        datos_globales["ciudad_baja"]['temperatura'] = temp_promedio 


    print(f"La temperatura promedio de {key} es de: {temp_promedio}°C, su mas alta fue de {temp_max}°C y las mas baja de {temp_min}°C")

print(datos_globales)