with open('advent of code\\2021\day3\\test2.txt') as file:
    puzzle = []
    for line in file:
        puzzle.append(line.strip())


zero_count = 0
one_count = 0

cont = list.copy(puzzle)

all = []
for i in range(len(cont[0])):
    all.append([])


for i in range(len(cont[0])):

    for elem in cont:
        if elem[i] == '0':
            zero_count += 1
        else:
            one_count += 1

    if zero_count > one_count:
        for elem in cont:
            if elem[i] == '0':
                all[i].append(elem)
    elif zero_count < one_count:
        for elem in cont:
            if elem[i] == '1':
                all[i].append(elem)

    zero_count = 0
    one_count = 0

print(all)


def bin_to_dec(num):
    counter = 0
    dec_num = 0
    for i in num[::-1]:
        dec_num += int(i)* 2**counter
        counter += 1
    return dec_num

#print(bin_to_dec(f'{}')

