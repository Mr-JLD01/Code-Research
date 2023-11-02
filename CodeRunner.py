from MutuallyOrthogonalLatinSquares import MutuallyOrthogonalLatinSquares
from QaryLatinSquare import QaryLatinSquare
from LatinSquare import LatinSquare
from LinearCode import LinearCode
from LinearAlgebra import basis_over_n_field, transpose


def latin_square_to_code(ls: LatinSquare) -> LinearCode:
    codewords = []

    for row in range(ls.size):
        for col in range(ls.size):
            codewords.append(str(row) + str(col) + str(ls.square[row][col]))

    return LinearCode(codewords)


def mols_to_code(mols: MutuallyOrthogonalLatinSquares) -> LinearCode:
    codewords = []

    for row in range(mols.dimension):
        for col in range(mols.dimension):
            codeword = ""
            for elem in mols.matrix[row][col]:
                codeword += str(elem)
            codewords.append(str(row) + str(col) + codeword)

    return LinearCode(codewords)


def matrix_to_code(matrix: list[list[int]], field: int) -> LinearCode:
    generator_matrix = basis_over_n_field(matrix, field)
    codewords = []

    # adding basis
    for row in generator_matrix:
        codeword = ""
        for elem in row:
            codeword += str(elem)
        codewords.append(codeword)

    print("Basis converted")
    print("Making {} codewords".format(field**len(generator_matrix)))
    # adding scalars of basis
    for scalar in range(field):
        for word in codewords:
            codeword = LinearCode.scalar_mult(word, scalar, field)
            codewords.append(codeword)

            # remove duplicates
            codewords = list(set(codewords))

    print("Scalars added")

    codewords = sorted(codewords)
    gen_list = list(codewords)

    print("Made {} codewords of {}".format(len(codewords), field**len(generator_matrix)))  # noqa

    base_list = len(codewords)
    full_list = base_list

    # adding linear combinations
    print("Number of loops to go through:: {}".format(base_list))
    for word1 in range(0, base_list):
        for word2 in range(word1 + 1, full_list):
            codeword = LinearCode.vector_add(codewords[word1], codewords[word2], field)  # noqa
            codewords.append(codeword)

        if word1 < base_list - 1:
            codewords = gen_list + remove_duplicates(codewords)
        else:
            codewords = remove_duplicates(codewords)
        full_list = len(codewords)

        print("Loop {}: Made {} codewords of {}".format(word1 + 1, full_list, field**len(generator_matrix)))  # noqa

    print("Combinations added")
    print("Making Code")

    return LinearCode(codewords)


def remove_duplicates(lst: list[any]) -> list[any]:
    lst = sorted(lst)
    cleaned_list = []
    length_cleaned = 0

    for elem in lst:
        if length_cleaned == 0 or elem != cleaned_list[length_cleaned - 1]:
            cleaned_list.append(elem)
            length_cleaned += 1

    return cleaned_list


if __name__ == "__main__":
    error_message = "Not a Code"
    generates = "=======> Generates =======>\n"
    input_message = "Continue on? [y/n]"

    matrix = [
        [1, 1, 0, 0],
        [1, 0, 1, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 1]
    ]

    # test_code = matrix_to_code(matrix, 2)
    # print(test_code)

    # input()

    matrix = [
    [1, 1, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 1, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 1, 1],
	[1, 0, 0, 1, 0, 0, 1, 0, 0],
	[0, 1, 0, 0, 1, 0, 0, 1, 0],
	[0, 0, 1, 0, 0, 1, 0, 0, 1],
	[1, 0, 0, 0, 1, 0, 0, 0, 1],
	[0, 1, 0, 0, 0, 1, 1, 0, 0],
	[0, 0, 1, 1, 0, 0, 0, 1, 0],
	[1, 0, 0, 0, 0, 1, 0, 1, 0],
	[0, 1, 0, 1, 0, 0, 0, 0, 1],
	[0, 0, 1, 0, 1, 0, 1, 0, 0]
    ]

    test_code = matrix_to_code(matrix, 2)
    print(test_code)

    matrix = transpose(matrix)

    test_code = matrix_to_code(matrix, 2)
    print(test_code)

    matrix.append([1]*(len(matrix[0])))

    test_code = matrix_to_code(matrix, 2)
    print(test_code)

    matrix = [
            [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0]]

    # test_code = matrix_to_code(matrix, 2)
    # print(test_code)

    matrix = [
        # horiz lines
        # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        # vert lines
        # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        # y=x+c lines
        # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        # y=4x+c lines
        # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        # y=2x+c lines
        # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        # y=3x+c lines
        # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
    ]

    # test_code = matrix_to_code(matrix, 2)
    # print(test_code)

    matrix = [
        [1, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1]
    ]

    t_mat = transpose(matrix)

    # test_code = matrix_to_code(matrix, 2)
    # print(test_code)

    matrix = [
        [1, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1]
    ]

    test_code = matrix_to_code(matrix, 2)
    print(test_code)

    # test_code = matrix_to_code(t_mat, 2)
    # print(test_code)


    # answer = ""
    # while (answer != "y"):
    #     for q in range(2, 9):
    #         input()
    #         print("\n"*100)
    #         test_ls = QaryLatinSquare(q)
    #         print(test_ls)
    #         print(generates)
    #         test_code = latin_square_to_code(test_ls)
    #         print(test_code)
    #     answer = input("Continue on? [y/n] :: ")

    # for order in range(3, 9, 2):
    #     answer = ""
    #     while (answer != "y"):
    #         for i in range(2, order):
    #             input()
    #             print("\n"*100)
    #             mols = [LatinSquare(ls) for ls in MutuallyOrthogonalLatinSquares.find_mutually_orthogonal_latin_squares(order, i)]  # noqa
    #             mols_test = MutuallyOrthogonalLatinSquares(mols)  # noqa
    #             print(mols_test)
    #             print(generates)
    #             test_code = mols_to_code(mols_test)
    #             print(test_code)
    #         answer = input("Continue on? [y/n] :: ")

    # # NOTE - Examples of not all MOLS create codes

    # input()
    # print("\n"*100)
    # try:
    #     square1 = LatinSquare([[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]])  # noqa
    #     square2 = LatinSquare([[0, 1, 2, 3], [3, 2, 1, 0], [1, 0, 3, 2], [2, 3, 0, 1]])  # noqa

    #     mols_4_test = MutuallyOrthogonalLatinSquares([square1, square2])  # noqa
    #     print(mols_4_test)
    #     print(generates)
    #     test_code = mols_to_code(mols_4_test)
    #     print(test_code)
    # except AssertionError:
    #     print(error_message)

    # input()
    # print("\n"*100)
    # try:
    #     square1 = LatinSquare([[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]])  # noqa
    #     square2 = LatinSquare([[0, 1, 2, 3], [2, 3, 0, 1], [3, 2, 1, 0], [1, 0, 3, 2]])  # noqa

    #     mols_4_test = MutuallyOrthogonalLatinSquares([square1, square2])  # noqa
    #     print(mols_4_test)
    #     print(generates)
    #     test_code = mols_to_code(mols_4_test)
    #     print(test_code)
    # except AssertionError:
    #     print(error_message)
