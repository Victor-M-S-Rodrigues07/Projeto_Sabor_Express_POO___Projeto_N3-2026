# 1) Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

class ContaBancaria:

    def __init__ (self, titular = "", saldo = 0.0 ):

        self._titular = titular
        self._saldo = saldo
        self._ativo = False



# 2) Na classe ContaBancaria, adicione um método especial str que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

    def __str__ (self):

        return f"Titular: {self._titular} | Saldo: R${self._saldo:.2f}"
    

conta_maria = ContaBancaria ("Maria", 1717)
conta_joao = ContaBancaria ("João", 12380)

print (conta_maria)
print (conta_joao)



# 3) Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

class ContaBancaria:

# [...]

    def ativar_conta (self):

        self._ativo = True

    # 4) Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
    @property

    def titular (self):

        return self._titular
    
    @property

    def saldo (self):

        return self._saldo
    
    @property

    def ativo (self):

        return self._ativo

 
conta_joao = ContaBancaria ("João", 12380)
print (conta_joao)

conta_joao.ativar_conta()
print (conta_joao._ativo)



# 5) Crie uma instância da classe e imprima o valor da propriedade titular.

conta_maria = ContaBancaria ("Maria", 1717)
print (conta_maria.titular)



# 6) Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

class ClienteBanco:

    def __init__ (self, nome = "", cpf = "", genero = "", idade = int, salario = 0):

        self.nome = nome
        self._cpf = cpf
        self.genero = genero
        self._idade = idade
        self._salario = salario

    def __str__ (self):

        return f"Nome: {self.nome} | Idade: {self._idade} | Gênero: {self.genero} | CPF: {self._cpf} | Salário: R${self._salario}"
    
cliente_1 = ClienteBanco ("Maria", "123.456.789-00", "Feminino", 30, 5000)
cliente_2 = ClienteBanco ("João", "987.654.321-00", "Masculino", 40, 8000)
cliente_3 = ClienteBanco ("Ana", "456.789.123-00", "Feminino", 25, 3000)

print (cliente_1)
print (cliente_2)
print (cliente_3)



# 7) Crie um método de classe para a conta ClienteBanco.


class ContaBancaria:

# [...]

    @classmethod

    def criar_conta (cls, nome, cpf):

        conta = ContaBancaria (nome, cpf)
        
        
cliente_4 = ClienteBanco ("Roberto", "456.788.234-45", "Masculino", 76, 1230)
cliente_4.criar_conta("Roberto", "456.788.234-45")
print (cliente_4)