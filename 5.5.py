class carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')

c1 = carro('fusca')
print(c1.nome)
c1.acelerar()

c2 = carro('ferrari')
c2.acelerar()