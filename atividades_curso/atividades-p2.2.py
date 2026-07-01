class Pessoa:

    def __init__ (self, nome = "", idade = 0, profissao = ""):

        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__ (self):

        return f"Nome: {self._nome} | Idade: {self._idade} | Ocupação: {self._profissao}"
    

    @property

    def saudacao (self):

        print (f"Olá! Seja bem-vinda {self._nome}. Sua profissão é {self._profissao}") if self._profissao else print (f"Olá! Seja bem-vinda {self._nome}!")

    def fazer_aniversario (self):

        self._idade += 1

    
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.fazer_aniversario()
pessoa3.fazer_aniversario()

print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)