class Avaliacao:

    def __init__ (self, cliente, nota):

        self._cliente = cliente
        self._nota = nota

        if nota > 5 or nota < 0:

            print ("Os valores das avaliações precisam estar entre 0 e 5. Desconsiderando nota")
            return None

        else:

            self._nota = nota