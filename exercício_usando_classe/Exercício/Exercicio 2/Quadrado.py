class Quadrado:

    def __init__(self, tamanho_lado=0.0):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, valor_lado):
        self.tamanho_lado = float(valor_lado)

    def retornar_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        area = self.tamanho_lado**2
        return area
