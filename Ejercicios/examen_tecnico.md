# Examen tecnico
 
## Explica con el mayor detalle las respuestas a estas preguntas (45 minutos).:
Con las preguntas mostradas, trata de desarrollar los códigos para responder el mayor número de ejercicios usando Python.

- **Pregunta 1**:
1.	La información del ERP del cliente vive en un data center controlado por un proveedor, con reglas que no permiten adicionar campos, columnas, construir tablas o extraer información. ¿Qué pasos harías para pasar de la información en el ERP, cruzar y transformarla, y mandarla a una herramienta  de Business Intelligence con actualizaciones automáticas?

<u>**Respuesta**</u>:
Escribiría un script en python que esté escuchando constantemente la base de datos, dicho script replicaría la base de datos usando SQL alchemy; aparte que lo agregaría a un servidor fastapy para la consulta y modificación de manera remota en cualquier momento.

- **Pregunta 2**:
2.	El cliente de la pregunta 1 está evaluando adquirir un servidor físico o en la nube para poder alojar ahí un espejo de la información de su ERP. ¿Qué recomendarías en cuanto a costo o inversión y el rendimiento esperado dadas las características de cada una de las opciones?

<u>**Respuesta**</u>:
Crearía una análisis basado en la cantidad de los datos, peticiones y tiempo de uso de la base de datos, ya que son los principales parámetros para los precios en los servicios de la nube, es decir si la cantidad de información es mínima, o no es necesario que se consuma todo el tiempo, sugeriría un alojamiento en la nube como aws-rds, de lo contrario sugeriría un servidor local con un firewall de última generación.

- **Pregunta 3**:
3.	Un cliente solamente cuenta con un servidor de producción donde viven los datos, ¿qué sugerirías para no afectar el desempeño de esta al conectar BI?

    a.	¿Cuáles serían las implicaciones (tiempo, conocimiento, administración, costo) de esta sugerencia?

<u>**Respuesta**</u>:
Dependiendo de la cantidad de peticiones y la complejidad de las mismas, utilizaría Power BI DirectQuery; también podría utilizar un mirror en diferentes servidores en la nube que solamente se ejecuten cuando se quieran consultar los datos, como el edge de cloudflare o netlify, incluso una lambda daws. En cuestión de tiempo y conocimiento, requieren de un ingeniero experimentado en la replicación y que utilice las tecnologías mencionadas, asimismo un experto en ciberseguridad para la protección de los datos y amplio conocimiento en los protocolos necesarios para la consulta de datos, por ejemplo los clusters. El costo ignorando los costos de personal, dependerá de cuantos mirrors haya disponibles y de la complejidad de las consultas del servidor, aunque se pueden ahorrar costos si se activa cada que se utilice. Y en la parte de tiempo el proceso más tardado sería la migración de la base de datos y la adaptabilidad a un nuevo protocolo.

- **Pregunta 4**:
4.	Un query que escribiste regresa 10,000 filas únicamente, pero su ejecución toma entre 3 y 4 horas. Por lo mismo, muchas veces no llegan los resultados completos a BI o se pierde la conexión mientras esto ocurre. ¿Qué harías?

<u>**Respuesta**</u>:
Depende, si tengo mucho presupuesto del cual disponer montaria clusters en el edge de netlify o cloudflare, asi la informacion esta segmentada y se puede repartir la carga de la query, tambien la informacion estaria disponible solo cuando se use. Si mi presupuesto es limitado crearia un script en python que recabara en bloques la informacion de la query, asi quitaria peso al servidor de la db y aunque ahorraria tiempo no seria tan significativo pero no se pondria en riesgo perder la conexion a la base de datos

- **Pregunta 5**:
5.	Te busca un cliente para decirte que los resultados que ve en los tableros no le hacen sentido (ayer si mostraba resultados correctos). ¿Qué pasos harías para darle una respuesta al cliente?

<u>**Respuesta**</u>:Para este tipo de casos es necesario contar previamente con sistemas de logs dentro de los sistemas, un sistema de migrado de bases de datos como alembic y respaldos de la informacion para brindar una correcta auditoria en caso de problemas. Independientemente de las herramientas de las cuales disponga rastrearia los datos anomalos, para rastrear el por que de los mismos, posteriormente con los datos identificados cargaria la informacion correcta de un respaldo, asi no se perderian actualizaciones en los demas registros

- **Pregunta 6**
6.	¿Qué mejores prácticas sugerirías para garantizar la seguridad de la información del cliente, ya sea en un servidor físico o en la nube?

<u>**Respuesta**</u>:
Tanto en la nube como local seria importante tener un buen protocolo de encriptado de datos, asi como un firewall de ultima generacion, en caso de ser posible manejar un entorno de pruebas o sandbox para trabajar de manera segura. Posteriormente como aclaraba en el punto anterior contar con protocolos y herramientas de migracion y recuperacion de db, asi como un sistema de logs, con roles y permisos para los usuarios. Tambien mencionar los tuneles de conexion sean seguros, es decir si manjo una conexion TLS o http, https hacerlo a traves de canales y puertos seguros. Pero el punto considero mas importante es la correta y continua capacitacion al personal





