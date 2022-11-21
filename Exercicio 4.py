# Utilidade Range gera numeros, aqui no caso de 1 a 10 em tipo lista
import random


#lista = list(range(1,11))
lista = [10, 2, 35, 47, 52, 69, 59, 81, 99, 16]
print (lista)
lista2 = list(range(1,61))
print (lista2)
sorteio = random.choice(lista)
print (sorteio)

sorteio = random.sample(lista2, 6)
sorteio.sort()
print (sorteio)


#converte lista em tupla
x  =  [ 1 , 2 , 3 , 4 ] 
tuple ( x )
print (x)
# Tuplas é uma lista que não pode ser modificadas
# Converter uma tupla em uma lista 
list(x)
print (x)

# DICIONARIO uma estrutura de dados que armazena pares de valores chave nos quais as chaves DEVEM ser objetos imutáveis.

dicionario1 = {'A': 1, 'B':2, 'C':3, 'D':4}
print (dicionario1 ['B'])




