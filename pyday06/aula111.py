#parametros

def soma(a,b):
    return a + b


def sub(a,b):
    return a - b


def calculdora():
 while True:       
        n1  =  float(input('= '))
        op =  input('+ ou -')
        if op == '+':
            n2  =  float(input('= '))
            print(soma(n1, n2))
        elif op == '-':
            n2  =  float(input('= '))
            print(sub(n1, n2))
        else:
            print('Digite algo válido')                
            
calculdora()



# import statistics


# # desvio padrao
# # variancia 
# # media 
# # moda
# # mediana 




# def estatistica(notas):
#     media  =  statistics.mean(notas)
#     mediana = statistics.median(notas)
#     desvio_p = statistics.stdev(notas)
#     variancia = statistics.variance(notas)
#     moda = statistics.mode(notas)


#     return media, moda, mediana, desvio_p, variancia


# notas = [10.,9.,5.,6.5,8.,7.,9.,5]
# notas1 = [10.,5.,6.5]
# notas2 = [8.,7.,9.,5]
# notas3 = [10.,9]



# print(estatistica(notas))
# print(estatistica(notas1))
# print(estatistica(notas2))
# print(estatistica(notas3))