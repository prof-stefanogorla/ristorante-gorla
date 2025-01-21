class Piatto:
    def __init__(self, nome, prezzo, tipo, calorie):
        self.nome = nome
        self.prezzo = prezzo
        self.tipo = tipo
        self.calorie = calorie

    def __str__(self):
        return f"{self.nome} ({self.tipo}) - {self.prezzo:.2f} Euro. {self.calorie} cal"
    
class Menu:
    def __init__(self):
        self.piatti = []

    def aggiungi_piatto(self, piatto):
        self.piatti.append(piatto)

    def mostra_menu(self):
        if not self.piatti:
            return "Il menu' e' vuoto."
        return "\n".join([str(piatto) for piatto in self.piatti])    

class Ristorante:
	def __init__(self, nome):
		self.nome = nome
		self.menu = Menu()
	
	def avvia(self):
		while True:
			print(f"\nBenvenuto al ristorante {self.nome}")
			print("2. Mostra il menu'")
			print("3. Esci")
	
			scelta = input("Scegli un'opzione: ")
			if scelta == "1":
				self.aggiungi_piatto()
			elif scelta == "2":
				print(self.menu.mostra_menu())
			elif scelta == "3":
				break
			else:
				print("Opzione non valida.")
	
	def aggiungi_piatto(self):
		nome = input("Inserisci il nome del piatto: ")
		prezzo = float(input("Inserisci il prezzo: "))
		tipo = input("Inserisci il tipo: ")
		calorie = input("Inserisci le calorie: ")
		self.menu.aggiungi_piatto(Piatto(nome, prezzo, tipo, calorie))
