import os

my_file = open('elf_crypto_msg.txt','r')

dic_op = {
    'A' : 'rock',
    'B' : 'paper',
    'C' : 'scisors'

}

dic_ply = {
    'X' : 'rock 1',
    'Y' : 'paper 2',
    'Z' : 'scisors 3'

# win = 6
# draw = 3
# loss = 0

}


data = my_file.read()

lista = []
score = 0

lista = data.split('\n')

print(lista)

for i in range(len(lista)):
    if 'X' in lista[i]:
        score += 1
        
        if 'A' in lista[i]:
            score += 3
        
        elif 'C' in lista[i]:
            score += 6

    elif 'Y' in lista[i]:
        score += 2
        
        if 'B' in lista[i]:
            score += 3
        
        elif 'A' in lista[i]:
            score += 6
    
    elif 'Z' in lista[i]:
        score +=3
        
        if 'C' in lista[i]:
            score += 3
        
        elif 'B' in lista[i]:
            score += 6
    
print(score)