def weak_point(matrix):
   weak_row_index = min([(i, sum(row)) for i, row in enumerate(matrix)], key=lambda x: x[1])[0]
   weak_col_index = min([(i, sum([row[i] for row in matrix])) for i in xrange(len(matrix[0]))], key=lambda x: x[1])[0]
   return weak_row_index, weak_col_index
