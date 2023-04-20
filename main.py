
#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
#anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
#informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número
#informado pertence ou não a sequência.
#IMPORTANTE:
#Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido
#no código;

f = [0, 1]

n = int(input("Digite um número: "))

while f[-1] < num:
    f.append(f[-1] + f[-2])

if n in f:
    print(f"O número {n} pertence à sequência Fibonacci.")
else:
    print(f"O número {n} não pertence à sequência Fibonacci.")