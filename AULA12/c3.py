"""class Animal:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.sexo = idade

    def comer(self):
        print(f'{self.nome} está comendo...')

an1 = Animal('Girafa', "50kg", "5anos")
an2 = Animal('Gato', '5kg', '3 meses')
an3 = Animal('Leão', '105kg', '10 anos')


print("Animal:", an1.nome, "\peso:", an1.peso , "\Sexo:", an1.sexo)
print("Animal:", an2.nome, "\peso:", an2.peso , "\Sexo:", an2.sexo)
print("Animal:", an3.nome, "\peso:", an3.peso , "\Sexo:", an3.sexo)

an1 = Animal('Girafa')
print("Nome:", an1.nome)
an1.comer()"""

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')
        
fusca = Carro('Fusca')
print("Nome:", fusca.nome)
fusca.acelerar()

byd =  Carro('BYD')
print("Nome:", byd.nome)
byd.acelerar()
#print(p2.nome)
