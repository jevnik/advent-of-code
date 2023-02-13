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

best_index = (0,0)
cur_index = (0,0)
score_left = 0
score_right = 0
score_up = 0
score_down = 0
scoreboard = {}

for red in range(len(trees)):
    for stupac in range(len(trees[red])):
        if red != 0 and stupac != 0 and red != (len(trees)-1) and stupac != (len(trees[red])-1):
            #print()
            #print('index:',(red,stupac),'trenutna celija: ',trees[red,stupac])
            
            for g in range(stupac-1,-1,-1):  # kontrola lijeve strane
                
                #print('od trenutnog ulijevo',trees[red,g])

                if int(trees[red,g]) >= int(trees[red,stupac]):
                    score_left += 1
                    break

                if int(trees[red,g]) < int(trees[red,stupac]):
                    score_left += 1
            
            #print('score left',score_left)
            

            for g in range(stupac+1,len(trees[red])):  # kontrola desne strane
                
                #print('od trenutnog udesno',trees[red,g])

                if int(trees[red,g]) >= int(trees[red,stupac]):
                    score_right += 1
                    break

                if int(trees[red,g]) < int(trees[red,stupac]):
                    score_right += 1
            
            #print('score right',score_right)
            
        
            for g in range(red-1,-1,-1):  # kontrola iznad
                
                #print('od trenutnog iznad',trees[g,stupac])

                if int(trees[g,stupac]) >= int(trees[red,stupac]):
                    score_up += 1
                    break

                if int(trees[g,stupac]) < int(trees[red,stupac]):
                    score_up += 1
            
            #print('score up',score_up)

            
            for g in range(red+1,len(trees)):  # kontrola ispod
                
                #print('od trenutnog ispod',trees[g,stupac])

                if int(trees[g,stupac]) >= int(trees[red,stupac]):
                    score_down += 1
                    break

                if int(trees[g,stupac]) < int(trees[red,stupac]):
                    score_down += 1
            
            #print('score down',score_down)
            cur_index = (red,stupac)
            score = score_left * score_right * score_up * score_down
            scoreboard[cur_index] = score



            #print('score:',score)
            score_left = 0
            score_right = 0
            score_up = 0
            score_down = 0

#print(scoreboard)
print('max', max(scoreboard.values()))


