# dia = 7
# nome = "Rafael"
#
# print("Olá",nome,", hoje é dia",dia)
#
# print( "Olá {}, hoje é dia {}".format(nome, dia) )

vetor = [""]*5
i = 0
while i < len(vetor):
    vetor[i] = input("Produto {}: ".format(i+1) )
    i = i + 1

# Exercício 1: Crie um vetor e armazene os números de 1 a 100. Cada número deve ocupar uma posição do vetor (lista).
# Lista criada com 100 posições
lista = [""]*100
# Define a posição inicial para percorrer a lista
p = 0
# Enquanto o p for menor que o tamanho da lista (pq a última posição sempre é 1 a menos que o tamanho)
while p < len(lista):
    # Armazena o valor de p + 1 na lista, mas não atualiza o valor de p
    lista[p] = p + 1
    # Agora sim o valor de p é atualizado/incrementado
    p = p + 1

# Exercício 1a
# Define a posição inicial
p = 0
# Define o limite de p
while p < len(lista):
    # Mostra o elemento da lista que está na posição p
    print("Na posição {} tem o valor {}.".format(p, lista[p]))
    # Incrementa o p para ir para a próxima posição
    p = p + 1

# Exercício 1b ....
# Define que a posição inicial agora é a última do vetor
p = len(lista)-1
# Define que o p sempre tem que ser maior que 0 para funcionar
# Porque ele começa em 99 e vai diminuindo até 0
while p >= 0:
    # Mostra o valor na posição p
    print("Posição {} tem o valor {}".format(p, lista[p]) )
    # Diminui o valor de p até chegar no 0
    p = p - 1


print("Fim...")
