nums = [2, 1, 5, 1, 3, 2]
target = 7
result = []
for i in range(len(nums)):
    sum = 0
    sub = []
    for j in range(i, len(nums)):
        sum += nums[j]
        sub.append(nums[j])
        if sum >= target:
            result.append(sub[:])
            break 
print(result)