""""
GERAR ARQUIVOS DINAMICAMENTE
"""

# lendo arquivo
with open('day-3/preproinsulin-seq-clean.txt') as file:
    insulinFile = file.read()
    
# exibir dados do arquivo
print("ORIGINAL: ", insulinFile)

# valores
lsInsulin = insulinFile[0:24]
bInsulin = insulinFile[25:54]
aInsulin = insulinFile[90:110]
cInsulin = insulinFile[55:89]

# lista
names = ["lsInsulin", "bInsulin", "aInsulin", "cInsulin"]

# loop
for insulin in names:
    fw = open('day-3/' + insulin + '-seq-clean.txt', 'w')
    fw.write(globals()[insulin])
    fw.close()