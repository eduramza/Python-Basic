#Exceções em python
#Tratando exceções afim de impedir a interrupção do código
#Tratar exceções garante que o programa não será encerrado quando houver problemas
try:
    n1 = 7
    n2 = 0
    print(n1 / n2)
    print('Calculo completado')
except ZeroDivisionError:
    print('Um erro ocorreu na tentativa de divisão:')
    print('Divisão por zero não permitida!')

#multiplos blocos de exceções
try:
    variable = 10
    print(variable + 'hello')
    print(variable / 2)
except ZeroDivisionError:
    print('Divisão por zero não permitida!')
except(ValueError, TypeError):
    print('Um erro ocorreu no processamento do código!')

#tratamento genérico
try:
    num = 10
    print(num / 0)
except:
    print('Um erro ocorreu!')

#Finally
#Todo código contigo em Finally será executado independente se houve exceção ou não no tratamento do TRY
try:
    print('Olá!')
    print(6/0)
except ZeroDivisionError:
    print('Erro divisão por zero')
finally:
    print('Esse código será executado mesmo que ocorra exceções!')

#Raise Exceptions
print(1)
raise ValueError
print(2)

name = '123'
raise NameError('Nome inválido!')

#raise genérico
try:
    num = 5/0
except:
    print('Um erro ocorreu:')
    raise

#Assertions são usadas para principios de test
print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)

temp = -10
assert(temp>= 10), 'Tratamento de um assert' 
