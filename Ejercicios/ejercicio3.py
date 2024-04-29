import pandas as pd
from datetime import datetime

class Data_inputs:
    def __init__(self):
        print("Objeto creandose")
        self.fecha_inicio = self.crear_fecha_incio()
        self.fecha_final = self.crear_fecha_final()
        self.categoria = self.crear_texto(opcional=True, campo="categoria")
        self.uso = self.crear_texto(opcional=True, campo="uso")
        self.sku = self.crear_texto(opcional=False, campo="sku")
        self.porcentaje = self.crear_numero(campo="porcentaje", decimal=True)
        self.inventario = self.crear_numero(campo="inventario inicial")
        

    def crear_fecha_incio(self):
        formato = "%d/%m/%Y"
        input_fecha = input("Ingresa una fecha de inicio con el formato dd/MM/yyyy (opcional)... ")
        try:
            return datetime.strptime(input_fecha,formato)
        except Exception as e:
            self.fecha_inicio = False
            print("Valor no reconocido se ha dejado en blanco")

    def crear_fecha_final(self):
        formato = "%d/%m/%Y"
        input_fecha = input("Ingresa una fecha de final con el formato dd/MM/yyyy (opcional)... ")
        try:
            fecha_fin = datetime.strptime(input_fecha,formato)
            if fecha_fin < self.fecha_inicio:
              raise
            return fecha_fin
        except Exception as e:
            self.fecha_fin = False
            print("Valor no reconocido o la fecha de fin no puede ser menor a la de incio, se ha dejado en blanco")

    def crear_texto(self,campo:str, opcional=False):
        text_op = ""
        if opcional:
          text_op = "(opcional)"
        texto = input(f"Ingresa {campo}...{text_op}")
        if not opcional and len(texto)<1:
          raise ValueError(f"El campo {campo} es obligatorio")
        return texto
    
    def crear_numero(self, campo:str, decimal:bool = False):
        texto = input(f"Ingresa {campo}...")
        try:
            numero = int(texto)
            if decimal:
               return round(numero/100,2)
            return numero
        except:
            raise ValueError(f"El {texto} no se puede convertir a numero")
    
    def obtener_semana_ISO(self, fecha_str:str, respuesta:str = False):
        formato = "%d-%m-%y %H:%M"
        try:
            fecha = datetime.strptime(fecha_str,formato)
            if respuesta == "fecha":
              return fecha
            anio, semana, dia= fecha.isocalendar()
            return semana
        except Exception as e:
            print(e)
            return "No se puede convertir"
        
    def ajustar_piezas(self,registro:dict):
        fecha_reg = self.obtener_semana_ISO(registro['Fecha'],respuesta="fecha")
        if self.fecha_inicio and  self.fecha_inicio < fecha_reg:
          return float(registro['Piezas'])
        if self.fecha_final and fecha_reg > self.fecha_final:
          return float(registro['Piezas'])
        if registro['Modelo'] == "real":
          return float(registro['Piezas'])
        if self.uso:
            if registro['Uso'] != self.uso:
                return float(registro['Piezas'])
            else:
               return float(registro['Piezas']) * (self.porcentaje +1)
        if self.categoria:
            if registro['Categoria'] != self.categoria:
                return registro['Piezas']
            else:
               return float(registro['Piezas']) * (self.porcentaje +1)
        return float(registro['Piezas']) * (self.porcentaje +1)

inputs_data = Data_inputs()


df_promos = pd.read_csv("./Ejercicios/Prueba_Promociones.csv")
df_promos['numero_semana'] = df_promos['Fecha'].apply(inputs_data.obtener_semana_ISO)


df_promos['Piezas'] = df_promos.apply(inputs_data.ajustar_piezas, axis=1)

df_filters_by_sku = df_promos.query(f" SKU == '{inputs_data.sku}' and Modelo != 'real'").copy()
df_filters_by_sku["Fecha_parsed"] = pd.to_datetime(df_filters_by_sku['Fecha'],format="%d-%m-%y %H:%M")
df_filters_by_sku.sort_values(by="Fecha_parsed", ascending=True,inplace=True)

df_filters_by_sku["inventario_acumulado"] = df_filters_by_sku['Piezas'].cumsum()

fecha_cero = df_filters_by_sku.query(f" inventario_acumulado >= {inputs_data.inventario}")
try:
    print(f"la fecha en la que se acaba el inventario es {fecha_cero.iloc[0]['Fecha']}")
except Exception as e:
   print(e)
   print("No es suficiente el inventario inicial se acabara desde el dia 0")
