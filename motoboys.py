moto1 = {'Loja': "", 'Pedidos': 0, 'Valor da entrega': 0, 'Ganho do motoboy': 0}

moto2 = {'Loja': "", 'Pedidos': 0, 'Valor da entrega': 0, 'Ganho do motoboy': 0}

moto3 = {'Loja': "", 'Pedidos': 0, 'Valor da entrega': 0, 'Ganho do motoboy': 0}

moto4 = {'Loja': "", 'Pedidos': 0, 'Valor da entrega': 0, 'Ganho do motoboy': 0}

moto5 = {'Loja': "", 'Pedidos': 0, 'Valor da entrega': 0, 'Ganho do motoboy': 0}


def loja_1():
    pedido_1 = 50 * 0.05
    pedido_2 = 50 * 0.05
    pedido_3 = 50 * 0.05
    moto4['Loja'] += " Loja 1"
    moto4['Pedidos'] += 2
    moto4['Valor da entrega'] += 2
    moto4['Ganho do motoboy'] += pedido_1 + pedido_2 + moto4['Valor da entrega']

    moto1['Loja'] += " Loja 1"
    moto1['Pedidos'] += 1
    moto1['Valor da entrega'] += 2
    moto1['Ganho do motoboy'] += pedido_3 + moto1['Valor da entrega']


def loja_2():
    pedido_1 = 50 * 0.05
    pedido_2 = 50 * 0.05
    pedido_3 = 50 * 0.05
    pedido_4 = 50 * 0.05

    moto2['Loja'] += " Loja 2"
    moto2['Pedidos'] += 2
    moto2['Valor da entrega'] += 2
    moto2['Ganho do motoboy'] += pedido_1 + pedido_2 + moto2['Valor da entrega']

    moto1['Loja'] += " Loja 2"
    moto1['Pedidos'] += 2
    moto1['Valor da entrega'] += 2
    moto1['Ganho do motoboy'] += pedido_3 + moto2['Valor da entrega']

    moto3['Loja'] += " Loja 2"
    moto3['Pedidos'] += 2
    moto3['Valor da entrega'] += 2
    moto3['Ganho do motoboy'] += pedido_4 + moto2['Valor da entrega']


def loja_3():
    pedido_1 = 50 + (50 * 0.15)
    pedido_2 = 50 + (50 * 0.15)
    pedido_3 = 100 + (100 * 0.15)

    moto5['Loja'] += " Loja 3"
    moto5['Pedidos'] += 2
    moto5['Valor da entrega'] += 2
    moto5['Ganho do motoboy'] += pedido_1 + pedido_3 + moto5['Valor da entrega']

    moto3['Loja'] += " Loja 3"
    moto3['Pedidos'] += 1
    moto3['Valor da entrega'] += 2
    moto3['Ganho do motoboy'] += pedido_2 + moto2['Valor da entrega']


def buscar():
    loja_1()
    loja_2()
    loja_3()

    while True:
        print('Você gostaria de obter informações de qual motoboy? \n'
              'Digite 1 para Moto 1\n'
              'Digite 2 para Moto 2\n'
              'Digite 3 para Moto 3\n'
              'Digite 4 para Moto 4\n'
              'Digite 5 para Moto 5\n'
              'Digite 999 caso não queira mais consultar')
        escolha = str(input('Digite o número de escolha: '))
        try:
            if int(escolha) == 1:
                print('=' * 30)
                print("MOTOBOY 1 \n"
                      f"Quantidade de pedidos: {moto1['Pedidos']}\n"
                      f"Lojas pecorridas: {moto1['Loja']}\n"
                      f"Total recebido R$ {moto1['Ganho do motoboy']:.2f}")
                print('=' * 30)
            elif int(escolha) == 2:
                print('=' * 30)
                print("MOTOBOY 2 \n"
                      f"Quantidade de pedidos: {moto2['Pedidos']}\n"
                      f"Lojas pecorridas: {moto2['Loja']}\n"
                      f"Total recebido R$ {moto2['Ganho do motoboy']:.2f}")
                print('=' * 30)
            elif int(escolha) == 3:
                print('=' * 30)
                print("MOTOBOY 3 \n"
                      f"Quantidade de pedidos: {moto3['Pedidos']}\n"
                      f"Lojas pecorridas: {moto3['Loja']}\n"
                      f"Total recebido R$ {moto3['Ganho do motoboy']:.2f}")
                print('=' * 30)
            elif int(escolha) == 4:
                print('=' * 30)
                print("MOTOBOY 4 \n"
                      f"Quantidade de pedidos: {moto4['Pedidos']}\n"
                      f"Lojas pecorridas: {moto4['Loja']}\n"
                      f"Total recebido R$ {moto4['Ganho do motoboy']:.2f}")
                print('=' * 30)
            elif int(escolha) == 5:
                print('=' * 30)
                print("MOTOBOY 5 \n"
                      f"Quantidade de pedidos: {moto3['Pedidos']}\n"
                      f"Lojas pecorridas: {moto3['Loja']}\n"
                      f"Total recebido R$ {moto3['Ganho do motoboy']:.2f}")
                print('=' * 30)
            elif int(escolha) == 999:
                print('=' * 30)
                print('Obrigado por utilizar nossa consulta')
                print('=' * 30)
                break
        except Exception:
            print('=' * 30)
            print('Opção Inválida, tente novamente.')
            print('=' * 30)


if __name__ == '__main__':
    buscar()
