def checkio(number):
    sum = 0
    i = 1
    p = 0
    while(sum < number):
        p = i*(i+1)/2
        sum = sum + p
        i = i +1

    if (sum - number) >= i-1:
        return (i - 2+1)*(i-2)/2
    else:
        return p - (sum - number)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
