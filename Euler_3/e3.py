def prime_generator(num=600851475143):
    "Returns the largest prime factors of a given number"
    primefactors, product, org_num = [], 1, num
    for factor in range(2, org_num+1):
        while num % factor == 0:
            num = num//factor  # floored integer of division
            primefactors.append(factor)
            product *= factor

        if product == org_num:
            break

    return primefactors[-1] if len(primefactors) > 0 else 1
