import sys
from Data import Data

# Questão 02: (Crie o código necessário para gravar os dados em arquivo de texto
# Salvar os dados em um arquivo com nome: "Banco_Alunos.txt")
try:
    file = open('./Banco_Alunos.txt', 'w')
    for Aluno in Data:
        file.write('%s\n' % Aluno)

except IOError as e:
    print('um erro ocorreu:',e)

except FileNotFoundError:
    print('Nao achou')

# Questão 03: (Crie o código necessário para encerrar o programa)
sys.exit(0)
