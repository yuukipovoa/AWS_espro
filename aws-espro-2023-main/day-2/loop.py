"""
Repeticao com FOR e WHILE
"""
# biblioteca para gerar numeros aleatorios
import random

# for - PARA
# while - ENQUANTO

# mensagem de boas-vindas
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# gerar numero aleatorio entre 1 e 10
number = random.randint(1,10)

# mostrar
#print(number)

# variavel de controle
isGuessRight = False

# estrutura
while isGuessRight != True:
    # solicitar o usuario digitar um numero entre 1-10
    guess = input("Guess a number between 1 and 10: ")
    # condicional
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        # alterar a variavel de controle
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))



