import os
import json

RUTA_ARCHIVO = "tareas.json" #usar mayusculas para rutas es una buena practica

def menu():
    print("\n--- 🙊🙉🙈  🜄 🜃 🜁 🜂 Gestor de Tareas 🜂 🜁 🜃 🜄  🙈🙉🙊 ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def cargar_tareas():
    if not os.path.exists(RUTA_ARCHIVO):
        return []
    try:
        with open(RUTA_ARCHIVO, "r", encoding='utf-8') as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []

def guardar_tareas(lista_de_tareas):
    with open(RUTA_ARCHIVO, "w", encoding='utf-8') as archivo:
        json.dump(lista_de_tareas, archivo, indent=4)

def agregar_tarea(lista_de_tareas):
    nombre_a = input("Ingrese el nombre de la tarea: ")
    descripcion_a = input("Ingrese la descripción de la tarea: ") 
    if not nombre_a or not descripcion_a:
        print("\n El nombre y la descripción no pueden estar vacíos.")
        return
    tarea = {"nombre": nombre_a, "descripcion": descripcion_a, "completada": False}
    lista_de_tareas.append(tarea) 
    guardar_tareas(lista_de_tareas)
    print(f"\n✅ Tarea '{nombre_a}' agregada con éxito.")

def ver_tareas(lista_de_tareas):
    print("\n--- TUS TAREAS ---")
    if not lista_de_tareas: 
        print("No hay tareas pendientes. ¡Felicidades crack! 🎉")
    else:
        for i, tarea in enumerate(lista_de_tareas):
            estado = "✅ Completada" if tarea["completada"] else "⏳ Pendiente"
            print(f"{i + 1}. {tarea['nombre']} ({tarea['descripcion']}) - {estado}")
    print("------------------")

def marcar_completada(lista_de_tareas):
    ver_tareas(lista_de_tareas) #se reutiliza la funcion ver_tareas de acuerdo a la actividad
    if not lista_de_tareas:
        return
    try:
        num_tarea = int(input("\nIngrese el número de la tarea que desea marcar como completada: "))
        if 1 <= num_tarea <= len(lista_de_tareas):
            if lista_de_tareas[num_tarea - 1]["completada"]:
                print("\n❌ La tarea ya estaba marcada como completada.")
                return
            lista_de_tareas[num_tarea - 1]["completada"] = True
            guardar_tareas(lista_de_tareas) # se reutiliza la funcion guardar_tareas de acuerdo a la actividad
            print(f"\n✅ Tarea '{lista_de_tareas[num_tarea - 1]['nombre']}' marcada como completada.")
        else:
            print("\n❌ Número de tarea fuera de rango.")
    except ValueError:
        print("\n❌ Error: Debe ingresar un número válido.")

def eliminar_tarea(lista_de_tareas):
    ver_tareas(lista_de_tareas)
    if not lista_de_tareas:
        return
    try:
        num_tarea = int(input("\nIngrese el número de la tarea que desea eliminar: "))
        if 1 <= num_tarea <= len(lista_de_tareas):
            tarea_eliminada = lista_de_tareas.pop(num_tarea - 1)
            guardar_tareas(lista_de_tareas)
            print(f"\n🗑️ Tarea '{tarea_eliminada['nombre']}' eliminada con éxito.")
        else:
            print("\n❌ Número de tarea fuera de rango.")
    except ValueError:
        print("\n❌ Error: Debe ingresar un número válido.")

def main():
    tareas_en_memoria = cargar_tareas() #lista de diccionarios de tareas que estan el archivo tareas.json
    while True:
        menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_tarea(tareas_en_memoria)
        elif opcion == "2":
            ver_tareas(tareas_en_memoria)
        elif opcion == "3":
            marcar_completada(tareas_en_memoria)
        elif opcion == "4":
            eliminar_tarea(tareas_en_memoria)
        elif opcion == "5":
            break
        else:
            print("\n❌ Opción no válida. Por favor, elige una opción del 1 al 5.")            
    print("\n¡Hasta luego!")
if __name__ == "__main__": #hacer esto es una buena practica en python. Evita que el codigo se ejecute si el modulo no es el principal
    main()
