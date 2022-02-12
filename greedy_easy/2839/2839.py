N = int(input())

result = 0
while True:
    if N % 5 != 0:
        N -= 3
        result += 1
        continue
    result += N // 5
    break

if N < 0:
    print(-1)
else:
    print(result)