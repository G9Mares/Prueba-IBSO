from fastapi import FastAPI, Query, Request
from ejercicio4 import api_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app = FastAPI()
@app.get("/get_listas")
async def home():
    listas = api_data.obtener_listas()
    return listas

@app.get("/get_book/{id_book}")
async def home(id_book:str):
    listas = api_data.obtener_libro(isbn=id_book)
    return listas

@app.post("/by_list")
async def home(request:Request):
    datos = await request.json()
    libros = api_data.obtener_libros(metodo="by_list",datos=datos)
    print(libros)
    return libros