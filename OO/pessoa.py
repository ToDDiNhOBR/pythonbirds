class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    toddinho = Pessoa(nome='ToDDiNhOBR')
    pedro = Pessoa(toddinho, nome='Pedro')
    print(Pessoa.cumprimentar(pedro))
    print(id(pedro))
    print(pedro.cumprimentar())
    print(pedro.nome)
    print(pedro.idade)
    for filho in pedro.filhos:
        print(filho.nome)
    print(pedro.filhos)
    pedro.sobrenome = 'Resende'
    del pedro.filhos
    pedro.olhos = 1
    del pedro.olhos
    print(pedro.sobrenome)
    print(pedro.__dict__)
    print(toddinho.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(pedro.olhos)
    print(toddinho.olhos)
    print(id(Pessoa.olhos), id(pedro.olhos), id(toddinho.olhos))





