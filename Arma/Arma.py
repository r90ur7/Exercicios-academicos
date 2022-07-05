class Arma:
    def __init__(self, tambor = 0, municao = 0):
     self.gatilho = False
     self.tambor = tambor
     self.trava = False
     self.municao = municao
    #gatilho =False
    #tambor = 0
    #trava = False
    #munição = 5
    def atirar(self):
     if self.trava == True :
         if self.tambor > 0:
             self.tambor = self.tambor - 1
         self.trava = False
         print("atirou")
         return True
     else:
         self.engatilhar()
    def engatilhar(self):
        self.trava = True
    def recarregar(self):
        self.tambor = 5
        self.municao = 0