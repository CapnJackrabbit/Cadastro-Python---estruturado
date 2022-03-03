import os,json

def procura_nome():
    flag = '0'
    with open('outputfile.txt', 'r') as arquivo:
        filesize = os.path.getsize ("outputfile.txt")
        if filesize > 2:
            nome = (input('DIGITE O NOME QUE PROCURA '))
            dados = json.load (arquivo)
            for associado in dados:
                if nome in associado['NOME']:
                    print('\nNOME ENCONTRADO' + '\n' + 'NOME: ' + associado['NOME'] + '\n' + 'CPF: ' + associado['CPF'] + '\n' + 'ENDEREÇO: ' + associado['ENDEREÇO'] + '\n' + 'CANAC: ' + associado['CANAC'] + '\n')
                    flag = '1'
            return flag
        else:
            print('ARQUIVO VAZIO\n')
    arquivo.close()