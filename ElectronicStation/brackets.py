def checkio(expression):
   stack = []
   left = ['(','[','{']
   right = [')',']','}']
   for c in expression:
      if c in left:
         stack.append(c)
      elif c in right:
         try:
            top = stack.pop()
         except IndexError:
            print "Error Caught!"
            return False
         if left.index(top) != right.index(c):
            return False
      else:
         pass
   if len(stack) == 0:
      return True
   else:
      return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
   assert checkio(u"((5+3)*2+1)") == True, "Simple"
   assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
   assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
   assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
   assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
   assert checkio(u"2+3") == True, "No brackets, no problem"
