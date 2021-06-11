# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input('enter 1st number to find lcm'))
num2 = int(input('enter 2nd number to find lcm'))

print("The L.C.M. is", compute_lcm(num1, num2))