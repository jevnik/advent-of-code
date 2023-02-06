a = [1,2,2,3]

def removeDuplicates(nums: list[int]) -> int:
    prvi = 0
    for drugi in range(1,len(nums)):
        
        if nums[prvi] == nums[drugi]:
            nums[prvi] = nums[drugi]
        else:
            
            prvi += 1
            nums[prvi] = nums[drugi]

            
    print(nums)
    return (drugi +1)
removeDuplicates(a)             
print(a)