nums = [10, 20, 30, 40, 50, 60, 70, 80]
ranges = [(1, 4), (3, 6), (5, 8)]
lst = []
for m, n in ranges:
    lst.extend(nums[m:n])
lst = list(dict.fromkeys(lst))
print(lst)