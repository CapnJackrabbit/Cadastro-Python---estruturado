
def valida_anac():
    while True:
            anac = input('INSIRA O CANAC: ')
            if anac.isdigit() == False:
                print('O CÓDIGO ANAC DEVE CONTER APENAS NÚMEROS (6)')
            elif len(anac) < 6:
                print('O CÓDIGO ANAC DEVE CONTER PELO MENOS 6 DÍGITOS!')
            elif len(anac) >6:
                print('O CÓDIGO ANAC DEVE CONTER NO MÁXIMO 6 DÍGIOS!')
            else:
                return anac
