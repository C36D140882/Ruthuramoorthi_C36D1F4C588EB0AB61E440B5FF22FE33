# 1.1 implement a recurstve function to calculate the factorial of a given number.

def fact_res(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_res(n-1)

number = 2
res = fact_res(number)

print("the factorial of {} is {}.".format(number,res))
    
    