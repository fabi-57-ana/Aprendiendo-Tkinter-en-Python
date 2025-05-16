import tkinter as tk
from PIL import Image, ImageTk
import os
import random  

ventana = tk.Tk()
ventana.title("Monitor de Ambiente")
ventana.geometry("800x600") 


ruta_imagen = os.path.join("imagenes", "C:/Users/Usuario/Documents/Modulo Programacion/img/6023003.jpg")  # Asegúrate de tener una imagen relacionada
try:
    imagen_fondo = Image.open(ruta_imagen)
    imagen_fondo = imagen_fondo.resize((800, 600), Image.Resampling.LANCZOS)  
    fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    fondo_label = tk.Label(ventana, image=fondo_tk)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)  

except FileNotFoundError:
    print("Error: No se encontró la imagen de fondo.")


def actualizar_datos():
    
    temperatura = random.uniform(20.0, 30.0)
    humedad = random.uniform(40.0, 80.0)
    
    
    label_temp.config(text=f"Temperatura: {temperatura:.1f} °C")
    label_humedad.config(text=f"Humedad: {humedad:.1f} %")
    
    
    ventana.after(2000, actualizar_datos)


estilo_label = {
    "font": ("Arial", 24, "bold"),
    "bg": "#333333", 
    "fg": "white",    
    "borderwidth": 2,
    "relief": "ridge"
}


label_temp = tk.Label(ventana, **estilo_label)
label_temp.place(x=100, y=100, width=300, height=100)


label_humedad = tk.Label(ventana, **estilo_label)
label_humedad.place(x=100, y=250, width=300, height=100)


actualizar_datos()


ventana.mainloop()


#####################################################################################


# # Prototipo para Evidencia 2.
# print("Bienvenido al Sistema de Monitoreo de AgroTech Coop")

# # Listas para simular una "base de datos" (esto es temporal, luego será reemplazado por SQL)
# parcelas = []
# sensores = []
# mediciones = []

# while True:
#     print("\n--- Menú Principal ---")
#     print("1. Gestionar Parcelas")
#     print("2. Gestionar Sensores")
#     print("3. Registrar Mediciones")
#     print("4. Consultar Datos")
#     print("5. Salir")
    
#     opcion = input("Ingrese una opción: ")
    
#     # Opción 1: Gestionar Parcelas
#     if opcion == "1":
#         print("\n--- Gestionar Parcelas ---")
#         print("1. Ver parcelas")
#         print("2. Agregar parcela")
#         print("3. Volver al menú principal")
        
#         sub_opcion = input("Seleccione una opción: ")
        
#         if sub_opcion == "1":
#             if len(parcelas) == 0:
#                 print("No hay parcelas registradas.")
#             else:
#                 print("Parcelas registradas:")
#                 for parcela in parcelas:
#                     print(f"ID: {parcela['id']}, Ubicación: {parcela['ubicacion']}, Cultivo: {parcela['cultivo']}")
        
#         elif sub_opcion == "2":
#             print("\nAgregar nueva parcela:")
#             id_parcela = len(parcelas) + 1
#             ubicacion = input("Ubicación: ")
#             cultivo = input("Tipo de cultivo: ")
#             parcelas.append({
#                 "id": id_parcela,
#                 "ubicacion": ubicacion,
#                 "cultivo": cultivo
#             })
#             print("¡Parcela registrada con éxito!")
    
#     # Opción 2: Gestionar Sensores (similar a parcelas)
#     elif opcion == "2":
#         print("\n--- Gestionar Sensores ---")
#         print("1. Ver sensores")
#         print("2. Agregar sensor")
#         print("3. Volver al menú principal")
        
#         sub_opcion = input("Seleccione una opción: ")
        
#         if sub_opcion == "1":
#             if len(sensores) == 0:
#                 print("No hay sensores registrados.")
#             else:
#                 print("Sensores registrados:")
#                 for sensor in sensores:
#                     print(f"ID: {sensor['id']}, Tipo: {sensor['tipo']}, Parcela ID: {sensor['id_parcela']}")
        
#         elif sub_opcion == "2":
#             print("\nAgregar nuevo sensor:")
#             id_sensor = len(sensores) + 1
#             tipo = input("Tipo de sensor (ej. Temperatura): ")
#             id_parcela = input("ID de parcela: ")
#             sensores.append({
#                 "id": id_sensor,
#                 "tipo": tipo,
#                 "id_parcela": id_parcela
#             })
#             print("¡Sensor registrado con éxito!")
    
#     # Opción 3: Registrar Mediciones
#     elif opcion == "3":
#         print("\n--- Registrar Mediciones ---")
#         if len(sensores) == 0:
#             print("Primero registre al menos un sensor.")
#         else:
#             id_sensor = input("ID del sensor: ")
#             valor = input("Valor de la medición: ")
#             fecha = input("Fecha (DD/MM/AAAA): ")
#             mediciones.append({
#                 "id_sensor": id_sensor,
#                 "valor": valor,
#                 "fecha": fecha
#             })
#             print("¡Medición registrada!")
    
#     # Opción 4: Consultar Datos
#     elif opcion == "4":
#         print("\n--- Consultar Datos ---")
#         print("1. Ver últimas mediciones por parcela")
#         print("2. Ver últimas mediciones por tipo de sensor")
        
#         sub_opcion = input("Seleccione una opción: ")
        
#         if sub_opcion == "1":
#             if len(mediciones) == 0:
#                 print("No hay mediciones registradas.")
#             else:
#                 print("Últimas mediciones:")
#                 for med in mediciones[-5:]:  # Muestra las últimas 5
#                     print(f"Sensor ID: {med['id_sensor']}, Valor: {med['valor']}, Fecha: {med['fecha']}")
    
#     # Opción 5: Salir
#     elif opcion == "5":
#         print("Saliendo del sistema...")
#         break
    
#     else:
#         print("Opción no válida. Intente nuevamente.")



#####################################################################################################




# # Prototipo para Evidencia 2 - Con datos simulados y explicaciones
# print("Bienvenido al Sistema de Monitoreo de AgroTech Coop")

# # ===== DATOS SIMULADOS (PARA PRUEBAS) =====
# parcelas = [
#     {"id": 1, "ubicacion": "Campo Norte", "cultivo": "Soja"},
#     {"id": 2, "ubicacion": "Campo Sur", "cultivo": "Maíz"}
# ]

# sensores = [
#     {"id": 1, "tipo": "Temperatura", "id_parcela": 1},
#     {"id": 2, "tipo": "Humedad", "id_parcela": 2}
# ]

# mediciones = [
#     {"id_sensor": 1, "valor": "25.5°C", "fecha": "10/05/2024"},
#     {"id_sensor": 2, "valor": "60%", "fecha": "09/05/2024"}
# ]
# # ===== FIN DE DATOS SIMULADOS =====

# while True:
#     print("\n--- Menú Principal ---")
#     print("1. Gestionar Parcelas")
#     print("2. Gestionar Sensores")
#     print("3. Registrar Mediciones")
#     print("4. Consultar Datos")
#     print("5. Salir")
    
#     opcion = input("Ingrese una opción: ")
    
#     # --- Opción 1: Gestionar Parcelas ---
#     if opcion == "1":
#         print("\n--- Gestionar Parcelas ---")
#         print("1. Ver parcelas")
#         print("2. Agregar parcela")
#         print("3. Volver al menú principal")
        
#         sub_opcion = input("Seleccione una opción: ")
        
#         if sub_opcion == "1":
#             print("\nParcelas registradas:")
#             for parcela in parcelas:
#                 print(f"ID: {parcela['id']} | Ubicación: {parcela['ubicacion']} | Cultivo: {parcela['cultivo']}")
        
#         elif sub_opcion == "2":
#             print("\nAgregar nueva parcela:")
#             id_parcela = len(parcelas) + 1
#             ubicacion = input("Ubicación (ej. 'Campo Este'): ")
#             cultivo = input("Tipo de cultivo (ej. 'Trigo'): ")
#             parcelas.append({
#                 "id": id_parcela,
#                 "ubicacion": ubicacion,
#                 "cultivo": cultivo
#             })
#             print(f"¡Parcela '{ubicacion}' registrada con éxito!")
    
#     # --- Opción 2: Gestionar Sensores ---
#     elif opcion == "2":
#         print("\n--- Gestionar Sensores ---")
#         print("1. Ver sensores")
#         print("2. Agregar sensor")
#         print("3. Volver al menú principal")
        
#         sub_opcion = input("Seleccione una opción: ")
        
#         if sub_opcion == "1":
#             print("\nSensores registrados:")
#             for sensor in sensores:
#                 print(f"ID: {sensor['id']} | Tipo: {sensor['tipo']} | Parcela ID: {sensor['id_parcela']}")
        
#         elif sub_opcion == "2":
#             print("\nAgregar nuevo sensor:")
#             id_sensor = len(sensores) + 1
#             tipo = input("Tipo de sensor (ej. 'pH'): ")
#             id_parcela = input("ID de parcela (ej. '1'): ")
#             sensores.append({
#                 "id": id_sensor,
#                 "tipo": tipo,
#                 "id_parcela": id_parcela
#             })
#             print(f"¡Sensor de '{tipo}' registrado en parcela {id_parcela}!")
    
#     # --- Opción 3: Registrar Mediciones ---
#     elif opcion == "3":
#         print("\n--- Registrar Mediciones ---")
#         if len(sensores) == 0:
#             print("Error: No hay sensores registrados.")
#         else:
#             print("Sensores disponibles:")
#             for sensor in sensores:
#                 print(f"ID: {sensor['id']} | Tipo: {sensor['tipo']}")
            
#             id_sensor = input("ID del sensor: ")
#             valor = input("Valor (ej. '7.2 pH'): ")
#             fecha = input("Fecha (DD/MM/AAAA): ")
#             mediciones.append({
#                 "id_sensor": id_sensor,
#                 "valor": valor,
#                 "fecha": fecha
#             })
#             print("¡Medición registrada!")
    
#     # --- Opción 4: Consultar Datos ---
#     elif opcion == "4":
#         print("\n--- Consultar Datos ---")
#         print("1. Ver todas las mediciones")
#         print("2. Ver mediciones por sensor")
        
#         sub_opcion = input("Seleccione una opción: ")
        
#         if sub_opcion == "1":
#             print("\nTodas las mediciones:")
#             for med in mediciones:
#                 print(f"Sensor {med['id_sensor']}: {med['valor']} | Fecha: {med['fecha']}")
        
#         elif sub_opcion == "2":
#             sensor_id = input("ID del sensor: ")
#             print(f"\nMediciones del sensor {sensor_id}:")
#             for med in mediciones:
#                 if med["id_sensor"] == sensor_id:
#                     print(f"{med['valor']} | {med['fecha']}")
    
#     # --- Opción 5: Salir ---
#     elif opcion == "5":
#         print("Saliendo del sistema...")
#         break
    
#     else:
#         print("Opción no válida. Intente nuevamente.")





# Explicación del Código
# 1. Datos Simulados
# python
# parcelas = [
#     {"id": 1, "ubicacion": "Campo Norte", "cultivo": "Soja"},
#     {"id": 2, "ubicacion": "Campo Sur", "cultivo": "Maíz"}
# ]
# Listas de diccionarios: Simulan una base de datos simple.

# parcelas: Contiene parcelas pre-registradas.

# sensores: Sensores ya instalados.

# mediciones: Datos históricos de mediciones.

# 2. Menú Principal
# Bucle while True: Mantiene el programa en ejecución hasta que el usuario elija "Salir".

# Input de opciones: El usuario interactúa mediante números (1, 2, etc.).

# 3. Gestión de Parcelas
# Ver parcelas: Muestra los datos simulados con un for.

# python
# for parcela in parcelas:
#     print(f"ID: {parcela['id']} | Ubicación: {parcela['ubicacion']}")
# Agregar parcela: Añade un nuevo diccionario a la lista parcelas.

# 4. Gestión de Sensores
# Similar a parcelas, pero con datos de sensores (tipo y parcela asociada).

# 5. Registro de Mediciones
# Valida que existan sensores antes de registrar.

# Ejemplo de medición:

# python
# mediciones.append({"id_sensor": 1, "valor": "25°C", "fecha": "10/05/2024"})
# 6. Consultas
# Muestra todas las mediciones o filtra por ID de sensor.

# Simulación de Resultados
# Al ejecutar el programa y seleccionar opciones:

# Ver parcelas:

# ID: 1 | Ubicación: Campo Norte | Cultivo: Soja
# ID: 2 | Ubicación: Campo Sur | Cultivo: Maíz
# Ver sensores:

# ID: 1 | Tipo: Temperatura | Parcela ID: 1
# ID: 2 | Tipo: Humedad | Parcela ID: 2
# Consultar mediciones:

# Sensor 1: 25.5°C | Fecha: 10/05/2024
# Sensor 2: 60% | Fecha: 09/05/2024
# Cómo Entregar
# main.py: Con el código completo.

# README.md:

# markdown
# # Evidencia 2 - AgroTech Coop
# **Integrantes**: 
# - Nombre 1, DNI
# - Nombre 2, DNI
# **Instrucciones**: Ejecutar `python main.py`.
# Documentación: Explicar en un PDF cómo se estructuran los datos simulados y su relación con el modelo relacional futuro.

# Nota: Este prototipo será la base para la Evidencia 3, donde se reemplazarán las listas por una base de datos SQL real.


#############################################################################################


# Un sistema de gestión de parcelas en un campo es una herramienta digital diseñada para organizar, monitorear y optimizar el uso de la tierra en actividades agrícolas. En el contexto de tu proyecto para AgroTech Coop, este sistema permitiría a la cooperativa administrar sus parcelas de cultivo de manera eficiente, integrando datos de sensores IoT para tomar decisiones basadas en información en tiempo real.

# ¿Qué hace un sistema de gestión de parcelas?
# Registro de Parcelas:

# Almacena información clave como:

# Ubicación (georreferenciación, coordenadas GPS).

# Tamaño (hectáreas, metros cuadrados).

# Tipo de cultivo (soja, maíz, trigo, etc.).

# Historial de siembras y rotaciones.

# Monitoreo de Condiciones Ambientales:

# Utiliza sensores IoT para medir:

# Humedad del suelo.

# Temperatura ambiente.

# pH del suelo.

# Radiación solar, lluvia, etc.

# Gestión de Sensores:

# Registra qué sensores están instalados en cada parcela.

# Mantiene un inventario de dispositivos (modelos, fechas de instalación, mantenimiento).

# Análisis de Datos:

# Genera informes y alertas (ej: "Parcela 3 necesita riego urgente").

# Compara rendimientos entre parcelas.

# Toma de Decisiones:

# Ayuda a planificar:

# Riegos.

# Fertilizaciones.

# Cosechas.

# Ejemplo Práctico en AgroTech Coop
# Imagina que la cooperativa tiene:

# Parcela A: 10 hectáreas de soja con sensores de humedad.

# Parcela B: 5 hectáreas de maíz con sensores de temperatura.

# El sistema permitiría:

# Ver en un dashboard que la humedad en la Parcela A bajó al 30% (umbral crítico).

# Recibir una alerta para activar el riego automático.

# Registrar que se aplicó fertilizante en la Parcela B el 10/05/2024.

# Componentes Clave (Para tu Proyecto)
# Base de Datos Relacional:

# Tablas: Parcelas, Sensores, Mediciones.

# Relaciones: Una parcela → muchos sensores → muchas mediciones.

# Interfaz de Usuario (Consola Python):

# Menú para:

# python
# print("1. Agregar parcela")
# print("2. Ver mediciones de humedad")
# Integración con Sensores IoT:

# En tu prototipo, simulas datos, pero en la vida real se conectaría a APIs de sensores físicos.

# ¿Por qué es importante?
# Ahorro de recursos: Evita riegos o fertilizaciones innecesarias.

# Mayor productividad: Detecta problemas antes de que afecten los cultivos.

# Trazabilidad: Registro histórico para cumplir normas agrícolas.

# Diferencia entre tu Prototipo y un Sistema Real
# Prototipo (Evidencia 2)	Sistema Real
# Datos en listas Python	Base de datos SQL (MySQL, PostgreSQL)
# Consola básica	Interfaz web/móvil con mapas
# Sensores simulados	Sensores IoT físicos (LoRa, Zigbee)
# Ejemplo de Flujo en tu Código
# python
# # Datos de ejemplo (simulados)
# parcelas = [
#     {"id": 1, "ubicacion": "Campo Norte", "cultivo": "Soja", "hectareas": 10}
# ]

# # Consultar parcelas
# print("Parcelas registradas:")
# for p in parcelas:
#     print(f"ID: {p['id']} - {p['ubicacion']} ({p['hectareas']} ha)")
# Output:

# Parcelas registradas:
# ID: 1 - Campo Norte (10 ha)
# Conclusión
# Tu sistema de gestión de parcelas en AgroTech Coop es el primer paso hacia una agricultura de precisión, donde la tecnología optimiza el uso de recursos naturales y maximiza la producción. En las siguientes evidencias, pasarás de un prototipo en consola a un sistema conectado a bases de datos y sensores reales.

# Tips para tu proyecto:

# Usa el diagrama de BD para clarificar relaciones entre parcelas y sensores.

# Documenta cómo escalarías el sistema (ej: añadir drones o imágenes satelitales).




