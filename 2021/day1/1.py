with open('input_1.txt') as depth:
    depth = depth.read().splitlines()

count = 0
curr = 0

for d in depth:
    if int(d) > curr:
        count +=1
        curr = int(d)
    curr = int(d)

print(count-1)