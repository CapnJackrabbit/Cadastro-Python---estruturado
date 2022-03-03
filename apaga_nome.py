import os,json,procura_cpf

def apaga_nome():
    with open ('outputfile.txt', 'r+') as arquivo:
        filesize = os.path.getsize ("outputfile.txt")
        if filesize > 2:
            dados = json.load (arquivo)
            cpf = input('INFORME O CPF QUE DESEJA EXCLUIR: ')
            for associado in dados:
                if cpf in associado['CPF']:
                    print ('CPF ENCONTRADO: ' + associado['NOME'] + '\n\n')
                    print ('TEM CERTEZA QUE DESEJA EXCLUIR O ASSOCIADO ', associado['NOME'], '?' + '\n')
                    resp=input('S/N\n').upper()
                    if resp == 'S':
                        pos = dados.index(associado)
                        print(pos)
                        del dados[pos]
                        print (dados)
                        with open ('outputfile.txt', 'w') as arquivo:
                            json.dump (dados, arquivo)
                            arquivo.close ()
                    elif resp == 'N':
                        break
                elif procura_cpf.procura_cpf(cpf) == '0':
                    print('CPF NÃO ENCONTRADO')
                    break
        else:
            print('O ARQUIVO ESTÁ VAZIO\n')
