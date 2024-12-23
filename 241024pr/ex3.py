nums = [2, 7, 11, 15]
target = 9
n = {}
ans = None
for i, num in enumerate(nums):
    a = target - num
    if a in n:
        ans = [n[a], i]
        break
    n[num] = i
print(ans)