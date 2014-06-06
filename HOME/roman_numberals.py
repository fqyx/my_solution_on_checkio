def checkio(data):

    s = ''
    ones = ['X','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    tens = ['C', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    mils = ['M', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

    if data / 1000 != 0:
        s = s + 'M'*(data/1000)
        data = data % 1000
    if data / 100 != 0:
        s = s + mils[data/100]
        data = data % 100
    if data / 10 != 0:
        s = s + tens[data/10]
        data = data % 10
    if data / 1 != 0:
        s = s + ones[data/1]
    return s

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
