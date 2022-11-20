
#Exercicio loop com for
# conta a variavel sendo ela de valor=0, na range até 10posição exclusive
for i in range(11):
  print(i)

print ("----------------------")

#começa com a variavel pelo 2inclusivo, até 10naoinclusivo
for x in range(2, 10):
  print(x)

print ("----------------------")

#variavel i comça com valor 5, conta até 16exclusiv somando de 3 em 3
for i in range(5, 16, 3):
  print(i)

print ("----------------------")

for i in "hello!":
  print(i)


string = "hello world!"
#conta as posições das letras e informa o valor da string
for i in range(0, len(string), 1):
  print(str(i) + "th letter is "+ string[i])


#WHILE / Enquanto
#variavel começa com valor = 0
count = 0
#Enquanto a variavel for menor que 10, printa!!!
while (count < 10):
    print(count)
    #Essa porra aqui soma a variavel +1
    count += 1

"""
while True:
  user = input("Digita ai qualquer coisa: ")
  ## Quando o "break" é acionado, o print() abaixo NÃO será executado.
  ## O programa romperá o loop quando esta palavra-chave for lida.
  if user=="arcoiro":
    print("Finish Him")
    break
  print(user)

  arcoiro = False
while arcoiro == False:
  user = input("Enter something to be repeated: ")
  if user=="arcoiro":
    print("Program Ended!!!")
    end = True
  else:
    print(user)
    """


#While / Enquanto para contar multiplos
numero = int(input("\f Digite o numero: "))
while numero < 51:
    if numero % numero != 0:
        print ("Resultado não zero")
        numero += 1
        continue
    print(numero)
    numero += 1
    
