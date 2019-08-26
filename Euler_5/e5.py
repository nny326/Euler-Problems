def all_divisible():
    X, FACTORS, NUM = 1, list(range(1, 11)), 0
    while NUM == 0:
        for factor in FACTORS:
            mul = X/factor
            if not mul.is_integer():
                X += 1
                break
            elif factor == FACTORS[-1]:
                NUM = X
        return NUM