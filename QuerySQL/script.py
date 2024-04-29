import mysql.connector
from models import models

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = ""
db = "my_db"


conexion = mysql.connector.connect(
    host = HOST, 
    port = PORT,
    user = USER,
    password = PASSWORD,
    database = db
)

cursor = conexion.cursor(buffered=True)

# for i in models:
#     cursor.execute(i)
#     conexion.commit()

# vista_sql = """
# CREATE VIEW general_info_clients AS
# SELECT
#     doc.DNUM as ticket, doc.DFECHA as fecha, doc.DCANT as monto_neto, doc.DIVA as iva, doc.DBRUTO as monto_bruto, doc.DPAR1 as vendedor, doc.CLICOD as codigo_cliente,
#     clientes.CLINOM as cliente, clientes.CLICOD as codigo_client,
#     aux_inv.ICOD as productos_comprados, aux_inv.AICANTF as cantidad, aux_inv.AIALMACEN as almacen_vendedor, aux_inv.FMOV as numero_movimento,
#     inv.IDESCR as descripcion, inv.ILISTA3 as precio_lista, inv.IFAM3 as talla, inv.IFAM4 as color, inv.IFAM5 as temporada
# FROM 
#     FDOC doc
# LEFT JOIN FCLI AS clientes ON doc.CLICOD = clientes.CLICOD
# LEFT JOIN FAXINV AS aux_inv ON doc.DNUM = aux_inv.FMOV
# LEFT JOIN FINV AS inv ON inv.ICOD = aux_inv.ICOD

# """
# cursor.execute(vista_sql)


cursor.execute("SELECT * FROM general_info_clients")

resp = cursor.fetchall()
for art in resp:
    registro = dict(zip(cursor.column_names, art))  
    print(registro)
