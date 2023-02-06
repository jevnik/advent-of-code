import math

my_file = open('snake_real.txt','r')
data = my_file.read().split('\n')
print(data)

head = [0,0]
tail = [0,0]
visited = {(0,0)}

for i in data:
    print()
    print('Uputa:',i)
    
    if 'R' in i:
        for i in range(int(i.split(' ')[-1])):
            
            head[0] +=1
            print('head:',head)
            
            if head[1] != tail[1] and abs(head[0]-tail[0]) == 2:
                tail[0] += 1
                if head[1] > tail[1]:
                    tail[1] += 1
                else:
                    tail[1] -= 1

            elif (head[0]-tail[0]) == 2:
                tail[0] += 1
            visited.add((tail[0],tail[1]))
            print('tail',tail)
            print()
    
    elif 'L' in i:
        for i in range(int(i.split(' ')[-1])):
            
            head[0] -=1
            print('head:',head)
            
            if head[1] != tail[1] and abs(head[0]-tail[0]) == 2:
                tail[0] -= 1
                if head[1] > tail[1]:
                    tail[1] += 1
                else:
                    tail[1] -= 1

            elif (head[0]-tail[0]) == -2:
                tail[0] -= 1
            
            visited.add((tail[0],tail[1]))
            print('tail',tail)
            print()
        

    elif 'U' in i:
        for i in range(int(i.split(' ')[-1])):
            
            head[1] +=1
            print('head:',head)
            
            if head[0] != tail[0] and abs(head[1]-tail[1]) == 2:
                tail[1] += 1
                if head[0] > tail[0]:
                    tail[0] += 1
                else:
                    tail[0] -= 1

            elif (head[1]-tail[1]) == 2:
                tail[1] += 1
            
            visited.add((tail[0],tail[1]))
            print('tail',tail)
            print()

    elif 'D' in i:
        for i in range(int(i.split(' ')[-1])):
            
            head[1] -=1
            print('head:',head)
            
            if head[0] != tail[0] and abs(head[1]-tail[1]) == 2:
                tail[1] -= 1
                if head[0] > tail[0]:
                    tail[0] += 1
                else:
                    tail[0] -= 1

            elif (head[1]-tail[1]) == -2:
                tail[1] -= 1
            
            visited.add((tail[0],tail[1]))
            print('tail',tail)
            print()
    
print(type(visited))
print(visited)
print('res: ',len(visited))