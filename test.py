print("Hello World")
f = open("math.txt")
a = f.readlines()
i = 0
sum = 0
prod = 1
while i < 4:
#    print(a[i])
    sum+=int(a[i])
    prod*=int(a[i])
    i+=1
print("Sum =",sum)
print("Prod =",prod)
