def checkio(expression):
   s = ''.join([c for c in expression if c in '[]{}()'])
   for i in range(1000):
      s = s.replace('()', '').replace('[]', '').replace('{}', '')
   return s == ''
