from functools import reduce
n = int(input())
nums = [int(i) for i in input().split(" ") ]
weights = [float(i) for i in input().split(" ") ]
mean = reduce(lambda x,y: x+y,map( lambda x: x[0]*x[1],zip(nums,weights)))/sum(weights)
print("%.1f" % mean)