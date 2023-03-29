def twoSum(nums):
	dic = {}
	for n, i in enumerate(nums):
            compliment = target-i
            if i in dic:
                return [n,dic[i]]
            else:
                dic[compliment] = n

nums = [2,7,11,15]
target = 9
output = [0,1]

twoSum(nums)
                