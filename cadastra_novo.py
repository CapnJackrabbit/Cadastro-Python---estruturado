import procura_cpf,verifica_cpf,valida_anac,os,json

def cadastra_novo():
    print('NOVO ASSOCIADO\n')
    nome = input('INSIRA O NOME: ')
    ende = input('INSIRA O ENDEREÇO: ')
    while True:
        cpf = input('INSIRA O CPF: ')
        if len(cpf) < 11:
            print('O CPF DEVE CONTER PELO MENOS 11 DÍGITOS')
        else:
            if procura_cpf.procura_cpf(cpf) == '1':
                print('JÁ EXISTE UM ASSOCIADO COM O CPF CADASTRADO')
            else:
                check = verifica_cpf.verifica_cpf(cpf)
                if check == '1':
                    break
                else:
                    print('CPF INVÁLIDO! \n')
    anac = valida_anac.valida_anac()
    dados = []
    with open('outputfile.txt','r') as arquivo:
        filesize = os.path.getsize ("outputfile.txt")
        if filesize > 0:
            dados = json.load (arquivo)
    temp = {'NOME':nome,'ENDEREÇO':ende,'CPF':cpf,'CANAC':anac}
    dados.append(temp)
    with open ('outputfile.txt', 'w') as arquivo:
        json.dump(dados,arquivo)
        arquivo.close ()
