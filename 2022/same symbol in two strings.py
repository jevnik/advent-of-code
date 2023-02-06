def findCommonSymbol(x,y):
    lista = []
    if len(x) > len(y):
        for i in x:
            if i in y:
                lista = lista[:] + [i]

    else:
        for i in y:
            if i in x:
                lista = lista[:] + [i]
    return lista

# b = 'abcd'
# a = 'abefgd'

# print(findCommonSymbol(a,b))

a = [1,2,3,4,5]

for i in range(len(a)-1):
    x = i+1
    print(i,x)