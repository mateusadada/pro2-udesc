import sys
import json
from Data import Data

##################################################

## Questão 03: (Crie o código necessário para gravar os dados em arquivo JSON
##              Salvar os dados em um arquivo com nome: "Banco_Alunos.json.txt")
def Programa_Principal():
    try:
        with open('Banco_Alunos.json.txt', 'w') as file:
            json.dump(Data, file)
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        sys.exit(0)
    except IOError:
        print("Erro: Erro de entrada e saída.")
        sys.exit(0)

## Questão 04: (Crie o código necessário para encerrar o programa)
Programa_Principal()

##################################################
