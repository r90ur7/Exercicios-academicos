
class Animais:
    
    def __init__(self, cobertura=None, alimento=None, patas=None, habitat=None, nome=None):
            self.cobertura = cobertura
            self.nome = nome
            self.alimento = alimento
            self.patas = patas
            self.habitat = habitat
            
    def dar_nome(self,nome):
        self.nome = nome
        
    def trocar(self, cobertura):
            self.cobertura = cobertura
            
class Cachorros(Animais):
    def trocar(self):
        self.cobertura = 'luiza'

class Circulos:
    raio = 25.4

    def calcula_Area(self):
        self.area = 3.14*(self.raio**2)
        
    def calcula_Volume(self,altura):
        self.volume = 3.14*(self.raio**2)*altura