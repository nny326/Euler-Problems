"""
  Problem 5:  
 
  Desc.:  2520 is the smallest number that can be divided by each of the numbers
   from 1 to 10 without any remainder.

  Problem:  What is the smallest positive number that is evenly divisible by all of
   the numbers from 1 to 20?

"""

x, factors, num = 1, list(range(1,11)), 0

while (num == 0):
  for factor in factors:
    mul = x/factor
    if not mul.is_integer():
      x += 1
      # print(x)
      break
    elif factor == factors[-1]:
      num = x

print(num)