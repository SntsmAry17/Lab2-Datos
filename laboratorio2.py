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

#Deshaser la ultima salida mediante .pop primero comprobando con if si la lista no este vacia 
if not (salidas_buses):
    print("No hay salida de buses por el momento")

else:
    ultima_salida = salidas_buses.pop()
    print("Ultima salida registrada: ", ultima_salida)
