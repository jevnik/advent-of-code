my_file = open('datastream_real.txt','r')
data = my_file.read()
letters = []

for i in data:
    letters = letters[:] + [i]

print(letters)
temp = []
counter = 13

for i in range(13,len(letters),1):
    counter += 1
    temp = temp[:] + letters[i-13:i+1]
    print(temp)
    temp_set = set(temp)
    print(temp_set)
    if len(temp) == len(temp_set):
        print('Nasao pocetak', counter)
        
        
        break
    temp = []

