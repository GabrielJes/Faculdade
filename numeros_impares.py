#Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

#Entrada
#O arquivo de entrada contém 1 valor inteiro qualquer.

#Saída
#Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

x = int(input())
qtd = 0
inp = 1

while qtd < x :
    if x % 2 != 0 :
        print(inp)
        qtd += 1
        inp += 2
    else :
        print(inp)
        qtd += 1
        inp += 1
