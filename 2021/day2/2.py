
with open('advent of code\\2021\\day2\\input_2.txt') as file:
    com = file.read().splitlines()

#print(com)
forward = 0
depth = 0
aim = 0

for line in com:
    

    if line.startswith('down'):
        aim += int(line.split()[1])
    
    elif line.startswith('up'):
        aim -= int(line.split()[1])
    
    elif line.startswith('forward'):
        forward += int(line.split()[1])
        depth += aim * int(line.split()[1])
    

 
print(forward*depth)

