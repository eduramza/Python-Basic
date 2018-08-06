def my_func():
    print("Teste 1")
    print("Teste 2")
    print("Teste 3")

my_func()

#funções precisam ser sempre definidas antes de serem chamadas
#No exemplo abaixo, primeiro é feito a chamada da função para só depois a criação da mesma
#Então temos um erro
'''
hello()

def hello():
    print('Hello Jhovem!')
'''

#Argumentos
def print_exclamation(word):
    print(word + '!')

print_exclamation('Zorro')
print_exclamation('Burger King')
print_exclamation('Chinelo')

def somar(x, y):
    print(x+y)

somar(10,8)
somar(9863, 98741)

#Retorno de funções
def max(x,y):
    if x >= y:
        return x
    else:
        return y

print(max(13, 87))
z = max(787, 144)
print(z)

#Return finaliza uma função e qualquer código digitado após ele é ignorado
def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")

print(add_numbers(4, 5))

#Variaveis recebendo como atributos as funções
def multiply(x, y):
   return x * y

a = 4
b = 7
operation = multiply
print(operation(a, b))

#passando funções como argumentos de outras funções
def add(x, y):
  return x + y

def do_twice(func, x, y):
  return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))


