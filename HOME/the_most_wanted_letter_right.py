def checkio(text):
   text = text.lower();
   t = [x for x in text if x.isalpha()]
   from collections import Counter
   def compare(x,y):
      if x[1] > y[1]:
      return 1;
      elif x[1] < y[1]:
      return -1
      elif x[0] > y[0]:
      return -1
      else:
      return 1
   l=Counter(t).most_common();
   l.sort(compare,None,True)
   return l[0][0]

if __name__ == '__main__':
#These "asserts" using only for self-checking and not necessary for auto-testing
   assert checkio(u"Hello World!") == "l", "Hello test"
   assert checkio(u"How do you do?") == "o", "O is most wanted"
   assert checkio(u"One") == "e", "All letter only once."
   assert checkio(u"Oops!") == "o", "Don't forget about lower case."
   assert checkio(u"AAaooo!!!!") == "a", "Only letters."
   assert checkio(u"abe") == "a", "The First."
   print("Start the long test")
   assert checkio(u"a" * 9000 + u"b" * 1000) == "a", "Long."
   print("The local tests are done.")
