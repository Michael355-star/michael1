class Amor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.corazon = "??"
        self.sentimientos = []

    def expresar_amor(self):
        mensaje = f"{self.corazon} Para ti, {self.nombre}, mi amor es infinito."
        return mensaje

    def agregar_sentimiento(self, sentimiento):
        self.sentimientos.append(sentimiento)

    def mostrar_sentimientos(self):
        return f"Sentimientos por {self.nombre}: " + ", ".join(self.sentimientos)


# Crear una instancia de amor
mi_amor = Amor("Mi persona especial")

# Expresar amor
print(mi_amor.expresar_amor())

# Agregar sentimientos
mi_amor.agregar_sentimiento("cariño")
mi_amor.agregar_sentimiento("ternura")
mi_amor.agregar_sentimiento("pasión")

# Mostrar sentimientos
print(mi_amor.mostrar_sentimientos())
