# nome  =  estrutura dado ou objeto 

# estrutura composta
# pode ser iteravel - percorrivel

# lista vazia
lista_vazia  =  []
print(lista_vazia)

# lista com valores inteiros
#         -3-2-1 # indices negativos
 
#          0 1 2 # indices positivos
# print(lista[0]) # acessei indice

# atribuindo a variáveis
# n1 =  lista[0] 
# n2 =  lista[1]
# print(n1 + n2)
# x = 10
# métodos de listas:

lista   =  [8,1,2,3,1, 500,500]
lista_t = ['z','a','b']

# append  -  adicionar 1 valor no final

lista.append(100)
# print(lista)

# insert - add no indice que vc quiser 
lista.insert(0,250)
# print(lista)

# count -  conta a quantidade do dado
# print(lista.count(8))

# extend -  add varios dados de um vez no final
lista.extend([10,2,3,6,5,410])
# print(lista)

# +=() -  add varios dados
lista +=(10,3,6,5,10,150,'texto')
print(lista)

# adicionando manualmente -  substituição
lista[0] = 500
print(lista)

# removendo dados da lista através do valor

lista.remove(500)
print(lista)

# del  -  deleta de dentro para fora 

del lista[0]
print(lista)

# pop -  com indice ou sem indice

lista.pop()