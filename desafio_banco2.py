from abc import ABC, abstractclassmethod, abstractproperty


class Cliente:
    def _init_(self,endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def _init_ (self,cpf,nome,data_nascimento, endereco):
        super()._init_(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def _init_ (self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero,cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self,valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        
        if excedeu_saldo:
            print ("\n=== Operação falhou! Saldo insuficiente na conta! ===")

        elif valor > 0:
            saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        
        else:
            print("\n=== Operação falhou! O valor informado é invállido. ===")
        
        return False
    
    def depositar(self, valor):
        saldo = self.saldo

        if valor > 0:
            saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        
        else:
            print("\n=== Operação falhou! O valor informado é invállido. ===")
            return False
        
        return True
        
class ContaCorrente(Conta):
    def _init_(self,numero, cliente, limite=1500, limite_saques=3):
        super._init_ (numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
            transacoes if transacaco ["tipo"] = Saque.
            _name_]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print ("\n=== Operação falhou! Valor excede o limite da conta! ===")
        
        elif excedeu_saques:
            print ("\n=== Operação falhou! Número de saques excedidos! ===")
        
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    
class Historico:

    def _init_ (self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo":transacao._class_._name_,
                "valor":transacao.valor,
            }
        )

class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self,conta):
        pass

class Saque(Transacao):
    def _init_(self,valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = Conta.sacar (self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def _init_(self,valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = Conta.depositar (self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)