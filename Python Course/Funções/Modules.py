#Modules são pedaços de códigos que possuem funcionalidades uteis
#para fazer a chamada de modules basta apenas usar a palavra importcomo no exemplo abaixo
import random
from math import pi, sqrt #nesse exemplo esta sendo importado uma certa função para uma variavel que pode ser usada normalmente
from math import sqrt as quadrado #dando um alias para o valor importado, util para importar funções com nomes muito grandes

for i in range(5):
    value = random.randint(1,6)
    print(value)

print(pi)

print(quadrado(100))