import os

my_file = open('rucksack_badge_real.txt','r')

dic ={
}

brojac = 0

my_file1 = open('dictionary of points.txt','r')

for line in my_file1:
    key = line.split()[0]
    value = line.split()[1]
    dic[key] = value    

data = my_file.read()

lista = data.split('\n')



def findCommonSymbol(x,y):
    lista = []
    if len(x) > len(y):
        for i in x:
            if i in y:
                lista = lista[:] + [i]

    else:
        for i in y:
            if i in x:
                lista = lista[:] + [i]
    return lista


parovi = []

for i in range(3,int(len(lista))+1,3): 

    a = (lista[i-3])
    b = (lista[i-2])
    c = (lista[i-1])
    parovi = parovi[:] +[[a,b,c]]
    


isti_znakovi1 = [] # isti znakovi u prvom i drugom elementu jednog skupa
isti_znakovi_rj = [] # rjesenje, znak koji je isti u sva tri elementa prvog skupa

x = 0

for i in range(int(len(parovi))):
    for j in range(len(parovi[i])-1):
        x = j + 1
        isti_znakovi1 = isti_znakovi1+ [findCommonSymbol(parovi[i][x],parovi[i][j])]
        
isti_znakovi3 = [] # iz isti_znakovi1 maknuti duplikati
for i in range(len(isti_znakovi1)):

    dictemp = dict.fromkeys(isti_znakovi1[i])
   
    isti_znakovi3.append(list(dictemp))

for i in range(0,len(isti_znakovi3)-1,2):
    x = i + 1
    for j in isti_znakovi3[i]:
        if j in isti_znakovi3[x]:
            
            isti_znakovi_rj = isti_znakovi_rj + [j]



brojac = 0
for i in isti_znakovi_rj:
   
    brojac += int(dic[i])


print('len lista', len(lista))
print('len parovi', len(parovi))
print('brojac: ', brojac)