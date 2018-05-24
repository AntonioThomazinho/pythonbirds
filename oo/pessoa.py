class Pessoa:
    def __init__(self, nome = None, idade=35):
        #Atributo antes do = Após a virgula temos um parametro ou uma variável
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Thomazinho')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    p.nome = 'Antonio'
    print(p.nome)
    print(p.idade)
