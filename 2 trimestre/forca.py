"""
- Utilize o print com três áspas
- Para mostrar \ utilize \\ dentro do print
- \t da um espaço como se fosse o tab no word
"""

palavras = [
    "ifpr",
    "cachorro",
    "mundial",
    "testando",
    "palavra composta"
]

dicas = [
    "É uma instituição de ensino",
    "É um animal",
    "Palmeiras",
    "Aqui é um exemplo",
    "É uma palavra composta"
]

num = 3

print(palavra[3])
print(dica[3])

# Criar vetor de riscos
riscos = ["_"] * 10
# len(palavra[3])

# Criar um vetor vazio
letras_digitas = []

letra = input("Digite uma letra: ")

# Adiciona esta letra ao vetor anterior
letras_digitas.append(letra)

print("""
_________
|       |
|\t|
|
|
|
|
""")

print("""
_________
|       |
|       o
|      / \\
|
|
|
""")
