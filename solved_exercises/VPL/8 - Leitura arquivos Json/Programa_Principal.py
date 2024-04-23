import sys
import json

##################################################

## Questão 01: (Crie o código necessário para ler os dados do arquivo JSON
##              O arquivo já é fornecido e possui o nome: "Banco_Alunos.json.txt")
with open('Banco_Alunos.json.txt', 'r') as f:
    Data = json.load(f)

## Questão 02: (Crie o código necessário para imprimir na tela os dados das cidades)
def print_items():
    output_string = ""
    for p in Data['Aluno']:
        print(f'Aluno_Key: { p["Aluno_Key"] }')
        print(f'Cidade_Key: { p["Cidade_Key"] }')
        print(f'Aluno_Nome: { p["Aluno_Nome"] }')
        print(f'Aluno_Idade: { p["Aluno_Idade"] }\n')

    for p in Data['Cidade']:
        print(f'Cidade_Key: { p["Cidade_Key"] }')
        print(f'Cidade_Nome: { p["Cidade_Nome"] }')
        print(f'Cidade_Abrev: { p["Cidade_Abrev"] }\n')

## Questão 03: (Crie o código necessário para imprimir na tela os dados dos alunos)
try:
    print_items()

except IOError:
    print('Erro de acesso aos dados')
except FileNotFoundError:
    print('Arquivo não encontrado')

## Questão 04: (Crie o código necessário para encerrar o programa)
sys.exit(0)

##################################################
