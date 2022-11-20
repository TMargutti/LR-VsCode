#Exercicio alternativo switch/case em python

numero = int (input("Digite o numero: "))
listanumero = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



if numero in listanumero:
    print("Numero", numero, "Existe")
else:
    print (numero, "Não existe, Deseja incluir? [s] ou [n]")
    escolha = input()
    if escolha == "s":
        listanumero.append (numero)
    elif escolha == "n":
        print ("numero não adicionado a Lista")
    else:
        print ("Escolha não identificado")
print ("Numero está na posição", listanumero.index (numero))




"""
for i in listanumero:
    if numero == listanumero[i]:
        print("Numero", numero, "Esta incluso") 
    else:
        print ("numero não incluso")
"""
    
    