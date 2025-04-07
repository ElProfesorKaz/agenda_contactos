from gestion_contactos import GestionContacto
from contacto import Contacto
import re

def validar_email(email):
    """Valida que el correo electrónico contenga un '@'."""
    return '@' in email

def mostrar_menu():
    print("\n--- Menú de Agenda de Contactos ---")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

def main():
    gestion = GestionContacto()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Agregar contacto
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            email = ""
            while not validar_email(email):
                # Validar el correo electrónico
                email = input("Ingrese el correo electrónico: ")
                
                if not validar_email(email):
                    print("Correo electrónico inválido. Debe contener un '@'. Intente nuevamente.")
                    
            contacto = Contacto(nombre, telefono, email)
            gestion.agregar_contacto(contacto)
            print("Contacto agregado exitosamente.")
        
        elif opcion == "2":
            # Mostrar contactos
            print("\n--- Lista de Contactos ---")
            gestion.mostrar_contactos()
        
        elif opcion == "3":
            # Buscar contacto
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            print("\n--- Resultado de la búsqueda ---")
            gestion.buscar_contacto(nombre)
        
        elif opcion == "4":
            # Eliminar contacto
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            gestion.eliminar_contacto(nombre)
        
        elif opcion == "5":
            # Salir
            print("Saliendo de la aplicación. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()