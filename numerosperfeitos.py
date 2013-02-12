import sys
  
def ehPrimo(x):
  return x % 2 != 0 and x % 3 != 0
  
def obterDivisores(num):
  divisores = []
  for i in range(1,num):
    if (num % i) == 0:
      divisores.append(i)
  return divisores
  
def ehPerfeito(num):
  # nenhum numero primo e perfeito
  if ehPrimo(num): return False
  
  # Encontra todos os divisores de num
  divisores = obterDivisores(num)
      
  # Se a soma dos divisores de num for igual ao valor de num, 
  # num e um numero perfeito  
  return num == sum(divisores) 
  
def numerosPerfeitos(ate):
  return filter (ehPerfeito, range(1,ate))
  
def main():
  print("Os numeros perfeitos ate {} sao:".format(sys.argv[1]), 
    numerosPerfeitos(int(sys.argv[1])))  
  
if __name__ == '__main__':
  main()
  