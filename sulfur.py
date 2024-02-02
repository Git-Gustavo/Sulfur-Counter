#Recurso

sulfur = 1
polvora = sulfur * 2
explosivo =  sulfur * 10 + polvora * 50
escolha = 0

#Itens

rocket = explosivo * 10 + polvora * 150
c4 = explosivo * 20
bala = polvora * 10 + sulfur * 5
#Loop
while True:
    #Escolha
    print('\n1 --> C4 \n2 --> Rocket \n3 --> Bala Explosiva \n4 --> Sair\n')

    escolha_n = int(input('\nDigite o numero do que deseja: ')) + escolha
    if escolha_n == 4:
        break
    #Quantidade
    if escolha_n == 1:
        quantidade_c4 = int(input('\nQual a quantidade de C4 desejada ? '))
        total_sulfur_1 = quantidade_c4 * c4
        print('\n A quantidade de sulfur necessaria sera de: {}'.format(total_sulfur_1))
    elif escolha_n == 2:
        quantidade_rocket = int(input('\nQual a quantidade de Rocket desejada ? '))
        total_sulfur_2 = quantidade_rocket * rocket
        print('\nA quantidade de sulfur necessaria sera de: {}'.format(total_sulfur_2))
    elif escolha_n == 3:
        quantidade_bala = int(input('\nQual a quantidade de Balas Explosivas que deseja ? '))
        total_sulfur_3 = quantidade_bala * bala
        print('\nA quantidade de sulfur necessaria sera de: {}'.format(total_sulfur_3))

    else:
        print('\nTente novamente\n')
