planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche']
}

inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15]
}

def leer_opcion():
    try:
        opcion = int(input("Ingrese opción: "))
        if opcion >= 1 and opcion <= 6:
            return opcion
        print("Debe seleccionar una opción válida")
        return 0
    except:
        print("Debe seleccionar una opción válida")
        return 0

def cupos_tipo(tipo):
    tipo = tipo.lower()
    total = 0
    for cod in planes:
        if planes[cod][1].lower() == tipo:
            total += inscripciones[cod][1]
    print(f"El total de cupos disponibles es: {total}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for cod in inscripciones:
        precio = inscripciones[cod][0]
        cupos = inscripciones[cod][1]
        if precio >= p_min and precio <= p_max and cupos > 0:
            nombre = planes[cod][0]
            resultados.append(f"{nombre}--{cod}")
            
    if len(resultados) > 0:
        resultados.sort()
        print(f"Los planes encontrados son: {resultados}")
    else:
        print("No hay planes en ese rango de precios.")

def buscar_codigo(codigo):
    if codigo.upper() in planes:
        return True
    return False

def actualizar_precio(codigo, nuevo_precio):
    if buscar_codigo(codigo):
        inscripciones[codigo.upper()][0] = nuevo_precio
        return True
    return False

def agregar_plan(codigo, nombre, tipo, duracion, piscina, clases, horario, precio, cupos):
    cod = codigo.upper()
    if buscar_codigo(cod):
        return False
        
    piscina_bool = piscina.lower() == 's'
    clases_bool = clases.lower() == 's'
    
    planes[cod] = [nombre, tipo, duracion, piscina_bool, clases_bool, horario]
    inscripciones[cod] = [precio, cupos]
    return True

def eliminar_plan(codigo):
    cod = codigo.upper()
    if buscar_codigo(cod):
        del planes[cod]
        del inscripciones[cod]
        return True
    return False

while True:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("=====================================")
    
    opc = leer_opcion()
    if opc == 0:
        continue
        
    if opc == 1:
        t = input("Ingrese tipo de plan a consultar: ")
        cupos_tipo(t)
        
    elif opc == 2:
        try:
            p_min = int(input("Ingrese precio mínimo: "))
            p_max = int(input("Ingrese precio máximo: "))
            busqueda_precio(p_min, p_max)
        except:
            print("Debe ingresar valores enteros")
            
    elif opc == 3:
        cod = input("Ingrese código del plan: ")
        try:
            nuevo_p = int(input("Ingrese nuevo precio: "))
            if actualizar_precio(cod, nuevo_p):
                print("Precio actualizado")
            else:
                print("El código no existe")
        except:
            print("Error en el precio ingresado")
            
        resp = input("¿Desea actualizar otro precio (s/n)?: ")
        if resp.lower() == 'n':
            pass 
            
    elif opc == 4:
        codigo = input("Ingrese código del plan: ")
        nombre = input("Ingrese nombre del plan: ")
        tipo = input("Ingrese tipo (mensual/trimestral/anual): ")
        duracion = int(input("Ingrese duración (meses): "))
        piscina = input("¿Incluye acceso a piscina? (s/n): ")
        clases = input("¿Incluye clases grupales? (s/n): ")
        horario = input("Ingrese horario: ")
        precio = int(input("Ingrese precio: "))
        cupos = int(input("Ingrese cupos: "))
        
        if codigo == "" or nombre == "" or tipo not in ['mensual', 'trimestral', 'anual']:
            print("Error: Datos inválidos.")
        else:
            if agregar_plan(codigo, nombre, tipo, duracion, piscina, clases, horario, precio, cupos):
                print("Plan agregado")
            else:
                print("El código ya existe")
                
    elif opc == 5:
        codigo = input("Ingrese código del plan: ")
        if eliminar_plan(codigo):
            print("Plan eliminado")
        else:
            print("El código no existe")
            
    elif opc == 6:
        print("Programa finalizado.")
        break