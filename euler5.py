"""
Problem 5:
  Desc.:  2520 is the smallest NUMber that can be divided by each of the NUMbers \
      from 1 to 10 without any remainder.
  Problem:  What is the smallest positive NUMber that is evenly divisible by all of \
      the NUMbers from 1 to 20?
"""
X, FACTORS, NUM = 1, list(range(1, 11)), 0

while NUM == 0:
    for factor in FACTORS:
        mul = X/factor
        if not mul.is_integer():
            X += 1
            # print(X)
            break
        elif factor == FACTORS[-1]:
            NUM = X

print(NUM)
