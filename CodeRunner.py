from MutuallyOrthogonalLatinSquares import MutuallyOrthogonalLatinSquares
from QaryLatinSquare import QaryLatinSquare
from LatinSquare import LatinSquare
from LinearCode import LinearCode


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


if __name__ == "__main__":
    error_message = "Not a Code"
    generates = "=======> Generates =======>\n"
    input_message = "Continue on? [y/n]"

    answer = ""
    while (answer != "y"):
        for q in range(2, 9):
            input()
            print("\n"*100)
            test_ls = QaryLatinSquare(q)
            print(test_ls)
            print(generates)
            test_code = latin_square_to_code(test_ls)
            print(test_code)
        answer = input("Continue on? [y/n] :: ")

    for order in range(3, 9, 2):
        answer = ""
        while (answer != "y"):
            for i in range(2, order):
                input()
                print("\n"*100)
                mols = [LatinSquare(ls) for ls in MutuallyOrthogonalLatinSquares.find_mutually_orthogonal_latin_squares(order, i)]  # noqa
                mols_test = MutuallyOrthogonalLatinSquares(mols)  # noqa
                print(mols_test)
                print(generates)
                test_code = mols_to_code(mols_test)
                print(test_code)
            answer = input("Continue on? [y/n] :: ")

    # NOTE - Examples of not all MOLS create codes
    input()
    print("\n"*100)
    try:
        square1 = LatinSquare([[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]])  # noqa
        square2 = LatinSquare([[0, 1, 2, 3], [3, 2, 1, 0], [1, 0, 3, 2], [2, 3, 0, 1]])  # noqa

        mols_4_test = MutuallyOrthogonalLatinSquares([square1, square2])  # noqa
        print(mols_4_test)
        print(generates)
        test_code = mols_to_code(mols_4_test)
        print(test_code)
    except AssertionError:
        print(error_message)

    input()
    print("\n"*100)
    try:
        square1 = LatinSquare([[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]])  # noqa
        square2 = LatinSquare([[0, 1, 2, 3], [2, 3, 0, 1], [3, 2, 1, 0], [1, 0, 3, 2]])  # noqa

        mols_4_test = MutuallyOrthogonalLatinSquares([square1, square2])  # noqa
        print(mols_4_test)
        print(generates)
        test_code = mols_to_code(mols_4_test)
        print(test_code)
    except AssertionError:
        print(error_message)
