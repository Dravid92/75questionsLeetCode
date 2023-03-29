def containsDuplicate(nums):
	dummy_dic = {}
	for i in nums:
		dummy_dic[i] = i
		if len(nums) > len(dummy_dic):
			return True
		else:
			return False

nums = [1,2,3,1]
output = true

contrainsDuplicate(nums)