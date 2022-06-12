f = open("text.txt")
a = f.read()
l = len(a)
r = 0
m = ""
while r < l:
    if a[r].isupper() == True:
        m = a[r] + m
    r+=1
print(m)

