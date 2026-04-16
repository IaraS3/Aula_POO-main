class Cliente:
    def __init__(self, nome_cliente, cpf, tipo_conta, numero_conta=0, agencia = 400, extrato_bancario =0):
        self.nome_cliente = nome_cliente      
        self.cpf = cpf
        self.tipo_conta = tipo_conta
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.extrato_bancario = extrato_bancario

    def __str__(self):
        return f"Nome: {self.nome_cliente} | CPF: {self.cpf} | Tipo Conta: {self.tipo_conta} | Numero Conta: {self.numero_conta} | Agencia: {self.agencia} | Extrato: {self.extrato_bancario}"

    #Metodo
    def dicionario_cliente(self):
        return {chave: [valor] for chave , valor in self.__dict__.items()}  # o dict pega o objeto e transforma em dicionario