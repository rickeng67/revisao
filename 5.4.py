class Pessoa:
    def __init__(self, nome , endereco , telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

p1 = Pessoa('luiz','Rua a','1111111')
print(p1.nome)
print(p1.telefone)

        