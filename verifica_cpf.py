def verifica_cpf(cpf):
    cpf.isdigit ()
    if cpf.isdigit () == False:
        print ('CPF deve conter apenas múmeros')
    else:
        n1 = int (cpf[0])
        n2 = int (cpf[1])
        n3 = int (cpf[2])
        n4 = int (cpf[3])
        n5 = int (cpf[4])
        n6 = int (cpf[5])
        n7 = int (cpf[6])
        n8 = int (cpf[7])
        n9 = int (cpf[8])
        v1 = int (cpf[9])
        v2 = int (cpf[10])
        print (n1, n2, n3, n4, n5, n6, n7, n8, n9,v1,v2)


        def calcula_9(n1, n2, n3, n4, n5, n6, n7, n8, n9):
            c1 = n1 * 10
            c2 = n2 * 9
            c3 = n3 * 8
            c4 = n4 * 7
            c5 = n5 * 6
            c6 = n6 * 5
            c7 = n7 * 4
            c8 = n8 * 3
            c9 = n9 * 2
            somaC = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9
            return somaC


        soma9 = (calcula_9(n1, n2, n3, n4, n5, n6, n7, n8, n9) * 10) % 11
        if (soma9 == 10):
            soma9 = 0


        def calcula_10(n1, n2, n3, n4, n5, n6, n7, n8, n9, soma9):
            c1 = n1 * 11
            c2 = n2 * 10
            c3 = n3 * 9
            c4 = n4 * 8
            c5 = n5 * 7
            c6 = n6 * 6
            c7 = n7 * 5
            c8 = n8 * 4
            c9 = n9 * 3
            c10 = soma9 * 2
            somaC10 = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10
            return somaC10
        soma10 = (calcula_10(n1, n2, n3, n4, n5, n6, n7, n8, n9, soma9) * 10) % 11
        if v1 == soma9 and v2 == soma10:
            return '1'
        else:
            print('ERRO')
