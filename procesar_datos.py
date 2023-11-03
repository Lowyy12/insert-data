with open("datos.csv", "r") as fichero:
    nuevas_sentencias = []

    for x in fichero:
        campos = x.split(",")
        campo1 = str(campos[0].lower())
        valor1 = int(campos[1][1:])
        campo2 = str(campos[2][1:].lower())
        valor2 = str(campos[3][1:])
        campo3 = str(campos[4][1:].lower())
        valor3 = str(campos[5][1:-1].lower())

        # Crear la sentencia SQL para cada fila
        nueva_sentencia = f"insert into productos ({campo1}, {campo2}, {campo3}) values ({valor1}, '{valor2}', '{valor3}');"
        nuevas_sentencias.append(nueva_sentencia)

# Leer el contenido actual del archivo "productos.sql"
with open("productos.sql", "r") as archivo_sql:
    contenido_actual = archivo_sql.read()

# Filtrar las sentencias que no están en el archivo
sentencias_a_agregar = [sql for sql in nuevas_sentencias if sql not in contenido_actual]

# Escribir las sentencias SQL en el archivo existente sin repeticiones
with open("productos.sql", "a") as archivo_sql:  # Usamos "a" para añadir al archivo existente
    for sql in sentencias_a_agregar:
        archivo_sql.write("\n" + sql + "\n")
    archivo_sql.write("\n" + "commit;")
    archivo_sql.write("\n" + "select * from productos;")

print("Contenido añadido al archivo de datos")
