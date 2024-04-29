# Ejercicios python
 
## Instrucciones:
Con las preguntas mostradas, trata de desarrollar los códigos para responder el mayor número de ejercicios usando Python.

- **Ejercicio 1**:
1.	Crea un diccionario llamado datos_climaticos donde cada clave es el nombre de una ciudad y el valor es una lista de temperaturas (en grados Celsius) registradas a lo largo de una semana.
2.	Para cada ciudad, calcula la temperatura promedio, la temperatura máxima y la mínima de la semana.
3.	Determina cuál fue la ciudad con la temperatura promedio más alta y la más baja durante la semana.

- **Ejercicio 2**:
Asigna a cada letra minúscula un valor, desde 1 para la 'a' hasta 26 para la 'z'. 
Crea una función que pida al usuario una cadena de letras minúsculas y responde la suma de los valores de las letras en la cadena. (Ejemplo: hola = 8 + 15 + 12 + 1 = 36). 
Si el usuario te da un número o una letra mayúscula, pídele que lo cambie (Input: Hola. Output: Cambia a minúscula la letra “H” en la posición 1. Input: int2. Output: Cambia el número en la posición 4 por una letra minúscula).

-**Ejercicio 3**: 
1. Extraer la información del csv Prueba_Promociones
2. ⁠Generar un código donde el usuario pueda ingresar las siguientes variables
- fecha inicio (convertir a datetime)
- ⁠fecha fin (convertir a datetime)
- ⁠categoría (validar que sea string)
- ⁠uso (validar que sea string)
- ⁠sku (no permitir al usuario avanzar si no ingreso un valor string en el campo de SKU)
- ⁠% (validar que sea número decimal)
- ⁠inventario inicial (validar que sea entero)
3. Generar una nueva columna donde se coloque el # de semana correspondiente de la fecha
4. ⁠Con él % ingresado por el usuario, impactar ese porcentaje como crecimiento (columna de piezas) para todos los datos que cumplan con las siguientes condiciones:
- estén dentro del rango de fecha seleccionado. Si el usuario no coloca fecha fin entonces desde fecha inicio hasta el final, si el usuario no coloca fecha inicio entonces desde la fecha fin hasta el principio y si no coloca ninguna, a todas las fechas disponibles
- ⁠la columna modelo sea diferente a “real”
- ⁠la columna uso sea igual al valor ingresado por el usuario, en caso de que esté vacío ese campo, la columna categoría sea igual al valor ingresado por el usuario. En caso de que ambas vengan vacías aplicar a todo

-**Ejercicio 4**: Recomendador de libros
Fuente: https://developer.nytimes.com/docs/books-product/1/overview
Elementos a utilizar: 
1.	Crea una cuenta de Developer en la página de New York Times para tener un API key (https://developer.nytimes.com/)
2.	Usa el “Books API”. 
¿Qué debe poder hacer tu código?
1.	Pedirle al usuario decidir qué lista de “Best Sellers” quiere consultar. 
2.	Poder escoger si quiere ver los “Best Sellers” actuales o de alguna fecha en específica. 
3.	Poder escoger un precio específico del libro que quiere adquirir. 
4.	Poder escoger un rango de edades dirigido para el libro. 
Resultado: 
1.	Poder verlo de manera estructurada, poniendo la información clave del libro que estás recomendado para la información que te dio el usuario. 
2.	Poder acceder rápidamente a la reseña generada por el NYT acerca del libro recomendado.
3.	Para los Best Sellers actuales, decirle al usuario dónde lo puede comprar. 
4.	Poder mostrar toda esta información en una aplicación / pantalla / interfaz gráfica amigable para que el usuario pueda interactuar con los resultados.

