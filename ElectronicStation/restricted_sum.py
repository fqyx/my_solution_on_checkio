def checkio(data):
   sss = lambda a: a[0] if len(a) == 1 else sss(a[1:])+a[0]
   return sss(data)
