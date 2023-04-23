valor_1 = int(input())
valor_2 = int(input())
valor_3 = int(input())
valor_4 = int(input())
valor_5 = int(input())
par = 0

if valor_1 % 2 == 0:
    par += 1
if valor_2 % 2 == 0:
    par += 1
if valor_3 % 2 == 0:
    par += 1
if valor_4 % 2 == 0:
    par += 1
if valor_5 % 2 == 0:
    par += 1

print(f'{par} valores pares')
