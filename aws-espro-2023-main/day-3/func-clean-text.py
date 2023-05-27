"""
LIMPEZA DE STRING
"""

import re

# lendo arquivo
with open('day-3/preproinsulin-seq.txt') as file:
    insulinFile = file.read()
    
# exibir dados do arquivo
print(insulinFile)


"""
FUNCAO PARA LIMPAR OS DADOS
"""

def cleanText(string):
    # remover ORIGIN
    string = string.replace("ORIGIN", "")
    
    # remover os numeros
    string = re.sub(r"\d+", "", string) # regex
    #string = string.replace("61", "")
    #string = string.replace("1", "")
    
    # remover espacos em branco
    #string = string.replace(" ", "")
    string = re.sub(r"\s", "", string)
    
    # remover quebra de linha
    string = string.replace("\n", "")
    # remover as //
    string = string.replace("//", "")
    
    return string

text = cleanText(insulinFile)

print("DADO LIMPO: ", text)


# contagem de caracteres
print("Quantidade de caracteres: ", len(text))