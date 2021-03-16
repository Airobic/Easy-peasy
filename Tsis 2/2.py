n = input()
s = ""
for i in range(len(n)):
    if n[i] == "(" and n[i+1] == ")":
        s = s + "o"
    elif n[i] == "(" or n[i] == ")":
        s =s + ""
    else:
        s = s + n[i]
print(s)
