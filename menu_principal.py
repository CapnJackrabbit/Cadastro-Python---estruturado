import os,procura_nome,apaga_nome,cadastra_novo,alterar,sys



while True:
    print('CADASTRO DE ASSOCIADO \n')
    print('1- CADASTRAR NOVO')
    print('2- PROCURAR ASSOCIADO')
    print('3- ABRIR ARQUIVO')
    print('4- APAGAR ASSOCIADO')
    print('5- ALTERAR DADOS DE ASSOCIADO')
    print('6- SAIR')
    print()
    opc = input('SELECIONE UMA OPÇÃO: ')
    if opc == '1':
        cadastra_novo.cadastra_novo()


    elif opc == '2':
        if procura_nome.procura_nome() == '0':
            cprint('NOME NÃO ENCONTRADO','red')


    elif opc == '3':
        with open('outputfile.txt','r') as arquivo:
            filesize = os.path.getsize ("outputfile.txt")
            if filesize > 2:
                for elemento in arquivo:
                    print(elemento)
            else:
                print('O ARQUIVO ESTÁ VAZIO!\n')

    elif opc == '4':
        apaga_nome.apaga_nome()

    elif opc == '5':
        alterar.alterar()

    elif opc == '6':
        print('SAIR')
        break
