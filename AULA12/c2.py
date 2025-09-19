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



-------Outro exemplo
class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano
        
    def ligar(self):
        print(f"O carro {self.marca} está ligado."}
              
    def acelerar(self):
         print(f"O carro {self.marca} está acelerando."}

    ==Testando a classe==
carro1 = Carro("Toyota", 2020)
carro2 = Carro("Fiat", 2018)

carro1.ligar()
carro1.acelerar()

carro2.ligar()
carro2.acelerar()           
