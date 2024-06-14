esquerda = int(input())
direita = int(input())
res = 0
if(esquerda>direita):
    res = esquerda+direita
else:
    res = (direita-esquerda)*2

print(res)