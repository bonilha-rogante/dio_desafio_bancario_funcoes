# import textwrap

def menu():
    menu = '''
    ----------------------------
        MENU DE OPERAÇÕES

        [D] Depositar
        [S] Sacar
        [E] Extrato
        [U] Novo Usuário
        [C] Nova Conta
        [Q] Sair
    ----------------------------
    '''
    return input((menu)).upper()

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print(f'\nVocê realizou um depósito de R${valor:.2f}.\nSeu Saldo atual é de R${saldo:.2f}')
    else:
        print(f'\nVocê tentou depositar R${valor:.2f}.\nEsse valor é inválido. Por favor, faça um novo depósito.')

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques


    if excedeu_saldo:
        print(f'Você não possui saldo suficiente.')

    elif excedeu_limite:
        print(f'Você tentou realizar um saque maior do que seu limite.')

    elif excedeu_saques:
        print('Você já realizou todos os saques do dia.')
    
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R${valor:.2f}\n'
        numero_saques += 1
        print(f'Você realizou um saque de R$ {valor:.2f}.\nSeu saldo atual é R$ {saldo:.2f}')
    else:
        print('Valor informado inválido.')
        
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n================ EXTRATO ================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R${saldo:.2f}')
    print('='*30)

def criar_usuario(usuarios):
    cpf = input('Informe o CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)
     
    if usuario:
        print('CPF já cadastrado')
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe seu endereço (rua, nº - bairro - cidade/ estado): ')

    usuarios.append({'nome': nome, 'data_nascimento':data_nascimento, 'cpf':cpf, 'endereco':endereco})

    print('Usuário cadastrado com sucesso')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe seu CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(f'Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario':usuario}

    print('Usuário não encontrato')

def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    LIMITE_SAQUES = 3
    AGENCIA = '0001'


    while True:
        opcao = menu()

        if opcao == 'D':
            valor = float(input('Qual valor deseja depositar?\nR$ '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 'S':
            valor =  float(input('Você pode realizer até 3 saques no valor de R$500.00\nQual o valor que deseja sacar?\nR$ '))

            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)   

        elif opcao == 'E':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'U':
            criar_usuario(usuarios)

        elif opcao == 'C':
            # numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == 'S':
            break

        else: 
            print('Operação inválida, por favor selecione novamente a operação desejada.')

            
main()
