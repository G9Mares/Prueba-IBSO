def crear_dict(cadena:str):
    diccionario = {}
    for indice,i in enumerate(cadena):
        diccionario[i] = indice+1
    return diccionario

# El valor de las letras depende de su orden
valores = crear_dict("abcdefghijklmnopqrstuvwxyz")

palabra_sum = input("Escribe una palabra solo con minusculas...")

suma_palabra = 0
palabra_final = ""
for lugar,letra in enumerate(palabra_sum):

    if letra not in valores:
        caracter = False
        while not caracter:
            print(f"el caracter {letra} en la posicion {lugar} no es valido, la lista de caracteres validos es {list(valores.keys())}")
            letra = input(f" remplazalo por uno valido...")
            if letra in valores:
              caracter = True
    palabra_final = palabra_final + letra
    suma_palabra = suma_palabra + valores[letra]

print(f"la palabra final fue {palabra_final} y sumo: {suma_palabra}")