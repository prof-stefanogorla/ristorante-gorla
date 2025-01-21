class Piatto:
    def __init__(self, nome, prezzo, tipo):
        self.nome = nome
        self.prezzo = prezzo
        self.tipo = tipo

    def __str__(self):
        return f"{self.nome} ({self.tipo}) - {self.prezzo:.2f} Euro"
    
class Menu:
    def __init__(self):
        self.piatti = []

    def aggiungi_piatto(self, piatto):
        self.piatti.append(piatto)

    def mostra_menu(self):
        if not self.piatti:
            return "Il menu' e' vuoto."
        return "\n".join([str(piatto) for piatto in self.piatti])    
