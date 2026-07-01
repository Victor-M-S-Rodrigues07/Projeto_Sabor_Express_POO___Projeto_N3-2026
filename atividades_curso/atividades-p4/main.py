# 8 - No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

from models.livro import Livro

def main():

    RWBB = Livro ("Vermelho, Branco e Sangue Azul", "Tahereh Mafi", 2015)
    Amor_e_Gelato = Livro ("Amor e Gelato", "Jenna Evans Welch", 2016)
    Til = Livro ("Til", "José de Alencar", 1872)
    As_Furias_Invisiveis_do_Coração = Livro ("As Fúrias Invisíveis do Coração", "John Boyne", 2017)
    Acre = Livro ("Acre", "Lucrecia Zappi", 2017)
    Me_Chame_Pelo_Seu_Nome = Livro ("Me Chame Pelo Seu Nome", "André Aciman", 2007)
    As_Mil_Partes_do_Meu_Coracao = Livro ("As Mil Partes do Meu Coração", "Jandy Nelson", 2014)
    O_Segredo_de_Helena = Livro ("O Segredo de Helena", "Lucinda Riley", 2019)

    print (RWBB)
    print (O_Segredo_de_Helena)


if "__name__" == "__main__":

    main()