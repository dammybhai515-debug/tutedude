def fac_rec(num):
   if num == 1:
       return 1
   else:
       factorial = num * fac_rec (num - 1)
       return factorial
   
num=int(input("enter number fot factorial : "))
print(f"factorial for {num} is : {fac_rec(num)}")