# 5 - Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

from livro import Livro

# 6 - No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

livro_escolhido = Livro.escolher_livro("Acre")

print ("Livro disponível: ", livro_escolhido)

livro_escolhido.emprestar_livro()

print ("Livro disponível: ", livro_escolhido)

# 7 - No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

Livro.verificar_disponibilidade(2014)