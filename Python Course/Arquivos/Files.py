#Trabalhando com arquivos de texto

#BOAS PRÁTICAS FEHANDO O ARQUIVO MESMO QUE ALGUM ERRO OCORRA E LIBERANDO MEMÓRIA
try:
    f = open('arquivo.txt', 'r')
    print(f.read())
finally:
    f.close()

#With statment também é uma solução ótima pois ao final do seu bloco o arquivo é fechado automáricamente
with open('arquivo.txt', 'r') as f:
    print(f.read())
    
#Abrindo o arquivo
#myFile = open('arquivo.txt')
#myFile.close()

#modos de abertura
'''
    r = apenas leitura, também é o método default da função open
    w = usado para reescrever no conteudo do arquivo
    a = append mode, para adicionar novos conteúdos no fim do arquivo
    b = para abrir os arquivos em modo binario
'''
#write mode
#myFyle = open('arquivo.txt', 'w')
#myFile.close()
#modo de escrita binário
#myFyleBin = open('arquivo.txt', 'b')
#myFyleBin.close()

#LEITURA
#A ultima linha do arquivo sempre será uma linha vazia, mesmo que ele não tenha conteúdo
'''
file = open('arquivo.txt', "r")
cont = file.read()
print(cont)
file.close()
'''

#limitando o numero de bytes lidos pelo arquivo
'''
file2 = open('arquivo.txt', 'r')
print(file2.read(16))#printar 16 bytes
print(file2.read(4))#printar 16 bytes
print(file2.read(4))#printar 16 bytes
print(file2.read())#printar 16 bytes
file2.close()
'''

#Lendo linha por linha
file2 = open('arquivo.txt', 'r')
print(file2.readlines())
file2.close()

#usando loop for

file3 = open('arquivo.txt', 'r')
for line in file3:
    print(line)

file3.close()

#Escrevendo em arquivos
file = open('novo.txt', 'w')
file.write('Escrevendo no arquivo zika da balada 222222')
file.close()

file = open('novo.txt', 'r')
print(file.read())
file.close()

#retornando se uma escrita foi bem sucedida
msg = 'Hello World!'
file = open('novo.txt', 'w')
amount_written = file.write(msg)
print(amount_written)
file.close()

