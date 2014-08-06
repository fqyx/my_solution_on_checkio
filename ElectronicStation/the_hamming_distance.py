def checkio(n, m):
   count = 0
   while n > 0 or m > 0:
      if n % 2 != m % 2:
         count = count + 1
      n = n / 2
      m = m / 2
   return count

if __name__ == '__main__':
#These "asserts" using only for self-checking and not necessary for auto-testing
   assert checkio(117, 17) == 3, "First example"
   assert checkio(1, 2) == 2, "Second example"
   assert checkio(16, 15) == 5, "Third example"
