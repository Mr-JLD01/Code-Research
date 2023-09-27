
class LatinSquare:
    def __init__(self, square: list[list[any]]):
        assert LatinSquare.is_latin_square(square)
        self.dimension = len(square)
        self.square = square

    @classmethod
    def is_latin_square(cls, square: list[list[any]]) -> bool:
        try:
            num_rows = len(square)
            # NOTE - Square matrix check
            for row in square:
                assert len(row) == num_rows

            # NOTE - Extraneous alphabet check
            assumed_alphabet = square[0]
            for row in range(1, num_rows):
                for elem in square[row]:
                    assert elem in assumed_alphabet

            # NOTE - row and column check
            for row in range(num_rows):
                for col in range(num_rows):
                    elem = square[row][col]
                    assert elem not in square[row][col+1:]
                    for row_left in range(num_rows - row - 1):
                        assert elem != square[row + row_left + 1][col]

        except AssertionError:
            return False

        return True

    def __str__(self) -> str:
        return_string = ""
        return_string += "A {}-dimension Latin Square\n".format(self.dimension)
        return_string += "="*50 + "\n"
        for row in self.square:
            return_string += str(row) + "\n"

        return return_string


if __name__ == "__main__":
    error_message = "Not a Latin Square"
    try:
        ls_test = LatinSquare([[1], [0]])
    except AssertionError:
        print(error_message)

    try:
        ls_test = LatinSquare([[1, 0]])
    except AssertionError:
        print(error_message)

    try:
        ls_test = LatinSquare([[1, 1], [0, 1]])
    except AssertionError:
        print(error_message)

    ls_test = LatinSquare([[1, 0], [0, 1]])
    print(ls_test)

    ls_test = LatinSquare([[0, 1, 2], [1, 2, 0], [2, 0, 1]])
    print(ls_test)
