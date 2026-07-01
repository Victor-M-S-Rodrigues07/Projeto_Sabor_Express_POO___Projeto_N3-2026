# 1 -Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

class Livro:

    lista_livros = []

    def __init__ (self, titulo = "", autor = "", ano_publicacao = 0):

        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponibilidade = True
        Livro.lista_livros.append (self)

# 2 - Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

    def __str__ (self):

        return f"{self._titulo.ljust(25)} | {self._autor.ljust(25)} | {str(self._ano_publicacao).ljust(25)} | {'Disponível' if self._disponibilidade else 'Indisponível'}" 

# 3 Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

    def emprestar_livro (self):

        self._disponibilidade = False

# 4 - Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

    @staticmethod

    def verificar_disponibilidade (ano):

        lista_livros_disponiveis = []

        for livro_iterador in Livro.lista_livros:

            if livro_iterador._ano_publicacao == ano:

                lista_livros_disponiveis.append(livro_iterador)

        print (f"Livros disponíveis em {ano}: {', '.join([f'{livro._titulo} - {livro._autor}' for livro in lista_livros_disponiveis]) if lista_livros_disponiveis else 'Nenhum livro disponível neste ano.'}")

    @classmethod

    def escolher_livro (cls, titulo):

        for livro_iterador in cls.lista_livros:

            if livro_iterador._titulo == titulo:

                return livro_iterador
            
        return "Livro não encontrado"

RWBB = Livro ("Vermelho, Branco e Sangue Azul", "Tahereh Mafi", 2015)
Amor_e_Gelato = Livro ("Amor e Gelato", "Jenna Evans Welch", 2016)
Til = Livro ("Til", "José de Alencar", 1872)
As_Furias_Invisiveis_do_Coração = Livro ("As Fúrias Invisíveis do Coração", "John Boyne", 2017)
Acre = Livro ("Acre", "Lucrecia Zappi", 2017)
Me_Chame_Pelo_Seu_Nome = Livro ("Me Chame Pelo Seu Nome", "André Aciman", 2007)
As_Mil_Partes_do_Meu_Coracao = Livro ("As Mil Partes do Meu Coração", "Jandy Nelson", 2014)
O_Segredo_de_Helena = Livro ("O Segredo de Helena", "Lucinda Riley", 2019)

RWBB.emprestar_livro()

print (RWBB)
print (Amor_e_Gelato)

Livro.verificar_disponibilidade (2017)