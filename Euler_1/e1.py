def multiplies(_max=1):
    return sum([num for num in range(1, _max)
                if num % 3 == 0 or num % 5 == 0])
