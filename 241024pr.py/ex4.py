nums = [1, 2, 3, 4, 5, 6]
def squares(nums):
    return [n ** 2 for n in nums if n % 2 == 0] 
ans = squares(nums)
print(ans)
