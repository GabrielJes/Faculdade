from time import sleep
entrada = int(input())
qntd = 0
qtd = 0
while qtd < 10:
    tabuada = entrada * qntd
    qtd += 1
    print(f'{entrada} x {qtd} = {entrada * qtd}')
    sleep (1)