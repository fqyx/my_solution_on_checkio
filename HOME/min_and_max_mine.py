def min(*args, **kwargs):
    key = kwargs.get("key", None)
    print type(args)
    print len(args)
    if len(args) > 1:
        m = args[0]
        mv = key(m) if key else m
        for e in args:
            temp = key(e) if key else e
            if temp < mv:
                m = e
                mv = temp
        return m
    else:
        i = 0
        for e in args[0]:
            temp = key(e) if key else e
            if i == 0:
                mv = temp
            if temp < mv :
                m = e
                mv = temp
            i = i+1
        return m

def max(*args, **kwargs):
    key = kwargs.get("key", None)
    print type(args)
    print len(args)
    if len(args) > 1:
        m = args[0]
        mv = key(m) if key else m
        for e in args:
            temp = key(e) if key else e
            if temp > mv:
                m = e
                mv = temp
        return m
    else:
        i = 0
        for e in args[0]:
            temp = key(e) if key else e
            if i == 0:
                mv = temp
            if temp > mv:
                m = e
                mv = temp
            i = i+1
        return m

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    min(abs(i) for i in range(-10, 10))
