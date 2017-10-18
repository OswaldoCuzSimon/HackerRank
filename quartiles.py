n = int(input())
nums = [int(i) for i in input().split(" ") ]
nums.sort()
q1 = (n * 1)/4
q2 = n/2
q3 = (n * 3)/4
q1 = nums[int(q1)] if n%2 == 0 else (nums[int(q1)] + nums[int(q1)-1] ) / 2
q3 = nums[int(q3)] if n%2 == 0 else (nums[int(q3)] + nums[int(q3)+1 ])/ 2
q2 = (nums[int(n/2)] + nums[int(n/2) - 1])/2 if n%2 == 0 else  nums[int(n/2)]
print("%d\n%d\n%d" % (q1, q2, q3))