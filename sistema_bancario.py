menu = """
-------------MENU-----------------
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 1000
limite = 1000
extrato = "" #CRIADA PARA ARMAZENAR O HISTÓRICO DE TRANSAÇÕES (DEPÓSTISO E SAQUES) QUE SERÃO APRESENTADOS NO COMANDO EXTRATO.
numero_saques = 0 #CRIADA PARA ARMEZENAR QUANTOS SAQUES FORAM FEITOS
LIMITE_SAQUES = 3 #ESTABELECE O LIMITE NÃO DEIXANDO SER EFEITUADO MAIS SAQUES APÓS O LIMITE.

#LOOP PRINCIPAL > INICIO DO LOOPING INFINITO, ONDE CONTINUAMENTE EXIBE O MENU E ESPERA PELA ENTRADA DO USUÁRIO.
while True:

    opcao = input(menu) #CRIADA PARA INTERAGIR COM O USUÁRIO ONDE ELE FARÁ A ESCOLHA DA FUNÇÃO (DEPOSITAR, SACAR, EXTRATO OU SAIR)

    if opcao == "d": #VERIFICA SE O USUÁRIO ESCOLHEU A OPÇÃO, CASO POSITIVO, EXECUTA O BLOCO DE CÓDIGO CORRESPONDENTE
        valor = float(input("Informe o valor do depósito: ")) #VALOR QUE USUÁRIO DESEJA

        if valor > 0: #VERIFICA SE O VALOR DO DEPÓSITO É POSITIVO
            saldo += valor #SE FOR POSITVO O VALOR ACIMA, ENTÃO ELE É ADICIONADO AQUI
            extrato += f"Depósito: R$ {valor:.2f}\n" #AQUI É REGISTRADO
            print(f"Depósito de R$ {valor:.2f} efetuado com sucesso.") #TUDO OK SERÁ APRESENTADO A MENSAGEM DE QUE O VALOR FOI DEPOSITADO
            print(f"Saldo atual: R$ {saldo:.2f}.") #AQUI SERÁ EXIBIDO O SALDO ATUAL
        else:
            print("Operação falhou! O valor informado é inválido.") #CASO O VALOR INFORMADO SEJA NEGATIVO APRESENTARÁ ESSA MENSAGEM

    elif opcao == "s": #VERIFICA SE O USUÁRIO ESCOLHEU A OPÇÃO, CASO POSITIVO, EXECUTA O BLOCO DE CÓDIGO CORRESPONDENTE
        valor = float(input("Informe o valor do saque: "))

        #AQUI PRECISAMOS CRIAR ESSES PARÂMETROS PARA NOS CASOS ABAIXO PARA QUE CASO SEJA UM CASO FORA DO ESCOPO ELE SINALIZE.
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo: #SE O SALDO FOR INSUFICIENTE APRESENTA ESSA MENSAGEM
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite: #SE O VALOR DO SAQUE EXCEDER O LIMITE APRESENTA ESSA MENSAGEM
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques: #SE O NÚMERO DE SAQUES FOI ATINGIDO APRESENTA ESSA MENSAGEM
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor <= 0: #SE O VALOR DO SAQUE FOR INVÁLIDO (NEGATIVO OU ZERO), APRESENTA ESSA MENSAGEM
            print("Operação falhou! O valor informado é inválido.")
        else: #APÓS VERIFICAR TODAS AS AFIRMAÇÕES ACIMA FORAM BEM SUCEDIDAS
            saldo -= valor #SE TODAS AS VERIFICAÇÕES FORAM BEM SUCEDIDAS, ELE IRÁ SUBTRAIR
            extrato += f"Saque: R$ {valor:.2f}\n" #AQUI É REGISTRADO
            numero_saques += 1 #REGISTRA PRIMEIRO SAQUE EFEITUADO E ARMAZENA
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}.")

    elif opcao == "e": #VERIFICA SE O USUÁRIO ESCOLHEU A OPÇÃO, CASO POSITIVO, EXECUTA O BLOCO DE CÓDIGO CORRESPONDENTE
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato) #VERIFICA SE O EXTRATO ESTÁ VAZIO, SE ESTIVER APRESENTA ESSA MENSAGEM
        print(f"\nSaldo: R$ {saldo:.2f}") #APRESENTA TODAS AS TRANSAÇÕES REGISTRADAS
        print("==========================================")

    elif opcao == "q": #VERIFICA SE O USUÁRIO ESCOLHEU A OPÇÃO, CASO POSITIVO, EXECUTA O BLOCO DE CÓDIGO CORRESPONDENTE E ENVIA A MENSAGEM ABAIXO
       print("Obrigado por usar nossos serviços. Até breve!.")
       break #SAI DO LOOP INFINITO E ENCERRA O PROGRAMA
    
    else:#CASO NÃO SEJA DIGITADO (d, s, e ou q) O CÓDIGO ENVIA A MENSAGEM ABAIXO
        print("Operação inválida, por favor selecione novamente a operação desejada.")
