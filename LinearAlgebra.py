
matrix = [
	[1,1,1,0,0,0,0,0,0],
	[0,0,0,1,1,1,0,0,0],
	[0,0,0,0,0,0,1,1,1],
	[1,0,0,1,0,0,1,0,0],
	[0,1,0,0,1,0,0,1,0],
	[0,0,1,0,0,1,0,0,1],
	[1,0,0,0,1,0,0,0,1],
	[0,1,0,0,0,1,1,0,0],
	[0,0,1,1,0,0,0,1,0],
	[1,0,0,0,0,1,0,1,0],
	[0,1,0,1,0,0,0,0,1],
	[0,0,1,0,1,0,1,0,0]
]


def basis_over_n_field(matrix: list[list[int]], field: int) -> list[list[int]]:
	basis = list(matrix)
	rows_in_basis = []

	row, col = 0, 0

	while len(basis[0]) > col:
		row = find_leading_one_in_col(basis, col)
		if row > -1:
			rows_in_basis.append(row)
			if basis[row][col] > 1:
				basis[row] = reduce_row_by_scalar(basis[row], col, field)
			for row_index in range(len(basis)):
				if row_index == row:
					continue
				basis[row_index] = reduce_row_by_row(basis[row_index], basis[row], field)

		col += 1

	rows_in_basis.sort()
	cleaned_matrix = [matrix[i] for i in rows_in_basis]

	return cleaned_matrix


def reduce_row_by_row(row_to_reduce: list[int], row_reducer: list[int], field: int) -> list[int]:
	col_to_reduce = 0
	for col in range(len(row_reducer)):
		if row_reducer[col] != 0:
			col_to_reduce = col
			break

	while row_to_reduce[col_to_reduce] != 0:
		row_to_reduce = [(row_to_reduce[i] + row_reducer[i])%field for i in range(len(row_reducer))]

	return row_to_reduce


def reduce_row_by_scalar(row_to_reduce: list[int], leading_num: int, field: int) -> list[int]:
	scalar = row_to_reduce[leading_num]
	while row_to_reduce[leading_num] != 1:
		row_to_reduce = [(x + scalar)%field for x in row_to_reduce]

	return row_to_reduce


def find_leading_one_in_col(matrix: list[list[int]], col: int) -> int:
	for row in range(len(matrix)):
		if matrix[row][col] > 0 and sum(matrix[row][:col]) == 0:
			return row
	return -1


if __name__ == "__main__":
	row_reduced = basis_over_n_field(matrix, 2)
	for row in row_reduced:
		print(row)