import os,json,procura_cpf,valida_anac

def alterar():
    with open ('outputfile.txt', 'r+') as arquivo:
        filesize = os.path.getsize ("outputfile.txt")
        if filesize > 2:
            dados = json.load (arquivo)
            cpf = input('INFORME O CPF DO ASSOCIADO QUE DESEJA ALTERAR: ')
            for associado in dados:
                if cpf in associado['CPF']:
                    print ('CPF ENCONTRADO: ' + associado['NOME'])
                    print ('\nTEM CERTEZA QUE DESEJA ALTERAR OS DADOS DE {}'.format(associado['NOME']), '?')
                    resp=input('S/N\n').upper()
                    if resp == 'S':
                        alt_dado = input('QUAL DADO?  N- NOME | E- ENDERECO | C- CODIGO ANAC \n').upper()
                        if alt_dado == 'N':
                            novo_nome = input("INFORME O NOVO NOME: ")
                            associado['NOME'] = novo_nome
                            print(dados)
                            with open ('outputfile.txt','r+') as arquivo:
                                json.dump(dados,arquivo)
                                arquivo.close()
                                break
                        elif alt_dado == 'E':
                            novo_end = input('INFORME O NOVO ENDEREÇO: ')
                            associado['ENDEREÇO'] = novo_end
                            print (dados)
                            with open ('outputfile.txt','r+') as arquivo:
                                json.dump(dados,arquivo)
                                arquivo.close()
                        elif alt_dado == 'C':
                            novo_anac = valida_anac.valida_anac()
                            associado['CANAC'] = novo_anac
                            print (dados)
                            with open ('outputfile.txt','r+') as arquivo:
                                json.dump(dados,arquivo)
                                arquivo.close()
                    elif resp == 'N':
                        break
                elif procura_cpf.procura_cpf(cpf) == '0':
                    print('CPF NÃO ENCONTRADO')
                    break
        else:
            print('O ARQUIVO ESTÁ VAZIO\n')