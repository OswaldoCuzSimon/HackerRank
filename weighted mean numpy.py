import numpy as np
n = int(input())
nums = np.array([int(i) for i in input().split(" ") ])
weights = np.array([float(i) for i in input().split(" ") ])
mean = sum(nums*weights)/sum(weights)
print("%.1f" % mean)