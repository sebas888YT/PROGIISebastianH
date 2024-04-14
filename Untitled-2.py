class MenuPrincipal:
    def _init_(self):
        self.personas_submenu = SubMenuPersonas()

    def mostrar(self):
        while True:
            print("\nMENU PRINCIPAL")
            print("1. PERSONAS")
            print("2. UNIVERSIDADES")
            print("3. NOTAS")
            print("4. ASIGNATURA")
            print("5. SALIR")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.personas_submenu.mostrar()
            elif opcion == "2":
                print("Seleccionaste UNIVERSIDADES")
                # Aquí puedes implementar la lógica para la opción de UNIVERSIDADES
            elif opcion == "3":
                print("Seleccionaste NOTAS")
                # Aquí puedes implementar la lógica para la opción de NOTAS
            elif opcion == "4":
                print("Seleccionaste ASIGNATURA")
                # Aquí puedes implementar la lógica para la opción de ASIGNATURA
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")


class SubMenuPersonas:
    def _init_(self):
        self.personas = []

    def mostrar(self):
        while True:
            print("\nSUBMENU PERSONAS")
            print("1. CREAR PERSONA")
            print("2. LISTAR PERSONAS")
            print("3. ELIMINAR PERSONA")
            print("4. ATRAS")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.crear_persona()
            elif opcion == "2":
                self.listar_personas()
            elif opcion == "3":
                self.eliminar_persona()
            elif opcion == "4":
                print("Regresando al menú principal...")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción válida.")

    def crear_persona(self):
        nombre = input("Ingrese el nombre de la persona: ")
        self.personas.append(nombre)
        print("Persona creada correctamente.")

    def listar_personas(self):
        print("\nLISTADO DE PERSONAS:")
        for idx, persona in enumerate(self.personas, start=1):
            print(f"{idx}. {persona}")

    def eliminar_persona(self):
        self.listar_personas()
        idx = int(input("Ingrese el número de la persona a eliminar: ")) - 1
        if 0 <= idx < len(self.personas):
            del self.personas[idx]
            print("Persona eliminada correctamente.")
        else:
            print("Número de persona no válido.")


# Programa principal
if _name_ == "_main_":
    menu = MenuPrincipal()
    menu.mostrar()