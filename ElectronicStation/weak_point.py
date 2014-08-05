def weak_point(matrix):
   x_min = 0
   y_min = 0
   durablity_row_min = sum(matrix[0])
   durablity_col_min = (lambda x : sum([row[x] for row in matrix]))(0)
   for i in range(len(matrix) - 1):
      durablity_row = sum(matrix[i+1])
      if durablity_row_min > durablity_row:
         durablity_row_min = durablity_row
         y_min = i + 1
         #print "row:%d %d " % (durablity_row_min, y_min)
   for i in range(len(matrix) - 1):
      durablity_col = (lambda x : sum([row[x] for row in matrix]))(i+1)
      if durablity_col_min > durablity_col:
         durablity_col_min = durablity_col
         x_min = i + 1
         #print "col:%d %d " % (durablity_col_min, x_min)
   return y_min, x_min# [0, 0]


if __name__ == '__main__':
   #These "asserts" using only for self-checking and not necessary for auto-testing
   assert isinstance(weak_point([[1]]), (list, tuple)), "The result should be a list or a tuple"
   assert list(weak_point([[7, 2, 7, 2, 8],
                          [2, 9, 4, 1, 7],
                          [3, 8, 6, 2, 4],
                          [2, 5, 2, 9, 1],
                          [6, 6, 5, 4, 5]])) == [3, 3], "Example"
   assert list(weak_point([[7, 2, 4, 2, 8],
                          [2, 8, 1, 1, 7],
                          [3, 8, 6, 2, 4],
                          [2, 5, 2, 9, 1],
                          [6, 6, 5, 4, 5]])) == [1, 2], "Two weak point"
   assert list(weak_point([[1, 1, 1],
                          [1, 1, 1],
                          [1, 1, 1]])) == [0, 0], "Top left"
