"""
  Problem 4:
 
  Desc.: A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 × 99.

  Problem: Find the largest palindrome made from the product of two 3-digit numbers.

"""

palindrome = 0

for x in range(10, 1000):
  for y in range(10, 1000):
    product = str(x * y)
    if ((product[::] == product[::-1]) and (int(product) > palindrome)):
      palindrome, num1, num2 = int(product), x, y


print('{0} = {1} * {2}'.format(palindrome, num1, num2))