def checkio(data):
    if len(data)<10:
        return False
    has_digit = False
    for i in "0123456789":
        if data.find(i) != -1:
            has_digit=True
            break;
    new_data=data.swapcase()
    if new_data == data.upper() or new_data == data.lower():
        return False
    else:
        return has_digit

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u'A1213pokl') == False, "1st example"
    assert checkio(u'bAse730onE4') == True, "2nd example"
    assert checkio(u'asasasasasasasaas') == False, "3rd example"
    assert checkio(u'QWERTYqwerty') == False, "4th example"
    assert checkio(u'123456123456') == False, "5th example"
    assert checkio(u'QwErTy911poqqqq') == True, "6th example"
