def sum(nums, target):
    n = {} 
    for i, num in enumerate(nums):
        a = target - num 
        if a in n:
            return [n[a], i] 
        n[num] = i 
nums = [2,7,11,15]
target = 9
result = sum(nums, target)
print(result)