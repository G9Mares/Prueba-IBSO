import requests
from datetime import datetime
from dotenv import load_dotenv
import os
import pandas as pd
load_dotenv()

def consumir_api(url,parametro):
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)
    if response.status_code != 200:
        return []
    return response.json()[parametro]

class BestSellers:
    def __init__(self):
        print("Objeto creado")

    def crear_fecha(self, fecha):
        try:
            datetime.strptime(fecha,"%Y-%m-%d")
            self.fecha_consulta = fecha
        except:
            return False
    
    def obtener_listas(self):
        datos_list = consumir_api( f"https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={os.getenv('API_KEY')}",'results')
        df_list = pd.DataFrame(datos_list)
        df_listas = pd.DataFrame({"nombre":df_list['list_name'], "value":df_list['list_name_encoded']})
        valores =df_listas.to_dict(orient="records")
        return valores
    
    def obtener_libros(self, metodo:str, datos:dict):
        if metodo == "by_list":
            url = f"https://api.nytimes.com/svc/books/v3/lists/{datos['rango_fecha']}/{datos['lista']}.json?api-key={os.getenv('API_KEY')}"
            libros = consumir_api(url=url,parametro="results")['books']
            self.df_aux_books = pd.DataFrame(libros)
            df_books = pd.DataFrame({"tittle":self.df_aux_books['title'],"image":self.df_aux_books['book_image'], 'value':self.df_aux_books['primary_isbn10']})
            books = df_books.to_dict(orient='records')
            return books
    def obtener_libro(self, isbn):
        libro = self.df_aux_books.query(f" primary_isbn10 == '{isbn}'")
        info_libro = libro.to_dict(orient="records")[0]
        return info_libro

        


api_data = BestSellers()