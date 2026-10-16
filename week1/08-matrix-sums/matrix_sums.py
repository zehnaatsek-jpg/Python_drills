def matrix_sums(matrix):
  rows = []
  for row in matrix:
    rows.append(sum(row))

  columns = []
  nums = len(matrix[0]) if matrix else 0
  for column in range(nums):
    columns_sum = 0
    for row_mat in range(len(matrix)):
      columns_sum += matrix[row_mat][column]
    columns.append(columns_sum)
  matric = (rows, columns)
  return matric

