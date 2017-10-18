from collections import Counter
n = int(input())
nums = [int(i) for i in input().split(" ") ]
mean = sum(nums)/n
nums.sort()
median = (nums[int(n/2)] +nums[int(n/2)-1])/2 if n %2 == 0 else nums[int(n/2)]

counter = Counter(nums)
maxi = max(counter.values())
modes = [k for k,v in counter.items() if v == maxi]
modes.sort()
mode = modes[0]
print(mean)
print(median)
print(mode)
