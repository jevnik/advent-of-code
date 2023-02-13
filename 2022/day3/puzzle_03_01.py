import os

my_file = open('advent of code\\rucksack_content_real.txt','r')

dic ={
}

brojac = 0

my_file1 = open('advent of code\dictionary of points.txt','r')

for line in my_file1:
    key = line.split()[0]
    value = line.split()[1]
    dic[key] = value    

data = my_file.read()

lista = data.split('\n')

cont1 = []
cont2 = []

for i in range(len(lista)):
    cont1.append(lista[i][:(int(len(lista[i])/2))])

for i in range(len(lista)):
    cont2.append(lista[i][(int(len(lista[i])/2)):])

for i in range(len(cont1)):
    for j in range(len(cont1[i])):
        
        if cont1[i][j] in cont2[i]:
            brojac = brojac + int(dic[cont1[i][j]])
            cont2[i] = cont2[i].replace(cont1[i][j],' ')