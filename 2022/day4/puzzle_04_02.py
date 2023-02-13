my_file = open('section_assignment_real.txt', 'r')

lista = []

linije = my_file.readlines()

for i in range(0,len(linije)-1):
    lista.append(linije[i][:-1])

lista.append(linije[-1])

lista2 = []

for i in lista:
    lista2.append(i.split(','))
    
rastavljeni_elf = []
parni_elf = []
neparni_elf = []

for i in range(len(lista2)):
    for j in lista2[i]:
        rastavljeni_elf = rastavljeni_elf[:] + [j.split('-')]

for i in range(len(rastavljeni_elf)):
    for j in range(len(rastavljeni_elf[i])):
        rastavljeni_elf[i][j] = int(rastavljeni_elf[i][j])


for i in range(len(rastavljeni_elf)):
    if i % 2 == 0:
        parni_elf = parni_elf[:] + [rastavljeni_elf[i]]
    else:
        neparni_elf = neparni_elf[:] + [rastavljeni_elf[i]]

parni_elf_raspon = []
neparni_elf_raspon = []
temp = []

for i in parni_elf:
    for j in range(int(i[0]),int(i[1])+1):
        temp = temp[:] + [j]
    parni_elf_raspon = parni_elf_raspon[:] + [temp]
    temp = []



for i in neparni_elf:
    for j in range(int(i[0]),int(i[1])+1):
        temp = temp[:] + [j]
    neparni_elf_raspon = neparni_elf_raspon[:] + [temp]
    temp = []

brojac = 0

for i in range(len(parni_elf_raspon)):
    for j in parni_elf_raspon[i]:
        if j in neparni_elf_raspon[i]:
            brojac += 1
            break

print(brojac)

