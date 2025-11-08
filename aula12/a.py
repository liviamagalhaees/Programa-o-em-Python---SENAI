def rest():
        print('Ola seja bem vindo ao nosso restaurante')  
        cardapio = ['', 'salada', 'macarronada', 'sanduiche', 'sorvete']
       

        p = input('Deseja ver o cardapio?: ')
        if p == 'sim':
         print(cardapio)
        pedido = []
        p2 = input('O que deseja pedir de acordo com os nomes do cardapio?: ')
        pedido.append(p2)
        print(pedido)
        
        p9 = input('Deseja pedir mais alguma coisa?: ')
        if p9 == 'sim': 
            print(pedido)
            p3 = input('deseja pedir mais o que: ')
            pedido.append(p3)
            print(pedido)
            print('Pedido final = ', (pedido))
            p0 = input('qual vai ser a forma de pagamento?: ')
            print('ok', p0)

        else:
            print('Pedido final = ', (pedido))
            p6 = input('qual vai ser a forma de pagamento?: ')
            print('ok', p6)
            
rest()
  
   