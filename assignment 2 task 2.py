a=int(input("enter number you want to start "))
   
b=int(input("enter number you want to end "))
sum=0
print (type (a))
for i in range (a,b+1):
    print (i)
for i in range (a,b+1):
    sum += i

print (f"sum of value for {a} to {b} is {sum}")
