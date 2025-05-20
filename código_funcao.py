def soma(numeroA, numeroB):
  resultado = numeroA + numeroB
  print(f"O resultado da soma é: {resultado}")
  
def subtracao(numeroAm, numeroBm):
  resultado = numeroAm - numeroBm
  print(f"o resultado é: {resultado}")


def multiplicacao(numeroax, numerobx):
  resultado = numeroax * numerobx
  print(f"o resultado é: {resultado}")

def divisao(numeroadiv, numerobdiv):
  resultado = numeroadiv / numerobdiv
  print(f"o resultado é: {resultado}")

def raiz(numeroA):
  resultado = numeroA ** 0.5
  print(f"O resultado é: {resultado}")
  
  
opcao = int(input("MENU, escolha sua formula para calcular! APENAS NUMEROS!"))

if (opcao ==  1):
  numeroA = float(input("Digite o 1º número: "))
  numeroB = float(input("digite o 2° numero: "))
  soma(numeroA, numeroB)

elif (opcao == 2):
  
   numeroAm =float(input("digite o 1° numero: "))
   numeroBm =float(input("digite o 2° numero:" ))
   subtracao(numeroAm, numeroBm)
    
elif (opcao == 3):
    numeroax = float(input("digite o 1° numero: "))
    numerobx = float(input("digite o 2° numero: "))
    multiplicacao(numeroax, numerobx)
    
elif (opcao == 4):
      numeroadiv = float(input("digite o primeiro numero: "))
      numerobdiv = float(input("digite o 2° número: "))
      divisao(numeroadiv, numerobdiv)
  
elif (opcao == 5):
  numeroA = float(input("Digite o número: "))
  raiz(numeroA)

