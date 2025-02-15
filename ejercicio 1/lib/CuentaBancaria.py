import re

class CuentaBancaria:
    MAXIMO_INGRESO: int = 3000
    MAXIMO_NUM_MOV: int = 100
    SALDO_MIN: int = -50

    def __init__(self, iban: str, titular: str, ingreso: int, retirada: int, saldo: int = 0, num_movimientos: int = 0,
                 num_max_mov: int = MAXIMO_NUM_MOV, max_ingreso: int = MAXIMO_INGRESO, saldo_min: int = SALDO_MIN):
        self._iban: str = iban
        self._titular: str = titular
        self._saldo: int = saldo
        self._num_movimientos = num_movimientos
        self._ingreso = ingreso
        self._retirada = retirada
        self._num_max_mov: int = num_max_mov
        self._max_ingreso: int = max_ingreso
        self._saldo_min: int = saldo_min
        self._historial_movimientos: list[str] = []

    def __str__(self):
        return f"Su saldo es de: {self._saldo}€."

    def validar_iban(self, iban: str) -> bool:
        patron_iban = r"^[A-Z]{2}\d{22}$"
        patron = re.compile(patron_iban)
        return bool(patron.match(iban))

    def validar_nombre(self, nombre: str) -> bool:
        patron_titular = "^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+){1,2}$"
        patron = re.compile(patron_titular)
        return bool(patron.match(nombre))

    @property
    def iban(self) -> str:
        return self._iban

    @iban.setter
    def iban(self, iban: str) -> bool:
        if self.validar_iban(iban):
            self._iban = iban
        else:
            return False

    @property
    def titular(self) -> str:
        return self._titular

    @titular.setter
    def titular(self, titular: str) -> bool:
        if self.validar_nombre(titular):
            self._titular = titular
        else:
            return False

    @property
    def num_movimientos(self) -> int:
        return self._num_movimientos

    @num_movimientos.setter
    def num_movimientos(self, num_movimientos: int) -> str | None:
        if num_movimientos > self._num_max_mov:
            return "ERROR 3934E/ Número de movimientos excedido..."
        else:
            self._num_movimientos = num_movimientos

    def _registrar_movimiento(self, descripcion: str) -> None:
        if len(self._historial_movimientos) >= self._num_max_mov:
            self._historial_movimientos.pop(0)
        self._historial_movimientos.append(descripcion)

    def ingresar(self) -> None | str:
        if self._ingreso > 0 and self._ingreso <= self._max_ingreso:
            self._saldo += self._ingreso
            self._num_movimientos += 1
            self._registrar_movimiento(f"Ingreso de {self._ingreso}€. Saldo actual: {self._saldo}€.")
        elif self._ingreso >= self._max_ingreso:
            return "AVISO: Notificar a hacienda"
        else:
            return "Los ingresos no pueden ser negativos."

    def retirada(self) -> None | str | bool:
        if self._retirada > 0 and self._saldo - self._retirada >= self._saldo_min:
            self._saldo -= self._retirada
            self._num_movimientos += 1
            self._registrar_movimiento(f"Retirada de {self._retirada}€. Saldo actual: {self._saldo}€.")
        elif self._retirada > 0 and self._saldo - self._retirada < self._saldo_min:
            return False
        else:
            return False

    def comprobar_saldo(self) -> None | bool:
        if self._saldo > 0:
            return self._saldo
        elif self._saldo < 0 > self._saldo_min:
            return "AVISO: Saldo negativo"
        else:
            return False

    def mostrar_historial(self) -> None:
        print("Historial de movimientos:")
        for movimiento in self._historial_movimientos:
            print(movimiento)
