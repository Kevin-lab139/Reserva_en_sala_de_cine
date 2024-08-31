class Cine:
    def __init__(self):
        self.SALA = []  # Representación de la sala (se creará en la opción 1)
        self.RESERVAS = {}   # Diccionario para almacenar reservas (clave: asiento, valor: usuario)

    def crear_sala(self):
        num_filas = int(input("Ingrese el número de filas: "))
        num_columnas = int(input("Ingrese el número de columnas: "))
        self.num_asientos = num_filas * num_columnas
        self.SALA = [[str(i * num_columnas + j + 1) for j in range(num_columnas)] for i in range(num_filas)]
        print("Sala creada:")
        for fila in self.SALA:
            print(" ".join(fila))