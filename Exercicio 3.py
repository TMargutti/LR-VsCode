#Função max retorna maior valor entre as variaveis

var1 = 4
var2 = 8
var3 = 16
max_val = max(var1, var2, var3)
print(max_val) 


#Funções DEF

def e_triangulo(a, b, c):

  # Reatribuir valores variáveis para garantir que C seja o comprimento mais longo
  # SE (retorna a maior variavel) != (diferente) da variavel C
  if (max(a,b,c) != c):
    # tmp armazena os valores anteriores de C, que não é o comprimento mais longo
    tmp = c
    c = max(a,b,c)

    if a == c:
      a = tmp
    elif b == c:
      b = tmp
    

  # Aplicar a fórmula
  if a**2 + b**2 == c**2:
    print("Triangulo retangulo meu parça")

    # Se o programa vê uma declaração Return, este é o FIM do programa/função
    return True
  
  # Estas duas linhas funcionarão SOMENTE quando a condição IF for falsa
  print("iii mano, deu ruim, não é triangulo retangulo")
  return False


# Solicite ao usuário que insira 3 comprimentos
def main():
  a = input("Digita aew o valor do primeiro lado do triangulo: ")
  b = input("Digita aew o valor do segundo lado do triangulo:")
  c = input("Digita aew o valor do terceiro lado do triangulo:")

  # As entradas do usuário são armazenadas como uma string, então nós as computamos para ser int
  return e_triangulo(int(a), int(b), int(c))

if __name__ == "__main__":
    main()
