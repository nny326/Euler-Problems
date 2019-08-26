def palindromer(length=3):
    palindromed = [0]
    length = 10**length
    for x in range(length, 9, -1):
        for y in range(length, 9, -1):
            product = str(x * y)
            if (product[::] == product[::-1]):
                palindromed.append(int(product))
                # palindromed.append((int(x*y), x, y))
    return max(palindromed)