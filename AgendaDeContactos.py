""" 
Para hacer una agenda de contactos necesitaria los siguientes parametros:

agregar
eliminar 
buscar
listar 
salir

 """

agenda = {} 

def agregar_contacto():
    
    nombre = input("Por favor ingresar su nombre completo: ")
    telefono = input("Ingrese su número de teléfono (sin espacios ni guiones): ")
    correoElectronico = input("Su correo Electronico: ")

    if nombre in agenda:
        print("⚠️ El Contacto ya existe en la agenda.")
    else:
        agenda[nombre] = {"Telefono": telefono, "CorreoElectronico": correoElectronico}
        print(f"✅ Contacto '{nombre}' agregado correctamente.\n")


def eliminar_contacto():
    nombreEliminar = input("Ingrese el nombre del usuario a eliminar: ")
    if nombreEliminar in agenda:
        del agenda[nombreEliminar]
        print(f"{nombreEliminar} fue eliminado correctamente.")
    else:
        print("⚠️ El contacto no existe.")

def buscar_contacto():
    nombreBuscar = input("Ingrese el nombre del usuario a eliminar: ")

    if nombreBuscar in agenda:

        print("¡Sí, este contacto se encuentra en la lista!")
    else:
        print("Contacto no encontrado, por favor ingresarlo")


def listar_contactos():

    if not agenda:
        print(" Lo siento contactos no encontrados, favor agregarlos")
    for nombre, datos in agenda.items():
        print(f"{nombre} - Tel: {datos['Telefono']} | Email: {datos['CorreoElectronico']}")

    


def mostrar_menu():
    print("Bienvenido a la agenda de contactos, dime con qué puedo ayudarte:")
    while True:
        print("\n")
        print("MENU AGENDA DE CONTACTOS:")
        print("-" * 30)
        print("""
        1. Agregar un contacto a la agenda
        2. Eliminar un contacto de la agenda
        3. Buscar un contacto
        4. Listar todos los contactos
        5. Salir
        """)
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion == 1:
                print("➡ Agregar contacto")
                agregar_contacto()
            elif opcion == 2:
                print("➡ Eliminar contacto")
                eliminar_contacto()
            elif opcion == 3:
                print("➡ Buscar contacto")
                buscar_contacto()
            elif opcion == 4:
                print("➡ Listar contactos")
                listar_contactos()
            elif opcion == 5:
                print("Saliendo de la agenda. ¡Hasta luego!")
                break
            else:
                print("⚠️ Opción no válida. Intenta de nuevo.")
        else:
            print("⚠️ Entrada no válida. Ingresa un número del 1 al 5.")


mostrar_menu()


