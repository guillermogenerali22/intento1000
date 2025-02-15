class Menu:
    @staticmethod
    def mostrar_menu():
        print("\n--- Menú Principal ---")
        print("1. Datos de la cuenta")
        print("2. IBAN")
        print("3. Titular")
        print("4. Saldo")
        print("5. Ingreso")
        print("6. Retirada")
        print("7. Movimientos")
        print("8. Historial de movimientos")
        print("9. Salir")
        return input("Elige una opción: ")
