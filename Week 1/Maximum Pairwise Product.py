# Uses python3
import sys
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0

# for i in range(0, n):
#     for j in range(i+1, n):
#         if a[i]*a[j] > result:
#             result = a[i]*a[j]
a.sort()

result = a[len(a)-1] * a[len(a)-2]

print(result)
