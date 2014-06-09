def fibonacii(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacii(n-1)+fibonacii(n-2)

def checkio(opacity):
    if opacity == 10000:
        return 0
    sum = 10000
    fi = 2
    f = fibonacii(fi)
    i = 1
    while(sum != opacity):
        if i == f:
            sum = sum - i
            fi = fi + 1
            f = fibonacii(fi)
        else:
            sum = sum + 1
        i = i + 1
    return i - 1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
