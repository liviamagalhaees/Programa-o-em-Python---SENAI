#CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar).

def numero():
    n1 = int(input('digite um numero: '))
    if n1 % 2 == 0: 
       print('par')
    else: 
        print('impar')

numero()      

#CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.


def num():
    n2 = int(input('numero: '))
    n3 = int(input('numero: '))
    n4 = int(input('numero: '))
    print(n2*n3*n4)

num()


#CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, 
# SE O USUÁRIO  DIGITAR, 18 ANOS.

def idade():
        idade1 = int(input('digite sua idade!: '))
        if idade1 == 18:
            print('Ok, voce tem 18 anos!') 
        else: 
            print('desculpe, voce nao tem 18 anos.')    

idade()  

#CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR 
# ELEVADO DE UM NÚMERO.


def valor():
    n1 = int(input('digite um numero: '))
    print(n1**2)

valor()

#ESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.



def escolha():
    while True:
        escolha = input(''' 
                        
        Descubra a idade de julia
        1 - 25
        2 - 18
        3 - 20
        4 - 22
                        
        ''')   
        
        print(escolha)
        if escolha == '1':
            print('Quase, um pouco mais nova')
        elif escolha == '2':
            print('Parabens acertou!')
            break
        elif escolha == '3':
            print('Quase, dica: -2')   
        elif escolha == '4':
            print('Quase, a sua escolha tem 4 anos a mais') 

escolha()


   










