import os
my_file = open('advent of code\elf_crypto_msg.txt','r')

dic_op = {
    'A' : 'rock',
    'B' : 'paper',
    'C' : 'scisors'
}
dic_outcome = {
    'X' : 'loss',
    'Y' : 'draw',
    'Z' : 'win'
# win = 6
# draw = 3
# loss = 0
}
dic_ply = {
    'rock' :'1',
    'paper' :'2',
    'scisors' :'3'
}
data = my_file.read()
lista = []
score = 0
lista = data.split('\n')

for i in range(len(lista)):
    if 'X' in lista[i]:
        if 'A' in lista[i]:
            score += 3
        elif 'B' in lista[i]:
            score += 1
        elif 'C' in lista[i]:
            score += 2

    if 'Y' in lista[i]:
        score +=3
        if 'A' in lista[i]:
            score += 1
        elif 'B' in lista[i]:
            score += 2
        elif 'C' in lista[i]:
            score += 3
    
    if 'Z' in lista[i]:
        score += 6
        if 'A' in lista[i]:
            score += 2
        elif 'B' in lista[i]:
            score += 3
        elif 'C' in lista[i]:
            score += 1

print(score)