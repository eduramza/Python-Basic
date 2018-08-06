#Exemplos de utilização, criação e operações com listas
#Listas simples
print('********** Validações básicas em lista ***************')
words = ['hello', 'world', '!']
print(words[0])
print(words[1])
print(words[2])

empty_list = []
print(empty_list)

print('********** Variáveis e listas dentro de listas ************')
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][1])

print('************* Exemplo de operações com string *************')
str = "Hello World!"
print(str[6])

#*******************************Operações************************************
print('****************** Operações de valores **********')
nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

nums = [1, 2, 3]
print(nums + [4,5,6])
print(nums * 3)

print('**************** Checando se está na lista *************')
words = ["spam", "eggs", "spam", "sausage"]
print('spam' in words)
print('egg' in words)
print('sausage' in words)

print('**************** Checando se não está na lista *************')
nums = [1,2,3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

#********************************Funções**********************************
#append adiciona um novo item no fim da lista
nums = [1,2,3]
nums.append('Teste')
print(nums)

#insert pode inserir em qualquer posição da lista
words = ['oi', 'wis']
index = 0
words.insert(index, 'olá')
print(words)

#contar o tamanho da lista
nums = [1,3,5,2,4, 10]
print(len(nums))

#achando a posição de um item na lista
letters = ['p', 'f', 'w', 'a', 'l', 'k', 'p', 'j']
print(letters.index('f')) 
print(letters.index('a'))
print(letters.index('k'))

#outras funções de listas
print(max(letters)) #valor maximo contido na lista
print(min(letters))
print(letters.count('p'))
letters.remove('f')
print(letters)
letters.reverse()
print(letters)

