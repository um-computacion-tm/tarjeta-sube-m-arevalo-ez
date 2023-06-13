class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

class Sube:
    def __init__(self):
        self.saldo = 1000
        self.grupo_beneficiario = None
        self.estado = ACTIVADO

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == PRIMARIO:
            return 35
        else:
            return PRECIO_TICKET

    def pagar_pasaje(self):
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException("El usuario está desactivado.")

        if self.saldo < self.obtener_precio_ticket():
            raise NoHaySaldoException("No hay saldo suficiente para pagar el pasaje.")

        self.saldo -= self.obtener_precio_ticket()

    def cambiar_estado(self, estado):
        if estado not in [ACTIVADO, DESACTIVADO]:
            raise EstadoNoExistenteException("El estado proporcionado no existe.")

        self.estado = estado

if __name__ == '__main__':
    main()