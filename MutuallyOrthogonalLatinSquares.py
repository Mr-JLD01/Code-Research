from LatinSquare import LatinSquare


class MutuallyOrthogonalLatinSquares:
    def __init__(self, mols: list[LatinSquare]):
        assert len(mols) > 1
        assert MutuallyOrthogonalLatinSquares.is_mutually_orthogonal_list(mols)
        self.dimension = mols[0].dimension
        self.mols = mols
        self.matrix = MutuallyOrthogonalLatinSquares.mols_matrix(mols)

    # FIXME - Doesn't work for even num_square
    @classmethod
    def find_mutually_orthogonal_latin_squares(cls, field: int, num_squares: int = 1) -> list[LatinSquare]:  # noqa
        mols = []
        assert num_squares <= field - 1

        for square in range(1, num_squares + 1):
            ls = []
            for r in range(field):
                row = []
                for c in range(field):
                    elem = (square*r + c) % field
                    row.append(elem)
                ls.append(row)

            if len(set([row[0] for row in ls])) == field:
                mols.append(ls)

        return mols

    @classmethod
    def is_mutually_orthogonal_list(cls, squares: list[LatinSquare]) -> bool:  # noqa
        try:
            num_squares = len(squares)
            for i in range(num_squares):
                for j in range(i+1, num_squares):
                    assert MutuallyOrthogonalLatinSquares.is_mutually_orthogonal(squares[i], squares[j])  # noqa
        except AssertionError:
            return False
        return True

    @classmethod
    def is_mutually_orthogonal(cls, square1: LatinSquare, square2: LatinSquare) -> bool:  # noqa
        overlay = []
        try:
            assert square1.dimension == square2.dimension
            for row in range(square1.dimension):
                for col in range(square1.dimension):
                    overlay.append((square1.square[row][col], square2.square[row][col]))  # noqa
            assert len(set(overlay)) == square1.dimension**2, "At least 1 point was repeated"  # noqa
        except AssertionError as error:
            print(error)
            print(overlay)
            return False
        return True

    # LINK - https://math.stackexchange.com/questions/1624841/algorithms-for-mutually-orthogonal-latin-squares-a-correct-one  # noqa
    # this function was taken from an answer in this forum
    @classmethod
    def mols_matrix(cls, squares: list[LatinSquare]) -> list[list[tuple[any]]]:  # noqa
        cartesian_product = []
        for row in range(squares[0].dimension):
            cartesian_row = []
            for col in range(squares[0].dimension):
                point = []
                for ls in squares:
                    point.append(ls.square[row][col])
                cartesian_row.append(tuple(point))
            cartesian_product.append(cartesian_row)

        return cartesian_product

    def __str__(self) -> str:
        return_string = ""

        return_string += "A {}-dimension M.O.L.S\n".format(self.dimension)
        return_string += "="*50 + "\n"
        for row in self.matrix:
            return_string += str(row) + "\n"

        return return_string


if __name__ == "__main__":
    for i in range(3, 11):
        try:
            input()
            print("\n"*100)
            mols = [LatinSquare(ls) for ls in MutuallyOrthogonalLatinSquares.find_mutually_orthogonal_latin_squares(i, 2)]  # noqa
            mols_test = MutuallyOrthogonalLatinSquares(mols)  # noqa
            print(mols_test)
        except AssertionError:
            print("M.O.L.S. not found for dimension {}".format(i))
