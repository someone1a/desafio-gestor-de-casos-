print("  ____  _               _            _         ")
print(" / ___|| |__   ___  ___| | ___   ___| | __  ")
print(" \___ \| '_ \ / _ \/ __| |/ _ \ / __| |/ / ")
print("  ___) | | | |  __/ (__| | (_) | (__|   <")
print(" |____/|_| |_|\___|\___|_|\___/ \___|_|\_\ ")
print("                                              ")


while True:
    print("           Gestor de casos                    ")
    print("Menu")
    print("1. Agregar Nuevo caso")
    print("2. Buscar Casos")
    print("3. Mostrar casos ordenados por nivel de dificultad")
    print("4. Mostrar todos los casos sin ordenamiento alguno")
    print("5. salir")

    opcion = input("Selecciona una opción (1-4): ").strip()
    if not opcion.isdigit() or not (1 <= int(opcion) <= 5):
        print("Por favor, ingresa un número válido.")
        continue
    opcion = int(opcion)

    #FUNCION PARA AGREGAR CADA CASO
    def agregar_caso (titulo, descripcion, dificultad, estado, fecha, lugar, sospechosos):
        if dificultad.isdigit():
            return dificultad 
        else:
            print("Ingrese un numero valido")
        caso = {
        "titulo": titulo,
        "descripcion": descripcion,
        "dificultad": dificultad,
        "estado": estado,
        "lugar": lugar,
        "fecha": fecha,
        "sospechosos": sospechosos
    }
    
    #FUNCION PARA BUSCAR LOS CASOS 
    def buscar_casos(caso, busqueda):
        for caso in casos:
            if busqueda.lower() in caso["titulo"].lower() or busqueda.lower() in caso["descripcion"].lower():
                print("Caso encontrado:")
                print("Título:", caso["titulo"])
                print("Descripción:", caso["descripcion"])
                print("Dificultad:", caso["dificultad"])
                print("Estado:", caso["estado"])
                print("Fecha:", caso["fecha"])
                print("Lugar:", caso["lugar"])
                print("Sospechosos:", ", ".join(caso["sospechosos"]))
                return
            else:
                return "No se encontraron casos que coincidan con la búsqueda."

    #CASOS ORDENADOS POR DIFICULTAD     
    def casos_dificultad(caso):
        casos_ordenados = sorted(caso, key=lambda x: int(x["dificultad"]))
        for caso in casos_ordenados:
            print("Título:", caso["titulo"])
            print("Descripción:", caso["descripcion"])
            print("Dificultad:", caso["dificultad"])
            print("Estado:", caso["estado"])
            print("Fecha:", caso["fecha"])
            print("Lugar:", caso["lugar"])
            print("Sospechosos:", ", ".join(caso["sospechosos"]))
            print("--------------------------------------------------")

    if opcion == 1:
        print("Agregando nuevo caso...")
        titulo = input("Ingrese el título del caso: ")
        descripcion = input("Ingrese la descripción del caso: ")
        dificultad = input("Ingrese el nivel de dificultad (1-10): ")
        estado = input("Ingrese el estado del caso (abierto/cerrado): ")
        fecha = input("Ingrese la fecha de creación del caso (DD/MM/AAAA): ")
        lugar = input("ingrese el lugar de los hechos ")
        sospechosos = input("Ingrese los sospechosos del caso (separados por comas): ").split(",")

        agregar_caso(titulo, descripcion, dificultad, estado, fecha, sospechosos)
        print("___________________________________________________________________________")
        print("El caso", titulo, "con el estado de", estado, "Fue creado")

    elif opcion == 2:
        print("Buscando casos...")
        busqueda = input("Ingrese el término de búsqueda: ")
        resultado = buscar_casos(caso, busqueda)
        print(resultado)

    elif opcion == 3:
        print("Mostrando casos ordenados por nivel de dificultad...")
        print(" ")
        casos_dificultad(caso)


    elif opcion == 4: 
        print ("Los casos que estan en el sistema son los siguientes:")


    if opcion == 5:
        print("Saliendo del programa...")
        break