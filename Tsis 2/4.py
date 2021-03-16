n = [int(i) for i in input().split()]
s = 0
l = []
l.append(s)
for i in n:
    s = s + i
    l.append(s)
mini = l[0]
for j in l:
    if j > mini:
        mini = j
print(mini)
