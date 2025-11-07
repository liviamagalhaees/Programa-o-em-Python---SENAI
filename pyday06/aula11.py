def display():
    try:
        #erro com numero 
        n = int(input('numero 1: '))
        n2 = int(input('numero 2: '))
        print(n/n2)

        #erro se digitar um numero float
        c = int(input('digite um numero= '))
        print(c)
        
        #erro direto pois nao existe esse indice
        l = []
        print(l[-1])
    
    except ValueError as erro:  
        print(erro)
    except ZeroDivisionError as erro:
        print(erro)
    except IndexError as erro:
        print(erro)              
    else:
        print('Ocorre um erro, volte e reveja! ')
    finally:
        print('fim do codigo...')            
display()        



