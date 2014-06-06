FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def two_digit(number):
    i = int(number)
    if i<20:
        return SECOND_TEN[i-10]
    else:
        s = ""
        if i % 10:
            s = s + (OTHER_TENS[i/10-2]+" ")
            s = s + (FIRST_TEN[i%10-1])
        else:
            s = OTHER_TENS[i/10-2]
        return s

def checkio(number):
    number = str(number)
    #replace this for solution
    if len(number) == 1:
        return FIRST_TEN[int(number)-1]
    elif len(number) == 2:
        return two_digit(number)
    elif len(number) == 3:
        i = int(number)
        if i % 100 == 0:
            return FIRST_TEN[i/100-1]+" "+HUNDRED
        elif i % 100 < 10:
            return FIRST_TEN[i/100-1]+" "+HUNDRED+" "+FIRST_TEN[i%100 - 1]
        else:
            return FIRST_TEN[i/100-1]+" "+HUNDRED+" "+two_digit(number[1:])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"'"
