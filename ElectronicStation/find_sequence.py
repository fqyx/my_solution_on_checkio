def has_rep(arr, l):
   if l < 4:
      return False
   for i in range(0,l-3):
      if arr[i] == arr[i+1] and arr[i+1] == arr[i+2] and arr[i+2] == arr[i+3]:
         return True
   return False

def checkio(matrix):
   l = len(matrix)
   is_exists = False
   for i in range(0,l):
      if has_rep(matrix[i],l):
         return True
   for i in range(0,l):
      if has_rep([matrix[j][i] for j in range(0,l)],l):
         return True
   for i in range(0,l-3):
      for j in range(0,l-3):
         if has_rep([matrix[i+c][j+c] for c in range(0,4)], 4):
            return True
   for i in range(0,l-3):
      for j in range(l-1,2,-1):
         if has_rep([matrix[i+c][j-c] for c in range(0,4)], 4):
            return True
   return False

if __name__ == '__main__':
#These "asserts" using only for self-checking and not necessary for auto-testing
   assert checkio([
                  [1, 2, 1, 1],
                  [1, 1, 4, 1],
                  [1, 3, 1, 6],
                  [1, 7, 2, 5]
                  ]) == True, "Vertical"
   assert checkio([
                  [7, 1, 4, 1],
                  [1, 2, 5, 2],
                  [3, 4, 1, 3],
                  [1, 1, 8, 1]
                  ]) == False, "Nothing here"
   assert checkio([
                  [2, 1, 1, 6, 1],
                  [1, 3, 2, 1, 1],
                  [4, 1, 1, 3, 1],
                  [5, 5, 5, 5, 5],
                  [1, 1, 3, 1, 1]
                  ]) == True, "Long Horizontal"
   assert checkio([
                  [7, 1, 1, 8, 1, 1],
                  [1, 1, 7, 3, 1, 5],
                  [2, 3, 1, 2, 5, 1],
                  [1, 1, 1, 5, 1, 4],
                  [4, 6, 5, 1, 3, 1],
                  [1, 1, 9, 1, 2, 1]
                  ]) == True, "Diagonal"
