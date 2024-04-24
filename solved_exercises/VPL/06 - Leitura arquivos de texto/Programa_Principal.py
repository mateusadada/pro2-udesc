import sys

# Questão 01: (Crie o código necessário para ler os dados do arquivo de texto
# O arquivo já é fornecido e possui o nome: "Banco_Alunos.txt")
try:
    with open('Banco_Alunos.txt', 'r') as f:
        Vect_Str = f.readlines()

except FileNotFoundError as e:
    print("O arquivo não foi encontrado.")
except IOError as e:
    print("O arquivo não pode ser aberto.")
except Exception as e:
    print("O arquivo está corrompido.")

# Questão 02: (Crie o código necessário para imprimir na tela os dados)
for str in Vect_Str:
    str = str.strip()
    print('%s' % str)

# Questão 03: (Crie o código necessário para encerrar o programa)
sys.exit(0)
