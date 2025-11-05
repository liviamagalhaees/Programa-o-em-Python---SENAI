 #Faça um programa, utilizando while, que mostre na tela os números de 0 a 1000.

#Faça um sistema, utilizando while e listas, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.


# pessoas = []
# for i in range(0,11) :

#         nome = input('Digite dez nomes: ')
#         pessoas.append(nome)
#         print(pessoas)
        
c = 10 
pessoas = []
while c>0:
        nome = input('Digite dez nomes: ')
        pessoas.append(nome)
        print(pessoas,c)
        c = c - 1
