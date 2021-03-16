n = input()
s = ""
for i in n:
    if i == ".":
        s = s + "[.]"
    else:
        s = s + i
print(s)
