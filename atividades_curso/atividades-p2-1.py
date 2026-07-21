class Musica:

    def __init__ (self, nome, artista, duracao = 0):

        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):

        return f"{self.nome} - {self.artista} ({self.duracao} segundos)"


objeto_N1 = Musica ("Imagine", "John Lennon", (3 * 60) + 54)

objeto_N2 = Musica ("Hey Jude", "Paul McCartney", (8 * 60) + 10)

objeto_N3 = Musica ("Let It Be", "The Beatles", (4 * 60) + 5)

print (objeto_N1)
print (objeto_N2)
print (objeto_N3)



# 1) Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro:

    def __init__ (self, modelo, cor, ano):

        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__ (self):

        return f"Carro: {self.modelo} | {self.cor} | {self.ano}"

cedan = Carro ("Cedan", "Amarelo", 2017)

print (cedan)

# 2) Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:

    def __init__ (self, nome, categoria, localidade, n_estrelas = 0):

        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.n_estrelas = n_estrelas
        self.localidade = localidade

    def __str__(self):

        return f"{self.nome}: {self.categoria} | {self.ativo} | {self.n_estrelas} | {self.localidade}"
    
    # 4) Adicione um método especial str à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
    
    def __str__(self):

        return f"{self.nome}: {self.categoria}"
    
mc_donalds_mil = Restaurante ("MC Donalds", "Hamburguers", "Avenida Paulista", 4.78)
print (mc_donalds_mil)

# 3) Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
# Acabei fazendo isso no exercício Nº 2.
 
burguer_king = Restaurante ("Burguer King", "Hamburguers", "Avenida Paulista", 4.4)
print (burguer_king)


# 5) Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Cliente:

    def __init__ (self, nome, cpf, endereco, idade):

        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.idade = idade

    def __str__(self):

        return f"{self.nome}: {self.endereco}"
    
Luiz = Cliente ("Luiz", "999999999", "Rua Augusta, 45", 21)
print (Luiz)

Arthur = Cliente ("Arthur", "999999999", "Brooklyn", 20)
print (Arthur)

Kaua = Cliente ("Kauã", "999999999", "Jardim Ângela", 21)
print (Kaua)