n = [int(i) for i in input().split()]
cnt = 0
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] == n[j] and i < j:
            cnt += 1
print(cnt)

