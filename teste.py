import json

def alterar():
    with open ("outputfile.txt","r") as arquivo:
        dados = json.load(arquivo)
        cpf = input("Informe o CPF do associado que deseja alterar: ")
        for associado in dados:
            if cpf in associado['CPF']:
                print ('CPF ENCONTRADO' + '\n' + associado['NOME'])
                print ('TEM CERTEZA QUE DESEJA ALTERAR OS DADOS DO ASSOCIADO ', associado['NOME'], '?')
                resp=input('S/N\n').upper()
                if resp == 'S':
                    alt_dado = input('QUAL DADO?  N- NOME | E- ENDERECO | C- CODIGO ANAC').upper()
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
                else:
                    break
            else:
                print('CPF NÃO ENCONTRADO')
                break
