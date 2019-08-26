def sum_even_fibonacci(max_value=4000000):
    N1, N2, SUM_ = 1, 2, 0

    while N1 < max_value:
        if N1 % 2 != 1:
            SUM_ += N1
        N3 = N2 + N1
        N1, N2 = N2, N3
    return SUM_
