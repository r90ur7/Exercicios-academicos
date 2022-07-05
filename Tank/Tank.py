'''
propriedades
============
Position: onde está o tanque?
Direction: para qual direção o tanque está?
Speed: qual velocidade?
Armor: qual é o nível de blindagem?
Ammo: quantos projéteis ele tem?

ações
=====
Move: mover o tanque para frente.
Turn: girar o tanque para a esquerda ou para a direita.
Fire: lançar projétil.
Hit: essa é a ação executada quando um projétil do inimigo
    atingir o tanque.
Explode: substitui o tanque por uma animação de explosão.
'''

class Tank:

    #método construtor
    def __init__(self,name):
        # atributos 
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 60

    def __str__(self):
        if self.alive:
            return f"{self.name}{(self.armor)} armor, {self.ammo} shells"
        else:
            return f"{self.name} (DEAD)"

    def fire(self, enemy):
        if self.ammo >= 1 :
            self.ammo -= 1
            print(f"{self.name} fire on {enemy}")
            enemy.hit()
        else:
            print(f"{self.name} has no  shells")

    def hit(self):
        self.armor -= 20
        print(f"{self.name} is hit")
        if self.armor <= 0 :
            self.explode()

    def explode(self):
        self.alive = False
        print(f"{self.name} explodes!")
     
