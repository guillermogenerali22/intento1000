from lib.CuentaBancaria import CuentaBancaria
from iu.Menu import Menu

class DawBank:
    def __init__(self) -> None:
        self.cuenta: CuentaBancaria = None

    def crear_cuenta(self) -> bool:
        iban: str = input("Introduce el IBAN: ")
        titular: str = input("Introduce el titular: ")
        while not CuentaBancaria(iban, titular, 0, 0).validar_iban(iban):
            print("IBAN no válido")
            iban = input("Introduce el IBAN correcto: ")
        while not CuentaBancaria(iban, titular, 0, 0).validar_nombre(titular):
            print("Nombre no válido")
            titular = input("Introduce el titular correcto: ")
        self.cuenta = CuentaBancaria(iban, titular, 0, 0)
        return True

    def ejecutar(self) -> None:
        while True:
            opcion: str = Menu.mostrar_menu()
            if opcion == "1":
                print(f"IBAN: {self.cuenta._iban}, Titular: {self.cuenta._titular}, Saldo: {self.cuenta._saldo}€")
            elif opcion == "2":
                print(f"IBAN: {self.cuenta._iban}")
            elif opcion == "3":
                print(f"Titular: {self.cuenta._titular}")
            elif opcion == "4":
                print(f"Saldo: {self.cuenta._saldo}€")
            elif opcion == "5":
                cantidad: int = int(input("Cantidad a ingresar: "))
                self.cuenta._ingreso = cantidad
                resultado: str | None = self.cuenta.ingresar()
                if resultado:
                    print(resultado)
                elif self.cuenta._saldo < 0:
                    aviso: str | bool = self.cuenta.comprobar_saldo()
                    print(aviso)
                print(f"Ingreso realizado. Saldo actual: {self.cuenta._saldo}€")
            elif opcion == "6":
                cantidad: int = int(input("Cantidad a retirar: "))
                self.cuenta._retirada = cantidad
                resultado: bool | None = self.cuenta.retirada()
                if resultado is False:
                    print("No se puede realizar la retirada.")
                elif self.cuenta._saldo < 0 > self.cuenta._saldo_min:
                    aviso: str | bool = self.cuenta.comprobar_saldo()
                    print(aviso)
                print(f"Retirada realizada. Saldo actual: {self.cuenta._saldo}€")
            elif opcion == "7":
                print(f"Movimientos: {self.cuenta.num_movimientos}")
            elif opcion == "8":
                self.cuenta.mostrar_historial()
            elif opcion == "9":
                print("Cerrando DawBank...")
                break
            else:
                print("Opción no válida, por favor elige otra vez.")

banco: DawBank = DawBank()
banco.crear_cuenta()
banco.ejecutar()
