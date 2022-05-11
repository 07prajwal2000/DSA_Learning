def compute_gcd(x, y): # HCF

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y): # LCM
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = 54
num2 = 24 

print("The L.C.M. is", compute_lcm(num1, num2))