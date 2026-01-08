nums = [1, 6, 2, 10, 3]
target = 7

d = {}

for i in range(len(nums)):
    if target - nums[i] in d:
        print([d[target - nums[i]], i])
        break
    d[nums[i]] = i
