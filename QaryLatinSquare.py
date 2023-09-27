from LatinSquare import LatinSquare


class QaryLatinSquare(LatinSquare):

    def __init__(self, q: int):
        self.q = q
        super().__init__(QaryLatinSquare.qLatinSquare(q))

    @classmethod
    def qLatinSquare(cls, q: int) -> list[list[int]]:
        base_row = []

        for i in range(q):
            base_row.append(i)

        square: list[list[int]] = []
        for _ in range(q):
            square.append(base_row)
            base_row = base_row[1:] + base_row[0:1]

        return square

    def __str__(self) -> str:
        return_string = ""
        return_string += "A {0}-ary {1}x{1} Latin Square\n".format(self.q, self.dimension)  # noqa
        return_string += "="*50 + "\n"
        for row in self.square:
            return_string += str(row) + "\n"

        return return_string


if __name__ == "__main__":
    for i in range(2, 8):
        input()
        print("\n"*100)
        test_ls = QaryLatinSquare(i)
        print(test_ls)
