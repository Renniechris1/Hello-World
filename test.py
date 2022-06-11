print("Hello the sum of all variables is")
f = open("math.txt")
a = f.readlines()
i = 0
sum = 0
while i < 4:
#    print(a[i])
    sum+=int(a[i])
    i+=1
print(sum)
