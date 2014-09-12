def cowsay(text):
    words = [w[i:i + 39] for w in text.split() for i in range(0, len(w), 39)]
    if text.startswith(' '):
        words.insert(0, '')
    if text.endswith(' '):
        words.append('')
    l, line = [], []
    for w in words:
        line.append(w)
        if len(' '.join(line)) > 39:
            l.append(' '.join(line[:-1]))
            line = [w]
    l.append(' '.join(line))
    maxle = max(len(s) for s in l)
    l = list(map(lambda _: _.ljust(maxle), l))
    res = ['\n ', '_' * (maxle + 2)]
    for i, s in enumerate(l):
        brackets = ('/\\', '||', '\\/', '<>')[3 if len(l) < 2 else (i > 0) + (i == len(l) - 1)]
        res.extend(('\n', brackets[0], ' ', s, ' ', brackets[1]))
    res.extend(('\n ', '-' * (maxle + 2), r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''))
    return ''.join(res)