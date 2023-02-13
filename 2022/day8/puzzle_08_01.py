import numpy as np
my_file = open('trees real.txt','r')


data = my_file.read().split('\n')


data_int = []
for i in data:
    data_int.append(int(i))

#print(data_int)
temp = []
trees = []
cond = 0
for i in range(len(data_int)):
    for j in data[i]:
        temp.append(j)
    
    trees.append(temp)
    temp = []


trees = np.array(trees)
tree_count = 0
for red in range(len(trees)):
    for stupac in range(len(trees[red])):

        if red == 0:
            tree_count += 1
            print(f'index: {red,stupac}',trees[red,stupac], 'na gornjem rubu')
            continue

        elif stupac == 0:
            tree_count += 1
            print(f'index: {red,stupac}',trees[red,stupac], 'na lijevom rubu')
            continue

        elif red == (len(trees)-1):
            tree_count += 1
            print(f'index: {red,stupac}',trees[red,stupac], 'na donjem rubu')
            continue
            
        elif stupac == (len(trees[red])-1):
            tree_count += 1
            print(f'index: {red,stupac}',trees[red,stupac], 'na desnom rubu')
            print()
            continue
            
        
        for g in range(stupac):  # kontrola pogleda s lijeva
            
            if int(trees[red,g]) > cond:
                cond = int(trees[red,g])  
                if cond >  (int(trees[red,stupac])):
                    break
            

        if cond < int(trees[red,stupac]):
            tree_count += 1
            print(f'index: {red,stupac}',trees[red,stupac],'s lijeva')
            cond = 0
            continue
        
        cond = 0
        
        for h in range((len(trees[red])-1),stupac,-1): # kontrola pogleda s desna
            
            if int(trees[red,h]) > cond:
                cond = int(trees[red,h])
                if cond > (int(trees[red,stupac])):
                    break

            
        if cond < (int(trees[red,stupac])):
            tree_count += 1
            print(f'index: {red,stupac}',trees[red,stupac],'s desna')
            cond = 0
            continue
    
        cond = 0
           
        
        for k in range(red): #kontrola pogleda odozgo
            if int(trees[k,stupac]) > cond:
                cond = int(trees[k,stupac])
                if cond > int(trees[red,stupac]):
                    break
        
        if cond < int(trees[red,stupac]):
            tree_count += 1
            print(f'index: {red,stupac}',trees[red,stupac],'odozgo')
            cond = 0
            continue
        
        cond = 0

        for l in range((len(trees)-1),red,-1): #kontrola odozdo
            if int(trees[l,stupac]) > cond:
                cond = int(trees[l,stupac])
                if cond > int(trees[red,stupac]):
                    break

        if cond < int(trees[red,stupac]):
            tree_count += 1
            print(f'index: {red,stupac}',trees[red,stupac],'odozdo')
            cond = 0
            continue
        
        cond = 0

print('tree_count:', tree_count)

