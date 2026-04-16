from Cliente import Cliente
from criar_conta import Criar_conta
from Adicionar_conta import Adicionar_conta
from acessar_conta import Acessar_conta
import pandas as pd
import os
caminho_excel = "cliente_banco_Tabajara.xlsx"

print("================================================")
print("                 BANCO TABAJARA")
print("                 Escolha uma opção")
print("                 1 - Criar conta")
print("                 2 - Acessar conta")
print("================================================\n")

opcao = int(input("R: "))

if opcao == 1:
    nome_cliente = str(input("Nome completo: "))
    cpf = int(input("CPF: "))
    tipo_conta = str(input("Tipo da conta que deseja criar: "))

    df = pd.DataFrame()
    

    if os.path.exists(caminho_excel): #True
        print("Arquivo ja existe")
        df = pd.read_excel(caminho_excel)
        #Instaciando o adicionar conta
        adicionar = Adicionar_conta(nome_cliente, cpf, tipo_conta)
    
        #Chamando a funcao adicionar que esta dentro da classe Adicionar_conta
        novo_dado = adicionar.adicionar(df)
    
    else: #false
        print('Arquivo não existe')
    
    
        #Instancio para manipular  os dados adicionados pelo cliente
        conta = Criar_Conta(nome_cliente, cpf, tipo_conta)
    
        #Identifico o caminho do excel e chamo a funcao salvar_excel
        novo_dado = conta.salvar_excel(caminho_excel)
    
    
        #Concat para inserir uma nova linha no excel com os dados digitados pelo
    df = pd.concat([df, novo_dado], ignore_index=True)
    
    df.to_excel(caminho_excel, index=False)


elif opcao == 2:
    print("Opcao 2 selecionada")

    #Validar se o CPF informado e o numero_conta são os mesmos.
    numero_conta = int(input("Digite o número da conta: "))

    acesso = Acessar_conta(cpf, numero_conta)
    acesso.validar_banco(caminho_excel)