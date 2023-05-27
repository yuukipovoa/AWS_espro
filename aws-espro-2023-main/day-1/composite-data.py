"""
Lista, Tuplas e Dicionarios
"""

# LISTA
myFruitList = ["apple", "banana", "cherry"]

# exibir dados da lista
print("LISTA ORIGINAL: ", myFruitList)

print(type(myFruitList))

# acessar posicao na lista
print(myFruitList[0])

# listas sao mutaveis // permite alteracoes
myFruitList[1] = "abacaxi"

print("LISTA ALTERADA: ", myFruitList)

print("--------------------------\n")


# tupla eh imutavel
myFinalAnswerTuple = ("apple", "banana", "pineapple")

print("TUPLA ORIGINAL: ", myFinalAnswerTuple)

# acessar posicao na tupla
print(myFinalAnswerTuple[1])


"""
Dicionario
"""

# chave : valor
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)

print(myFavoriteFruitDictionary["Saanvi"])