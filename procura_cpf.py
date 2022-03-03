import os,json

def procura_cpf(cpf):
    with open('outputfile.txt','r') as arquivo:
        filesize = os.path.getsize ("outputfile.txt")
        if filesize > 2:
            temp_cpf = json.load(arquivo)
            flag = '0'
            for elemento in temp_cpf:
                if cpf == elemento['CPF']:
                    flag = '1'
                    break
            return flag
