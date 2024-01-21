menu = '''

[d]depositar
[s]sacar
[e]extrato
[q]sair

=> '''

saldo= 0
limite = 500
extrato = ""
numeros_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao= input(menu)
    if opcao == 'd':
        valor = float(input('Informe o valor do depósito:'))

        if valor > 0:
            saldo == valor
            extrato == f'Depósito R$: {valor:.2f}\n'

        else:
            print('Operação falhou, o valor inserido é inválido')


    elif opcao == 's':
        valor = float(input('Informe o valor do saque:'))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numeros_saque  > LIMITE_SAQUE

        if excedeu_saldo:
            print('Operação falhou: limite de saldo insulficiente')

        if excedeu_limite:
            print('Operação falhou: O valor do saldo excedeu o limite')

        if excedeu_saques:
            print('Operação falhou:Numero máximos de saques excedidos')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saques: R$ {valor:.2f}\n'
            numeros_saque += 1

        else:
            print('Operação falhou: O valor informados é inválido')

    elif opcao == 0:
        print('\n============EXTRATO============')
        print('Não foram realizadas movimentações' if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}')
        print('==================================')

    elif opcao =='q':
        break

    else:
        print('Operação invalida, por favor selecione novamente a operação desejada.')




