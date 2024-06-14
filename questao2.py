notaC = 0
candidatos,aprovados = input().split(" ")
candidatos = int(candidatos)
aprovados = int(aprovados)
notas = input().split(" ")
posicao = 0
c = 0
while(c<candidatos):
    i = (candidatos-1)-c

    while(i>=0):
        notas[i] = int(notas[i])
        
        if(i == (candidatos-1)-c):
            maior = notas[i]
            posicao = i
        else:
            if(notas[i]>maior):
                maior = notas[i]
                posicao = i
        
        i = i - 1

    if(c == aprovados-1):
        notaC = notas[posicao]
        c = c+candidatos

    a = notas[(candidatos-1)-c]
    notas[(candidatos-1)-c] =  notas[posicao]
    notas[posicao] = a
    c = c+1

print(notaC)


