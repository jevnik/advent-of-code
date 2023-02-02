from this import d


with open('advent of code\\2021\\day2\\input_1.txt') as file:
    com = file.read().splitlines()

#print(com)
forward = 0
depth = 0

for line in com:
    if line.startswith('forward'):
        forward += int(line.split()[1])

    elif line.startswith('down'):
        depth += int(line.split()[1])
    
    elif line.startswith('up'):
        depth -= int(line.split()[1])
    

mult = forward * depth

print(mult)    
    

