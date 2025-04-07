from contacto import Contacto


class GestionContacto:
    def __init__(self):
        self.contactos = []
        self.cargar_contactos()

    def cargar_contactos(self):
        try:
            with open('contactos.txt', 'r') as file:
                for line in file:
                    nombre, telefono, email = line.strip().split(',')
                    contacto = Contacto(nombre, telefono, email)
                    self.contactos.append(contacto)
        except Exception as e:
            print(f"Error al cargar contactos: {e}")
    
    def agregar_contacto(self, contacto):
        try:
            with open('contactos.txt', 'a') as file:
                file.write(f"{contacto.nombre},{contacto.telefono},{contacto.email}\n")
            self.contactos.append(contacto)
        except Exception as e:
            print(f"Error al agregar contacto: {e}")
        
    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos guardados.")
        else:
            for contacto in self.contactos:
                print(contacto)
    def buscar_contacto(self, nombre):
        if not self.contactos:
            print("No hay contactos guardados.")
        else:
            for contacto in self.contactos:
                if contacto.nombre.lower() == nombre.lower():
                    print(contacto)
                    return
    def eliminar_contacto(self, nombre):
        try:
            self.contactos = [contacto for contacto in self.contactos if contacto.nombre.lower() != nombre.lower()]
            with open('contactos.txt', 'w') as file:
                for contacto in self.contactos:
                    file.write(f"{contacto.nombre},{contacto.telefono},{contacto.email}\n")
        except Exception as e:
            print(f"Error al eliminar contacto: {e}")

        
