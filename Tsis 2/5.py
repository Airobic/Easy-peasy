n = int(input())
m = str(n)
l = []
for i in range(len(m)):
    l.append(m[i])
cnt = 1
sum = 0
for i in range(len(l)):
    l[i] = int(l[i])
    cnt = cnt * l[i]
    sum = sum + l[i]
print(cnt - sum)
