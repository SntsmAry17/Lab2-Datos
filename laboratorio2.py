# LABORATORIO 2
# SISTEMA DE TERMINAL DE BUSES
# NOTA: RETOS ELEGIDOS:
# Registrar fecha y hora de cada salida. 
# Necesidad que resuelve: Permite llevar un registro de la fecha y hora en que se registra cada salida de bus, facilitando el control y seguimiento de las operaciones de la terminal.
# Evitar códigos de bus duplicados. 
# Necesidad que resuelve: Evita registros duplicados de buses, permitiendo mantener información única y organizada sobre las unidades que realizan las salidas.

from datetime import datetime #importacion para tener fecha y hora exacta a la hora de registrar el bus

# LIFO: REGISTRO DE SALIDAS DE BUSES

salidas_buses = []
#Funcion que recibe codigo de bus, ruta y hora de salida programada
def registrar_salidas(pila, codigo, ruta, hora_salida):
    # Evita registrar datos vacíos.
    if not codigo.strip() or not ruta.strip() or not hora_salida.strip(): # el metodo .strip ayuda a validar si existen espacios en blanco
        print("Error: todos los campos son obligatorios.")
        return

    # Comprueba que no exista otro bus con el mismo código.
    for salida in pila:
        if salida["codigo"].lower() == codigo.strip().lower(): #.lower para que todos los datos agregados pasen todo el texto a minusculas
            print("Error: el código de bus ya está registrado.")
            return

    # variable que obtiene la fecha y hora actual
    fecha_hora = datetime.now()

    # Agrega la salida al final de la pila.
    pila.append({
        "codigo": codigo.strip(),
        "ruta": ruta.strip(),
        "hora_salida": hora_salida.strip(),
        "fecha_registrada": fecha_hora
    })

    print("Salida registrada correctamente.")

# funcion que valida si hay salidas registradas, si no encuentra registro de salida tira un mensaje de que no hay salidas registradas
def mostrar_salidas(pila):
    if not pila:
        print("No hay salidas registradas.")
        return

    print("\n--- SALIDAS DE BUSES REGISTRADAS ---")

    for salida in pila:
        print(f"Código: {salida['codigo']}")
        print(f"Ruta: {salida['ruta']}")
        print(f"Hora de salida: {salida['hora_salida']}")
        print(
            "Fecha de registro: "
            f"{salida['fecha_registrada'].strftime('%d/%m/%Y %H:%M:%S')}"
        )
        print()

# funcion que elimina la salida registrada más recientemente con .pop()
def deshacer_salida(pila):

    ultima_salida = pila.pop()

    print("\n--- ÚLTIMA SALIDA ELIMINADA ---")
    print(f"Código: {ultima_salida['codigo']}")
    print(f"Ruta: {ultima_salida['ruta']}")
    print(f"Hora de salida: {ultima_salida['hora_salida']}")
    print(
        "Fecha de registro: "
        f"{ultima_salida['fecha_registrada'].strftime('%d/%m/%Y %H:%M:%S')}"
    )

# FIFO: REGISTRO Y ATENCIÓN DE PASAJEROS

pasajeros = []
# Funcion que registra y comprueba que los datos sean válidos y que el destino exista en el árbol de destinos y sea un destino final
def registrar_pasajero(cola, turno, nombre, destino):

    # Comprueba que ningún campo esté vacío.
    if not turno.strip() or not nombre.strip() or not destino.strip():
        print("Error: el turno, el nombre y el destino son obligatorios.")
        return

    # Busca el destino ingresado en el árbol.
    nodo = buscar_destino(terminal, destino.strip())

    # Rechaza destinos que no existen o que son regiones, en lugar de destinos finales.
    if nodo is None or nodo.hijos:
        print("Error: el destino no existe o no es un destino final.")
        return

    # Agrega al pasajero al final de la cola.
    cola.append({
        "turno": turno.strip(),
        "nombre": nombre.strip(),
        "destino": nodo.nombre
    })

    print("Pasajero registrado correctamente.")

# Funcion que muestra a los pasajeros que estan esperando a ser atendidos
def mostrar_pasajeros(cola):
   
    if not cola:
        print("No hay pasajeros en espera.")
        return

    print("\n--- PASAJEROS EN ESPERA ---")

    for pasajero in cola:
        print(f"Turno: {pasajero['turno']}")
        print(f"Nombre: {pasajero['nombre']}")
        print(f"Destino: {pasajero['destino']}")

#Funcion que atiende al primer pasajero registrado, eliminandolo con .pop(0)
def atender_pasajero(cola):

    if not cola:
        print("No hay pasajeros para atender.")
        return

    atendido = cola.pop(0)

    print("\n--- PASAJERO ATENDIDO ---")
    print(f"Turno: {atendido['turno']}")
    print(f"Nombre: {atendido['nombre']}")
    print(f"Destino: {atendido['destino']}")
    print(f"Pasajeros restantes: {len(cola)}")

# 3. ÁRBOL BINARIO DE DESTINOS

class NodoDestino:

    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

# Nodo principal del árbol.
terminal = NodoDestino("Terminal Central")

# Regiones que dependen de la terminal.
zona_oriental = NodoDestino("Zona Oriental")
zona_central = NodoDestino("Zona Central")
zona_occidental = NodoDestino("Zona Occidental")

terminal.hijos = [
    zona_oriental,
    zona_central,
    zona_occidental
]

# Destinos finales de cada región.
zona_oriental.hijos = [
    NodoDestino("San Miguel"),
    NodoDestino("La Unión"),
    NodoDestino("Usulután")
]

zona_central.hijos = [
    NodoDestino("San Salvador"),
    NodoDestino("La Libertad")
]

zona_occidental.hijos = [
    NodoDestino("Santa Ana"),
    NodoDestino("Ahuachapán")
]

#  Funcion que muestra el árbol de forma recursiva
def mostrar_arbol(nodo, nivel=0):

    if nodo is not None:
        print("  " * nivel + "- " + nodo.nombre)

        # Muestra cada hijo aumentando el nivel de profundidad.
        for hijo in nodo.hijos:
            mostrar_arbol(hijo, nivel + 1)

# funcion que busca un destino de forma recursiva.
def buscar_destino(nodo, nombre):

    if nodo is None:
        return None

    # Compara sin distinguir entre mayúsculas y minúsculas.
    if nodo.nombre.lower() == nombre.strip().lower():
        return nodo

    # Busca el nombre en cada uno de los hijos.
    for hijo in nodo.hijos:
        resultado = buscar_destino(hijo, nombre)

        if resultado is not None:
            return resultado

    return None

 # Solicitamos un nombre y comprobamos si existe en el árbol
def consultar_destino():

    nombre = input("Ingrese el destino que desea buscar: ").strip()

    if not nombre:
        print("Error: el nombre del destino no puede estar vacío.")
        return

    resultado = buscar_destino(terminal, nombre)

    if resultado is not None:
        print(f"Destino encontrado: {resultado.nombre}")
    else:
        print("El destino no existe en el árbol.")

# MENÚ 

def mostrar_menu():

    print("\n=== TERMINAL DE BUSES ===")
    print("1. Registrar salida de bus")
    print("2. Mostrar salidas registradas")
    print("3. Deshacer última salida")
    print("4. Registrar pasajero")
    print("5. Mostrar pasajeros en espera")
    print("6. Atender pasajero")
    print("7. Mostrar árbol de destinos")
    print("8. Buscar destino")
    print("0. Salir")

#Funcion que lee la opcion seleccionada y llama a la funcion que corresponde a esa opcion
def ejecutar_menu():

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            codigo = input("Código del bus(Ejemplo: B001): ")
            ruta = input("Ruta del bus(Ejemplo: ruta 301, ruta 11, ruta 12): ")
            hora = input("Hora programada de salida: ")

            registrar_salidas(salidas_buses, codigo, ruta, hora)

        elif opcion == "2":
            mostrar_salidas(salidas_buses)

        elif opcion == "3":
            deshacer_salida(salidas_buses)

        elif opcion == "4":
            turno = input("Turno del pasajero(ejemplo: P001): ")
            nombre = input("Nombre del pasajero: ")
            destino = input("Destino del pasajero: ")

            registrar_pasajero(pasajeros, turno, nombre, destino)

        elif opcion == "5":
            mostrar_pasajeros(pasajeros)

        elif opcion == "6":
            atender_pasajero(pasajeros)

        elif opcion == "7":
            print("\n--- ÁRBOL DE DESTINOS ---")
            mostrar_arbol(terminal)

        elif opcion == "8":
            consultar_destino()

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Seleccione una opción del menú.")


# Inicia el programa.
if __name__ == "__main__":
    ejecutar_menu()



