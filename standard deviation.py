from functools import reduce
from math import sqrt
n = int(input())
nums = [int(i) for i in input().split(" ") ]
mean = sum(nums)/n
stan = reduce(lambda x,y: x+y,map(lambda x: (x-mean)*(x-mean),nums))
print("%.1f"%sqrt(stan/n))