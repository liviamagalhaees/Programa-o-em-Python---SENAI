c = lambda x : x * 2
print(c(10))



def soma():
    a =  float(input('='))
    b =  float(input('='))
    return a + b


def sub(a,b):
    a =  float(input('='))
    b =  float(input('='))
    return a - b


def calculdora():
 while True:       
        
        op =  input('+ ou -')
        if op == '+':
            print(soma())
        elif op == '-':
           print(sub())
        else:
            print('Digite algo válido')                
            
calculdora()














