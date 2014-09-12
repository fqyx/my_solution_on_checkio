def checkio (number):
   digits = []
   while number > 9:
      can_be_found = False
      for i in range(9, 1, -1):
         if number % i == 0:
            digits.append(i)
            number = number / i
            can_be_found = True
            break
      if can_be_found == False:
         return 0
   digits.append(number)
   return int(reduce(lambda x,y:x+y, map(str, sorted(digits)), ""))

if __name__ == '__main__':
   #These "asserts" using only for self-checking and not necessary for auto-testing
   assert checkio(20) == 45, "1st example"
   assert checkio(21) == 37, "2nd example"
   assert checkio(17) == 0, "3rd example"
   assert checkio(33) == 0, "4th example"
   assert checkio(3125) == 55555, "5th example"
   assert checkio(9973) == 0, "6th example"
