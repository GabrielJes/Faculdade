def bissexto(valor1):
    if valor1 % 4 == 0 and valor1 % 100 != 0:
        valor1 = True
        return valor1
    else:
        valor1 % 4 != 0 and valor1 % 100 == 0
        valor1 = False
        return valor1
    
n1 = int(input())
n2 = int(input())
qtd = 0
ano = bissexto(n1)

while n1 <= n2:
    n1 += 1
    ano = ano
    while ano == True:
        qtd += 1
    print(n1)
print(ano)





    







    


