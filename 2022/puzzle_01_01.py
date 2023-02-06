import os

my_file = open('advent of code\elfs_food.txt','r')

data = my_file.read()



data_to_list = data.split('\n\n')
#data_to_list.remove('')
a = 0
popis = []

for i in data_to_list:
    popis.append(i.split('\n'))

for i in range(len(popis)):
    for j in range(len(popis[i])):
        popis[i][j] = int(popis[i][j])

zbrojevi = []
for i in range(len(popis)):
    zbrojevi.append(sum(popis[i]))

print(zbrojevi)
print(max(zbrojevi))