#A fixed point in a list is where the value is equal to its index. So for example the list [-5, 1, 3, 4], 1 is a fixed point in the list since the index and value is the same.
# Find a fixed point (there can be many, just return 1) in a sorted list of distinct elements, or return None if it doesn't exist.


def find_fixed_point(nums):
  for i in range(len(nums)):
      if i == nums[i]:
          return 1
print (find_fixed_point([-5, 1, 3, 4]))
# 1