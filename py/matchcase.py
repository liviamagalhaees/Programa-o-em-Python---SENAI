

#numero = int(input('numero: '))

#match numero:
 #   case 5: 
  #      print('é o numero 5')
 #   case 1: 
  #      print('e o numero 1')
        

#Verificando se uma string é vazia ou não

string = (input('digite algo para saber se e vazio ou nao: '))

match string:
   case (''):
    print('vazio')
   case(string):
    print('Tem algo escrito') 

#Verificando se um número é positivo, negativo ou zero
numero1 = float(input('numero positivo negativo ou zero: '))
    
match numero1: 
  case 0:
    print ("Zero")
  case x if x > 0:
    print ("Positivo")
  case x if x < 0:
    print ("Negativo")

#Verificando se um número é maior, menor ou igual a 10

numero3 = int(input('digite um numero: '))

match numero3:
    case x if x <10:
        print('menor que dez')
    case x if x >10: 
        print('maior que dez')
    case x if x == 10: 
      print('igual a dez')


#Verificando se o número é par ou ímpar 

numero4 = int(input('digite um numero impar ou par: ')) 

match numero4: 
  case x if x % 2 == 0: 
    print('par')
  case x if x % 2 != 0: 
    print('impar')


#Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)

classificacao = int(input('digite a idade: '))

match classificacao: 
  case x if x <= 12: 
    print('criança')
  case x if x <= 17: 
    print('adolescente')
  case x if x <=35:
    print('jovem')
  case x if x <= 64: 
    print('adulto')
  case x if x >=65: 
    print('idoso')

