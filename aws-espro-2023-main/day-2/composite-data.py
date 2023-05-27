"""
Dados Compostos
"""

# importa as bibliotecas
import csv
import copy

# dicionario de dados
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# loop
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

# lista vazia
myInventoryList = []


# leitura do arquivo CSV
with open('day-2/car_fleet.csv') as csvFile:
    # estrutura dos dados no arquivo
    csvReader = csv.reader(csvFile, delimiter=',')
    # variavel de controle
    lineCount = 0
    # loop linha por linha
    for row in csvReader:
        # recuperar nome da coluna
        # condicional
        if lineCount == 0:
            # mostrar os nomes
            print(f'Column names are: {", ".join(row)}')
            # incrementar a variavel de controle
            lineCount += 1
        # mostrar os valores cadastrados
        else:
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            
            # criar copia em memoria
            currentVehicle = copy.deepcopy(myVehicle)  
            
            # substituir dados do dicionario original pelo dados do arquivo CSV
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]
            
            # injetar dicionario atualizado na lista vazia
            myInventoryList.append(currentVehicle)
            
            # incrementar a variavel de controle
            lineCount += 1
        
    # contagem total de linhas
    print(f'Processed {lineCount} lines.')
    

# mostrar dados na lista populada
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
    print("----------------------\r")