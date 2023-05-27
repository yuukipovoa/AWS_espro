"""
Strings
"""

myString = "This is a string."

print(myString)

print(myString + " is of the data type " + str(type(myString)))

# multiplas variaveis
firstString = "water"
secondString = "fall"

# concatenacao
thirdString = firstString + secondString

# mostrar strings concatenadas
print("STRINGS CONCATENADAS: ", thirdString)


"""
RECUPERAR DADOS DIGITADOS PELO USUARIO
"""

# funcao input()
name = input("What is your name?: ")

print("O NOME DIGITADO FOI: ", name)

# funcao format()

action = "NOME"

print("O {} DIGITADO FOI: {}".format(action, name))

# INPUTS

color = input("What is your favorite color?:  ")
animal = input("What is your favorite animal?: ")

print("{}, you like a {} {}!".format(name,color,animal))