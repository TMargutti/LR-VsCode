import string


def isPalindrome(str):

   # Como não conseguimos controlar o que o usuário insere na sentença, vamos esclarecer primeiro a sentença.
   # Vamos remover todas as pontuações e espaços brancos da sentença e colocar todas as letras em minúsculo 
   # Na variavel exclude, seta todas as pontuações 
   exclude = set(string.punctuation)
   print ("1º", exclude)
   # Na Variavel str retirase dos caracteres as pontuações
   str = ''.join(ch for ch in str if ch not in exclude)
   print ("2º", str)
   #Nesse caralho aqui, tira os espaços e coloca tudo em minusculo
   str = str.replace(" ", "").lower()
   print ("3º", str)

   # Esse carai aqui  str [::-1] inverte a ordem da string
   print ("4º", str [::-1])
   # SE a str for igual a str ao contrario entao retorna verdade, senao retorna falso
   if str == str [::-1]:
    return True
   else:
    return False

# Solicitar ao usuário que introduza a sentença
def main():
  userSentence = input("Entre com a palavra para teste palindromo: ")

  if (isPalindrome(userSentence)):
    print(userSentence + " é Palindromo")
  else:
    print(userSentence + " Não Palindromo")

if __name__ == "__main__":
    main()