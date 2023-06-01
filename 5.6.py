class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    def filmar(self):
        if self.filmando: 
            print(f'{self.nome} JÀ está filmando...')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True 
    def desligar(self):
        if self.filmando: 
            self.filmando = False 
            print(f'{self.nome}  está desligada...')
            return
        print(f'{self.nome} a camera já estava desligada...')



c1 = Camera('Sony')
print(c1.nome)
c1.filmar()
c1.desligar()
c1.desligar()