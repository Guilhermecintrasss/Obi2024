placa = input()
digitos = ['1','2','3','4','5','6','7','8','9','0','-']
letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
resp = 0
falsificada = False
if(len(placa)== 7):
    i = 0
    while(i<7):
        c = 0
        erros = 0
        if(i<3):
            while(c<len(letras)):
                if(placa[i] != letras[c]):
                    erros = erros+1
                c = c+1

            if(erros == len(letras)):
                i = i+len(placa)
                falsificada = True

        elif(i == 3):
            while(c<len(digitos)):
                if(placa[i] != digitos[c]):
                    erros = erros+1
                c = c+1

            if(erros == len(digitos)):
                i = i+len(placa)
                falsificada = True
        elif(i == 4):
            while(c<len(letras)):
                if(placa[i] != letras[c]):
                    erros = erros+1
                c = c+1

            if(erros == len(letras)):
                i = i+len(placa)
                falsificada = True
        else:
            while(c<len(digitos)):
                if(placa[i] != digitos[c]):
                    erros = erros+1
                c = c+1

            if(erros == len(digitos)):
                i = i+len(placa)
                falsificada = True

        if(falsificada == False):
            resp = 2
        else:
            resp = 0
        i = i+1

elif(len(placa) == 8):
    i = 0

    while(i<8):
        c = 0
        erros = 0
        if(i<3):
            while(c<len(letras)):
                if(placa[i] != letras[c]):
                    erros = erros+1
                c = c+1

            if(erros == len(letras)):
                i = i+len(placa)
                falsificada = True

        elif(i == 3):

            if(placa[i] != '-'):
                erros = erros+1


            if(erros == 1):
                i = i+len(placa)
                falsificada = True
                
        else:
            while(c<len(digitos)):
                if(placa[i] != digitos[c]):
                    erros = erros+1
                c = c+1

            if(erros == len(digitos)):
                i = i+len(placa)
                falsificada = True

        if(falsificada == False):
            resp = 1
        else:
            resp = 0
        i = i+1

else:
    resp = 0

print(resp)