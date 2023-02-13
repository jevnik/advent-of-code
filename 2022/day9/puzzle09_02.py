import math

my_file = open('snake_test.txt','r')
data = my_file.read().split('\n')
print(data)


rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
head = rope[0]
tail = rope[-1]

visited = {(0,0)}

for i in data:
    print()
    print('Uputa:',i)
    if 'R' in i:
        for i in range(int(i.split(' ')[-1])):
            rope[0][0] += 1
            for j in range(1,(len(rope))):
                if rope[j-1][1] != rope[j][1] and abs(rope[j-1][0]-rope[j][0]) == 2:
                    rope[j][0] += 1
                    if rope[j-1][1] > rope[j][1]:
                        rope[j][1] += 1
                    else:
                        rope[j][1] -= 1

                elif (rope[j-1][0]-rope[j][0]) == 2:
                    rope[j][0] += 1
            print(rope)
        
    elif 'L' in i:
        for i in range(int(i.split(' ')[-1])):
            rope[0][0] -= 1
            for j in range(1,(len(rope))):
                if rope[j-1][1] != rope[j][1] and abs(rope[j-1][0]-rope[j][0]) == 2:
                    rope[j][0] -= 1
                    if rope[j-1][1] > rope[j][1]:
                        rope[j][1] += 1
                    else:
                        rope[j][1] -= 1

                elif (rope[j-1][0]-rope[j][0]) == -2:
                    rope[j][0] -= 1
            print(rope)
    
    elif 'U' in i:
        for i in range(int(i.split(' ')[-1])):
            rope[0][1] += 1
            for j in range(1,(len(rope))):
                if rope[j-1][0] != rope[j][0] and abs(rope[j-1][1]-rope[j][1]) == 2:
                    rope[j][1] += 1
                    if rope[j-1][0] > rope[j][0]:
                        rope[j][0] += 1
                    else:
                        rope[j][0] -= 1

                elif (rope[j-1][1]-rope[j][1]) == 2:
                    rope[j][1] += 1
            print(rope)

    elif 'D' in i:
        for i in range(int(i.split(' ')[-1])):
            
            rope[0][1] -= 1
            
            for j in range(1,(len(rope))):
                if rope[j-1][0] != rope[j][0] and abs(rope[j-1][1]-rope[j][1]) == 2:
                    rope[j][1] -= 1
                    if rope[j-1][0] > rope[j][0]:
                        rope[j][0] += 1
                    else:
                        rope[j][0] -= 1

                elif (rope[j-1][1]-rope[j][1]) == -2:
                    rope[j][1] -= 1
            print(rope)


    