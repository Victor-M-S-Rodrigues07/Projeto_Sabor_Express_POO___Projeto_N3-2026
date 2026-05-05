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