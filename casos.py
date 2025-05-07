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
    print(" ")

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
def agregar_caso(titulo, descripcion, dificultad, estado, fecha, lugar, sospechosos, casos):
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
    print("Caso agregado exitosamente.")