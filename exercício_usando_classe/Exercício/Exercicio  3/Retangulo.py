class Retangulo:

    def __init__(self, comprimento=0, largura=0):
        self.Comprimento = comprimento
        self.Largura = largura

    def ChangeValues(self, comprimento, largura):
        self.Comprimento = comprimento
        self.Largura = largura

    def GetValues(self):
        resultList = []
        resultList.append(self.Comprimento)
        resultList.append(self.Largura)
        return resultList

    def CalcArea(self):
        return float(self.Comprimento * self.Largura)

    def CalcPerimetro(self):
        return float(2 * (self.Comprimento + self.Largura))

    def calcular_quantidade_piso(self):
        pass