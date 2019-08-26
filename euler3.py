"""
Problem 3:

Desc.:  The prime factors of 13195 are 5, 7, 13 and 29.

Problem:  What is the largest prime factor of the number 600851475143 ?

"""


def prime_generator(num):
    "Returns the largest prime factors of a given number"
    primefactors, product, org_num = [], 1, num
    for factor in range(2, org_num+1):
        while num % factor == 0:
            num = num//factor   #floored integer of division
            primefactors.append(factor)
            product *= factor

        if product == org_num:
            break

    return primefactors[-1]


print(prime_generator(600851475143))
