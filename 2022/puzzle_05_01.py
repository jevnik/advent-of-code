
c = [['N','D','M','Q','B','P','Z'],['C','L','Z','Q','M','D','H','V'],['Q','H','R','D','V','F','Z','G'],['H','G','D','F','N'],['N','F','Q'],['D','Q','V','Z','F','B','T'],['Q','M','T','Z','D','V','S','H'],['M','G','F','P','N','Q'],['B','W','R','M']]
my_file = open('stacks_crates_real.txt', 'r')
data = my_file.readlines()

#print(data)
temp = []
upute = []
templist = []
#print(data)
for line in data:
    templist = templist[:] + line.split(' ')
    
    for j in range(len(templist)):
        if '\n' in templist[j]:
            templist[j] = templist[j].replace('\n','')
        
        if templist[j].isdigit():
            temp = temp[:] + [templist[j]]

            
    upute = upute[:] + [temp]
    temp = []
    templist = []
print(upute)
korak = 0




for i in upute:
    korak += 1 
    print('korak: ', korak)
    n = int(i[0])
    iz = int(i[1])
    u = int(i[2])
    print(' n', n,'\n','iz', iz, '\n','u',u)
    print()
    print('c prije: ',c)
    print('---------------------------------------')
    for i in range(n):
        
        c[u-1].append(c[iz-1][-1])
        c[iz-1].pop()
        
    print('c nakon: ', c)
    print()


for i in c:
    print(i[-1])

