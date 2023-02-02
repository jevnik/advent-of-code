with open('advent of code\\2021\\day1\\input_2.txt') as depth:
    depth = depth.read().splitlines()
    curr_sum = 0
    depth_sum = []

    for i in range(2,len(depth)):
        for j in range(i-2,i+1):
            curr_sum += int(depth[j])
        
        depth_sum.append(curr_sum)
        curr_sum = 0
        
    count = 0
    curr = 0

    for d in depth_sum:
        if int(d) > curr:
            count +=1
            curr = int(d)
        curr = int(d)

    print(count-1)