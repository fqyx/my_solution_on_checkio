def checkio(matrix):
   N = len(matrix)
   def seq_len(x, y, dx, dy, num):
      if 0 <= x < N and 0 <= y < N and matrix[y][x] == num:
      return 1 + seq_len(x + dx, y + dy, dx, dy, num)
      else:
         return 0

   DIR = [(dx, dy) for dy in range(-1, 2)
   for dx in range(-1, 2)
      if dx != 0 or dy != 0]
      for y in range(N):
         for x in range(N):
            for dx, dy in DIR:
            if seq_len(x, y, dx, dy, matrix[y][x]) >= 4:
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
