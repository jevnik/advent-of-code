my_file = open('advent_of_code_2022\directories real.txt','r')
data = my_file.read()

commands = data.split('\n')

path = '/home'
dirs= {
    path : 0

}


for command in commands:
   
    if command[0] == '$':
        
        if command[-1] == '/':
            pass
        
        elif command[2:4] == 'cd':
            if command[5:] == '..':
                path = path[:path.rfind('/')]
            else:
                path = path + '/' + command[4:]  
            
                dirs[path] = 0
    
    if command[0].isnumeric():
        dir = path
        for i in range(dir.count('/')):
            #print('+1', 'dir', dir)
            dirs[dir] += int(command.split(' ')[0])
            if dir != '/home':
                dir = dir[:dir.rfind('/')]
            
big_list = []    
for i in dirs.values():
    if i < 100000:
        big_list.append(i)
print(sum(big_list))