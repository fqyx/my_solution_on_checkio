VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

def sp(t):
    ws = []
    w = ""
    for c in t:
        if c.isalpha() or c.isdigit():
            w = w + c
        else:
            if w != "":
                ws.append(w)
                w = ""
    if w:
        ws.append(w)
    result = [a for a in ws if a.isalpha()]
    print result
    return result

def if_VOWELS(w):
    for c in w:
        if VOWELS.find(c.upper()) == -1:
            return False
    return True

def if_CONSONANTS(w):
    for c in w:
        if CONSONANTS.find(c.upper()) == -1:
            return False
    return True

def if_strip(w):
    l = len(w)
    if l == 1:
        return False
    e = [w[i] for i in range(0,l,2)]
    o = [w[i] for i in range(1,l,2)]
    if (if_CONSONANTS(e) and if_VOWELS(o)) or (if_CONSONANTS(o) and if_VOWELS(e)):
        return True
    else:
        return False

def checkio(text):
    count = 0
    print sp(text)
    for w in sp(text):
        if if_strip(w):
            count = count + 1
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio("1st 2a ab3er root rate")
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
