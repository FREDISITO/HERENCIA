from CUENTAAHORRO import CUENTAAHORRO
from CUENTACORRIENTE import CUENTACORRIENTE


class CuentaMixta(CUENTAAHORRO, CUENTACORRIENTE):
    def __init__(self, numero, nombre_propietario, saldo, interes, tieneChequera, limite:float=None, bono:float=None):
        CUENTAAHORRO.__init__(self, numero, nombre_propietario, saldo, interes)
        CUENTACORRIENTE.__init__(self, numero, nombre_propietario, saldo, tieneChequera)
        self._limite = limite
        self._bono = bono
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, cantidad):
        self._limite = cantidad

    @property
    def bono(self):
        return self._bono

    @bono.setter
    def bono(self, cantidad):
        self._bono = cantidad


#EJEMPLO DE USO
if __name__ == '__main__':
    cuenta_mixta = CuentaMixta(numero='0957808181', nombre_propietario='FREDDY CROVILL',saldo=7000, interes=0.05, tieneChequera=300, limite=20000, bono=2000)
    print("Saldo inicial de la cuenta mixta:", cuenta_mixta.saldo)
    print("Límite de la cuenta mixta:", cuenta_mixta._limite)
    print("Bono de la cuenta mixta:", cuenta_mixta._bono)

    cuenta_mixta.credito(500)
    print("Saldo después del depósito:", cuenta_mixta.saldo)

    cuenta_mixta.debito(1200)
    print("Saldo después del retiro:", cuenta_mixta.saldo)