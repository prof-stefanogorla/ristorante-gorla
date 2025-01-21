class Piatto:
	def __init__(self, nome, prezzo, tipo, calorie):
		self.nome = nome
		self.prezzo = prezzo
		self.tipo = tipo
		self.calorie = calorie
		self.allergeni = []

	def aggiungi_allergene(self, allergene):
		if allergene not in self.allergeni:
			self.allergeni.append(allergene)
	
	def rimuovi_allergene(self, allergene):
		if allergene in self.allergeni:
			self.allergeni.remove(allergene)
	
	def mostra_allergeni(self):
		return ", ".join(self.allergeni) if self.allergeni else "Nessun allergene"
	
	def __str__(self):
		allergeni_str = f" | Allergeni: {self.mostra_allergeni()}" if self.allergeni else ""
		return f"{self.nome} ({self.tipo}) - {self.prezzo:.2f} Euro. {self.calorie} Allergeni: {allergeni_str}"  


class PiattoSpeciale(Piatto):
	def __init__(self, nome, prezzo, tipo, descrizione_speciale):
		super().__init__(nome, prezzo, tipo)
		self.descrizione_speciale = descrizione_speciale
	
	def __str__(self):
		base_str = super().__str__()
		return f"{base_str} | Speciale: {self.descrizione_speciale}"


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
