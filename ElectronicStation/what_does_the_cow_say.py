COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
def text2arr(text):
    lines = []
    start_space_len = len(text) - len(text.lstrip())
    if start_space_len > 1:
        start_space_len = 1
    end_space_len = len(text) - len(text.rstrip())
    if end_space_len > 1:
        end_space_len = 1
    l = " " * start_space_len
    llen = start_space_len
    for w in text.split():
        if l:
            if len(w) + 1 + llen > 39:
                lines.append(l)
                if len(w) > 39:
                    while(len(w) > 39):
                        lines.append(w[0:39])
                        w = w[39:]
                    l = w
                else:
                    l = w
                    llen = len(w)
            else:
                llen = llen + len(w) + 1
                if l[-1] == " ":
                    l = l + w
                else:
                    l = l + " " + w
        else:
            if len(w) + llen > 39:
                if len(w) > 39:
                    while(len(w) > 39):
                        lines.append(w[0:39])
                        w = w[39:]
                    l = w
                else:
                    l = w
                    llen = len(w)
            else:
                llen = llen + len(w)
                l = l + w
    lines.append(l + " " * end_space_len)
    max_len = reduce(lambda x,y: x if x > y else y, [len(lll) for lll in lines], 0)
    if len(lines) == 1:
        return lines
    else:
        return [l + (max_len - len(l)) * ' ' for l in lines]
def wrap(arr):
    head = "\n _" + len(arr[0])* "_" + "_\n"
    tail = " -" + len(arr[0])* "-" + "-"
    if len(arr) == 1:
        return head + "< " + arr[0] + " >\n"+tail+COW
    else:
        first =  "/ " + arr[0] + " \\"+"\n"
        last =  '\\ ' + arr[len(arr)-1] + r' /'+"\n"
        mid =""
        for e in arr[1:-1]:
            l = "| "+e+" |\n"
            mid = mid + l
    return head + first + mid + last + tail +COW
def cowsay(text):
    return wrap(text2arr(text))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    #assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line
    #assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s%s' % (cowsay_one_line,expected_cowsay_one_line)
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % expected_cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s%s' % (cowsay_two_lines,expected_cowsay_two_lines)

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
