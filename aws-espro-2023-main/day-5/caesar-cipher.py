"""
CIFRA DE CESAR - CRIPTOGRAFIA
"""

# funcao para duplicar o alfabeto
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# receber mensagem do usuario para ser criptografada
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# receber chave de criptografia
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount


"""
CRIPTOGRAFANDO ...
"""

def encryptMessage(message, cipherKey, alphabet):
    
    # inicializar as variaveis
    encryptedMessage = ""
    uppercaseMessage = ""
    
    # mensagem transformada para letras maiusculas
    uppercaseMessage = message.upper()
    
    # loop
    for currentCharacter in uppercaseMessage:
        # OLA
        # ABCDE...  O, L, A
        # retorna posicao da letra no alfabeto
        position = alphabet.find(currentCharacter)
        
        # calculo de deslocamento
        # 0:A, 1:B, 2:C
        # 0 -> 2 == 2 (A => C)
        #OLA => [C]LA
        newPosition = position + int(cipherKey)
        
        # condicional
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter

    # retorna a mensagem criptografada        
    return encryptedMessage


"""
DECRIPTOGRAFANDO!
"""

def decryptMessage(message, cipherKey, alphabet):
    
    # processo inverso
    decryptKey = -1 * int(cipherKey)
    
    # retornar mensagem decriptografada
    return encryptMessage(message, decryptKey, alphabet)
    
    
    
"""
PROGRAMA DE CRIPTOGRAFIA
"""

def runCaesarCipherProgram():
    
    # declarando o alfabeto
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    
    # duplicando o alfabeto
    myAlphabet2 = getDoubleAlphabet(myAlphabet) # ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(f'Alphabet2: {myAlphabet2}')
    
    # recebendo mensagem do usuario
    myMessage = getMessage()
    print(myMessage)
    
    # recebendo a chave de cifra do usuario
    myCipherKey = getCipherKey()
    print(myCipherKey)
    
    # mensagem vai ser criptografada
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    # mensagem vai ser decriptografada
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    



# EXECUTAR O PROGRAMA -> FUNCAO PRINCIPAL runCaesarCipherProgram():
runCaesarCipherProgram()