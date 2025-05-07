casos = []
from casos import casos_dificultad, buscar_casos, agregar_caso

while True:
    for i in range(1, 3):
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

        agregar_caso(titulo, descripcion, dificultad, estado, fecha, lugar, sospechosos, casos)
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
