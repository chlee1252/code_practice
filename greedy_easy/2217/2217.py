# n = int(input())

# ropes = [int(input()) for _ in range(n)]
# ropes.sort(reverse=True)

# weights = []
# for index in range(n):
#     weights.append(ropes[index] * (index + 1))

# print(max(weights))

n = int(input())
k = [0] * 10001

for _ in range(n):
    k[int(input())] += 1

m,result = 0,0
for i in range(10000, 0,-1):
    if k[i] == 0:
        continue
    m += k[i]
    result = max(result, i * m)

print(result)