import pandas as pd
from datetime import datetime, timedelta
from itertools import combinations

# Paso 1: Crear lista de fechas y bloques horarios
inicio_semestre = datetime(2023, 1, 1)
dias_rotacion = [2, 3, 4]  # Miércoles, Jueves, Viernes
bloques = ["AM", "PM"]
lugares = [f"Lugar_{i}" for i in range(1, 5)]

# Generar todas las fechas de los días de rotación en las 10 semanas
fechas = [inicio_semestre + timedelta(days=i) for i in range(70) if (inicio_semestre + timedelta(days=i)).weekday() in dias_rotacion]

# Paso 2: Crear lista de todos los bloques horarios posibles
bloques_horarios = [{'fecha': fecha, 'lugar': lugar, 'bloque': bloque} for fecha in fechas for lugar in lugares for bloque in bloques]

# Paso 3: Crear lista de individuos y parejas posibles
individuos = [f'Individuo_{i+1}' for i in range(20)]
parejas = list(combinations(individuos, 2))

# Paso 4: Crear una lista para almacenar las asignaciones
asignaciones = []

# Función para verificar si un individuo ya tiene una asignación en una fecha específica
def ya_asignado(individuo, fecha):
    return any(asignacion['fecha'] == fecha and (asignacion['individuo1'] == individuo or asignacion['individuo2'] == individuo) for asignacion in asignaciones)

# Asignar parejas a bloques horarios
for bloque_horario in bloques_horarios:
    for pareja in parejas:
        if not ya_asignado(pareja[0], bloque_horario['fecha']) and not ya_asignado(pareja[1], bloque_horario['fecha']):
            asignaciones.append({'fecha': bloque_horario['fecha'], 'lugar': bloque_horario['lugar'], 'bloque': bloque_horario['bloque'], 'individuo1': pareja[0], 'individuo2': pareja[1]})
            parejas.remove(pareja)
            break

# Paso 5: Convertir la lista de asignaciones a un DataFrame
df = pd.DataFrame(asignaciones)
print(df)
