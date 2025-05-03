casos = []

def agregar_caso(titulo, descripcion, dificultad, estado, fecha, lugar, sospechosos):
    if not (1 <= int(dificultad) <= 10):
        print("La dificultad debe estar entre 1 y 10.")
        return
    if estado.lower() not in ["abierto", "cerrado"]:
        print("El estado debe ser 'abierto' o 'cerrado'.")
        return
    if not (len(fecha) == 10 and fecha[2] == '/' and fecha[5] == '/'):
        print("La fecha debe estar en el formato DD/MM/AAAA.")
        return
    if not (lugar and lugar.strip()):
        print("El lugar no puede estar vacío.")
        return
    if not (sospechosos and all(s.strip() for s in sospechosos)):
        print("Los sospechosos no pueden estar vacíos.")
        return
    if not (titulo and titulo.strip()):
        print("El título no puede estar vacío.")
        return
    if not (descripcion and descripcion.strip()):
        print("La descripción no puede estar vacía.")
        return
    if not (estado and estado.strip()):
        print("El estado no puede estar vacío.")
        return
    if not (fecha and fecha.strip()):
        print("La fecha no puede estar vacía.")
        return
    if not (lugar and lugar.strip()):
        print("El lugar no puede estar vacío.")
        return
    if not (sospechosos and all(s.strip() for s in sospechosos)):
        print("Los sospechosos no pueden estar vacíos.")
        return
    if not (titulo and titulo.strip()):
        print("El título no puede estar vacío.")
        return
    if not (descripcion and descripcion.strip()):
        print("La descripción no puede estar vacía.")
        return
    if not (estado and estado.strip()):
        print("El estado no puede estar vacío.")
        return
    if not (fecha and fecha.strip()):
        print("La fecha no puede estar vacía.")
        return  
    caso = {
        "titulo": titulo,
        "descripcion": descripcion,
        "dificultad": dificultad,
        "estado": estado.lower(),
        "fecha": fecha,
        "lugar": lugar,
        "sospechosos": [s.strip() for s in sospechosos]
    }
    casos.append(caso)

def buscar_casos(casos, busqueda):
    encontrados = [cas for cas in casos if busqueda.lower() in cas["lugar"].lower()]
    if encontrados:
        for cas in encontrados:
            print("Caso encontrado:")
            print("Título:", cas["titulo"])
            print("Descripción:", cas["descripcion"])
            print("Dificultad:", cas["dificultad"])
            print("Estado:", cas["estado"])
            print("Fecha:", cas["fecha"])
            print("Lugar:", cas["lugar"])
            print("Sospechosos:", ", ".join(cas["sospechosos"]))
            print("--------------------------------------------------")
    else:
        print("No se encontraron casos que coincidan con la búsqueda.")

def casos_dificultad(casos):
    casos_ordenados = sorted(casos, key=lambda x: int(x["dificultad"]))
    for caso in casos_ordenados:
        print("Título:", caso["titulo"])
        print("Descripción:", caso["descripcion"])
        print("Dificultad:", caso["dificultad"])
        print("Estado:", caso["estado"])
        print("Fecha:", caso["fecha"])
        print("Lugar:", caso["lugar"])
        print("Sospechosos:", ", ".join(caso["sospechosos"]))
        print("--------------------------------------------------")

while True:
    for i in range(1, 8):
        print(" ")

    print("  ____  _               _            _         ")
    print(" / ___|| |__   ___  ___| | ___   ___| | __  ")
    print(" \___ \| '_ \ / _ \/ __| |/ _ \ / __| |/ / ")
    print("  ___) | | | |  __/ (__| | (_) | (__|   <")
    print(" |____/|_| |_|\___|\___|_|\___/ \___|_|\_\ ")
    print("                                              ")
    print("           Gestor de casos                    ")
    print("Menu")
    print("1. Agregar Nuevo caso")
    print("2. Buscar Casos")
    print("3. Mostrar casos ordenados por nivel de dificultad")
    print("4. Mostrar todos los casos sin ordenamiento alguno")
    print("5. salir")

    opcion = input("Selecciona una opción (1-5): ").strip()
    if not opcion.isdigit() or not (1 <= int(opcion) <= 5):
        print("Por favor, ingresa un número válido.")
        continue
    opcion = int(opcion)

    if opcion == 1:
        print("Agregando nuevo caso...")
        titulo = input("Ingrese el título del caso: ").strip()
        descripcion = input("Ingrese la descripción del caso: ").strip()
        dificultad = input("Ingrese el nivel de dificultad (1-10): ").strip()
        estado = input("Ingrese el estado del caso (abierto/cerrado): ").strip()
        fecha = input("Ingrese la fecha de creación del caso (DD/MM/AAAA): ").strip()
        lugar = input("Ingrese el lugar de los hechos: ").strip()
        sospechosos = input("Ingrese los sospechosos del caso (separados por comas): ").split(",")

        agregar_caso(titulo, descripcion, dificultad, estado, fecha, lugar, sospechosos)
        print("___________________________________________________________________________")
        print("El caso", titulo, "con el estado de", estado, "fue creado")

    elif opcion == 2:
        print("Buscando casos...")
        busqueda = input("Ingrese el término de búsqueda: ").strip()
        buscar_casos(casos, busqueda)

    elif opcion == 3:
        print("Mostrando casos ordenados por nivel de dificultad...\n")
        casos_dificultad(casos)

    elif opcion == 4:
        print("Los casos que están en el sistema son los siguientes:")
        for i in casos:
            print("Título:", i["titulo"])
            print("Descripción:", i["descripcion"])
            print("Dificultad:", i["dificultad"])
            print("Estado:", i["estado"])
            print("Fecha:", i["fecha"])
            print("Lugar:", i["lugar"])
            print("Sospechosos:", ", ".join(i["sospechosos"]))
            print("--------------------------------------------------")
        print(" ")

    elif opcion == 5:
        print("Saliendo del programa...")
        break
