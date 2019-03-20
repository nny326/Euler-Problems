'''
PROBLEM 1:  Multiples of 3 and 5

Desc:   If we list all the natural  numbers below 10 that are
multiples of 3 and 5, we get 3, 5, 6 and 9. The sum of these multiples is 
23. 

Problem: Find the sum of all the multiples of 3 and 5 below 1000
'''
sum = 0
for x in range(1000):
    if (x % 3 == 0) or (x % 5 == 0):
        sum += x

print(sum)