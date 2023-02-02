
with open('advent of code\\2021\day3\input_1.txt') as file:
    puzzle = []
    for line in file:
        puzzle.append(line.strip())

gama_rate =''
epsilon_rate = ''
zero_count = 0
one_count = 0

for pos in range(len(puzzle[0])):
    for line in puzzle:
        if line[pos] == '0':
            zero_count += 1
        else:
            one_count += 1
    
    if zero_count > one_count:
        gama_rate = gama_rate + '0'
    else:
        gama_rate = gama_rate + '1'
    zero_count = 0
    one_count = 0

print(gama_rate)


for pos in range(len(puzzle[0])):
    for line in puzzle:
        if line[pos] == '0':
            zero_count += 1
        else:
            one_count += 1
    
    if zero_count < one_count:
        epsilon_rate = epsilon_rate + '0'
    else:
        epsilon_rate = epsilon_rate + '1'
    zero_count = 0
    one_count = 0

def bin_to_dec(num):
    counter = 0
    dec_num = 0
    for i in num[::-1]:
        dec_num += int(i)* 2**counter
        counter += 1
    return dec_num

print(bin_to_dec(f'{gama_rate}')*bin_to_dec(f'{epsilon_rate}'))
