#  Pila (LIFO) 
# Utilizar una lista de Python para almacenar los registros de salidas. 
# Agregar cada salida al final de la lista mediante append(). 
# Deshacer la última salida mediante pop(), comprobando antes que la pila no esté vacía. 
# Permitir visualizar las salidas registradas y señalar cuál es la última. 
salidas_buses = []

#Salidas de la terminal de autobuses 
salidas_buses.append("Ruta 3 - hora de salida: 3:30 am")
salidas_buses.append("Ruta 11 - hora de salida: 4:00 am")
salidas_buses.append("Ruta 13 - hora de salida: 3:45 am")
salidas_buses.append("Ruta 16 - hora de salida: 5:00 am")
salidas_buses.append("Ruta 2 - hora de salida: 6:00 am")

# Permitir visualizar las salidas registradas
print("\n SALIDAS DE BUSES REGISTRADAS")
for salidas in salidas_buses:
    print(salidas)

# Deshacer la última salida con pop(), después de comprobar que la lista no esté vacía.
if not (salidas_buses):
    print("No hay salida de buses por el momento")

else:
    ultima_salida = salidas_buses.pop()
    print("Ultima salida registrada: ", ultima_salida)



# Cola (FIFO)
# Utilizar una lista para almacenar pasajeros en espera.
# Registrar cada pasajero al final de la cola mediante append().
# Atender al pasajero que ingresó primero, retirándolo con pop(0).
pasajeros = []

def registrar_pasajero(cola, turno, nombre, destino):
    cola.append({
        "turno": turno,
        "nombre": nombre,
        "destino": destino
    })

# Nuevos pasajeros
registrar_pasajero(pasajeros, "P001", "Ana López", "San Miguel")
registrar_pasajero(pasajeros, "P002", "Carlos Pérez", "La Unión")
registrar_pasajero(pasajeros, "P003", "María Gómez", "Usulután")

# Muestra a los pasajeros con sus respectivos datos.
def mostrar_pasajeros(cola):
    print("\n PASAJEROS EN ESPERA")
    for pasajero in cola:
        print(f"{pasajero['turno']} {pasajero['nombre']} {pasajero['destino']}")

# Verifica que haya pasajeros, atiende al primero y muestra sus datos
def atender_pasajero(cola):
    if not cola:
        print("No hay pasajeros para atender.")

    else: 
        en_espera = len(cola)
        atendido = cola.pop(0)
        print("\n PASAJERO ATENDIDO")
        print(f"Turno: {atendido['turno']}")
        print(f"Nombre: {atendido['nombre']}")
        print(f"Total en espera: {en_espera}")

# Muestra la cola y atiende al primer pasajero.
mostrar_pasajeros(pasajeros)
atender_pasajero(pasajeros)



# Árbol de destinos
# Crear una clase NodoDestino con el nombre del destino y una lista de hijos.
# Construir una jerarquía que incluya Terminal Central, regiones y destinos.
# Implementar una función recursiva para mostrar la jerarquía.
# Implementar una búsqueda recursiva que devuelva el destino si existe o None si no existe.

# Cada nodo guarda el nombre de un destino y una lista de destinos hijos
class NodoDestino:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []


# Se organiza la terminal, las regiones y sus destinos en forma de árbol
terminal = NodoDestino("Terminal Central")
zona_oriental = NodoDestino("Zona Oriental")
zona_central = NodoDestino("Zona Central")
zona_occidental = NodoDestino("Zona Occidental")

terminal.hijos = [zona_oriental, zona_central, zona_occidental]
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

# Muestra cada destino y sus hijos usando una función recursiva
def mostrar_arbol(nodo, nivel=0):
    if nodo is not None:
        print("  " * nivel + "- " + nodo.nombre)
        for hijo in nodo.hijos:
            mostrar_arbol(hijo, nivel + 1)


# Busca el destino en el nodo actual y luego en sus hijos
# Devuelve el nodo encontrado o None si no existe.
def buscar_destino(nodo, nombre):
    if nodo is None:
        return None
    if nodo.nombre.lower() == nombre.lower():
        return nodo

    for hijo in nodo.hijos:
        resultado = buscar_destino(hijo, nombre)
        if resultado is not None:
            return resultado

    return None


# Muestra la jerarquía y busca un destino
print("\n ÁRBOL DE DESTINOS")
mostrar_arbol(terminal)

destino_buscado = buscar_destino(terminal, "San Miguel")
if destino_buscado is not None:
    print(f"\nDestino: {destino_buscado.nombre}")
else:
    print("\nEl destino no existe.")
