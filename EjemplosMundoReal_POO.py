# archivo: sistema_reservas.py

class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservada = False

    def reservar(self):
        if not self.reservada:
            self.reservada = True
            print(f"Habitación {self.numero} reservada.")
        else:
            print(f"Habitación {self.numero} ya está reservada.")

    def liberar(self):
        self.reservada = False
        print(f"Habitación {self.numero} liberada.")


class Cliente:
    def __init__(self, nombre, documento_identidad):
        self.nombre = nombre
        self.documento_identidad = documento_identidad

    def __str__(self):
        return f"{self.nombre} ({self.documento_identidad})"


class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias
        self.total = habitacion.precio * dias

    def realizar_reserva(self):
        print(f"Reserva realizada para {self.cliente}.")
        self.habitacion.reservar()
        print(f"Total a pagar: ${self.total}")


# Crear algunas instancias y probar
habitacion1 = Habitacion(101, "Individual", 100)
cliente1 = Cliente("Juan Pérez", "12345678")
reserva1 = Reserva(cliente1, habitacion1, 3)

reserva1.realizar_reserva()
