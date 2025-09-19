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


