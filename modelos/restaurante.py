from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []   # Atributo da classe

    def __init__ (self, nome, categoria):

        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []        # Lista porque vários clientes adicionam avaliações. Só se manipula depois, não na instanciação
        Restaurante.restaurantes.append (self)

    def __str__(self):

        return f"{self._nome} | {self._categoria}"
    

    @classmethod

    def listar_restaurantes (cls):

        print(f"{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}")

        for restaurante in cls.restaurantes:        # A classe tem o atributo lista de restaurantes

            print (f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")   # Não se puxa o self pois estamos pegando da lista


    @property

    def ativo (self):

        return "■" if self._ativo else "□"
    

    def alternar_estado (self):

        self._ativo = not self._ativo       # Not: inverte a lógica booleana

    def receber_avaliacao (self, cliente, nota):

        avaliacao = Avaliacao (cliente, nota)
        self._avaliacao.append (avaliacao)


    @property       
    
    # Ser capaz de ler para cada restaurante, É um atributo do restaurante, não uma ação, por isso o @property. Como é necessário ler a média, não pode ser uma função comum, pois ela não é chamada, é lida. Por isso o @property. Se fosse uma ação, seria uma função comum.

    def media_avaliacoes (self):

        if not self._avaliacao:

            return 0
        
        soma_das_notas = sum (avaliacao._nota for avaliacao in self._avaliacao) # Ternário de percursão da lista
        quantidade_de_notas = len (self._avaliacao)
        media = round (soma_das_notas / quantidade_de_notas, 1)

        return media