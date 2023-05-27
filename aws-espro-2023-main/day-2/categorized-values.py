"""
Categorizando Valores
"""

# dados mistos
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

print("LISTA ORIGINAL: ", myMixedTypeList, " /n")

# estrutura de repeticao com LOOP
# loop FOR
print("LISTA COM LOOP: ")

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))

# acessando valores manualmente
#myMixedTypeList[3]

