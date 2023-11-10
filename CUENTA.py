from abc import ABC, abstractmethod

#FREDDY DARWIN CROFFORD VILLAO
class CUENTA(ABC):
    def __init__(self, numero: str = None, nombrePropietario: str = None, saldo: float = None):
        self._numero = numero
        self._nombrePropietario = nombrePropietario
        self._saldo = saldo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, numero):
        self._numero = numero

    @property
    def nombrePropietario(self):
        return self._nombrePropietario

    @nombrePropietario.setter
    def nombrePropietario(self, nombre):
        self._nombrePropietario = nombre

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo_saldo):
        self._saldo = nuevo_saldo

    @abstractmethod
    def credito(self, cantidad):
        pass

    @abstractmethod
    def debito(self, cantidad):
        pass

    def mostrar_saldo(self):
        print(f"Saldo de la cuenta {self.numero}: ${self.saldo}")