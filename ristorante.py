class Piatto:
    def __init__(self, nome, prezzo, tipo):
        self.nome = nome
        self.prezzo = prezzo
        self.tipo = tipo

    def __str__(self):
        return f"{self.nome} ({self.tipo}) - {self.prezzo:.2f} Euro"
