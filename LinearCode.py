import math


class LinearCode:
    def __init__(self, codewords: list[str]):
        assert LinearCode.is_code(codewords)

        self.word_size = len(codewords[0])
        self.num_words = len(codewords)
        self.q_field = int(max(max(codewords))) + 1
        self.distance = LinearCode.class_distance(codewords)
        self.detection = self.distance - 1
        self.correction = math.ceil(self.distance / 2) - 1
        self.basis = LinearCode.generator_matrix(codewords)
        self.rank = len(self.basis)
        self.codewords = codewords

    @classmethod
    def is_code(cls, codewords: list[str]) -> bool:
        try:
            # NOTE - not empty check
            assert len(codewords) > 0, "Empty"

            # NOTE - consistent word length check
            word_size = len(codewords[0])
            for word in codewords:
                assert len(word) == word_size, "Word size not consistent"

            # NOTE - Zero vector check
            assert "0"*word_size in codewords, "No zero vector"

            field = int(max(max(codewords))) + 1

            # NOTE - Closed under vector addition check
            for word1 in codewords:
                for word2 in codewords:
                    add_test = LinearCode.vector_add(word1, word2, field)
                    assert add_test in codewords, "{} + {} = {}: Not in code".format(word1, word2, add_test)  # noqa

            # NOTE - Closed under scalar multiplication check
            for word in codewords:
                for scalar in range(field):
                    mult_test = LinearCode.scalar_mult(word, scalar, field)
                    assert mult_test in codewords, "{}*{} = {}: Not in code".format(scalar, word, mult_test)  # noqa

            return True
        except AssertionError as error:
            print(codewords)
            print(error)
            return False

    @classmethod
    def word_distance(cls, word1: str, word2: str) -> int:
        word_length = len(word1)
        assert word_length == len(word2)

        distance = 0
        for i in range(word_length):
            if word1[i] != word2[i]:
                distance += 1

        return distance

    @classmethod
    def class_distance(cls, codewords: list[str]) -> int:
        assert LinearCode.is_code(codewords)

        word_length = len(codewords[0])
        distance = word_length

        for word in codewords:
            if word == "0"*word_length:
                continue

            word_dist = LinearCode.word_distance(word, "0"*word_length)
            distance = min(word_dist, distance)

        return distance

    @classmethod
    def vector_add(cls, code1: str, code2: str, field: int) -> str:

        assert len(code1) == len(code2)
        vector_result = ''
        for i in range(len(code1)):
            vector_result += str((int(code1[i]) + int(code2[i])) % field)

        return vector_result

    @classmethod
    def scalar_mult(cls, code: str, scalar: int, field: int) -> str:
        vector_result = ''
        for i in range(len(code)):
            vector_result += str((int(code[i]) * scalar) % field)

        return vector_result

    @classmethod
    def generator_matrix(cls, codewords: list[str]) -> list[str]:
        assert LinearCode.is_code(codewords)
        len_codeword = len(codewords[0])
        q_field = int(max(max(codewords))) + 1
        gen_matrix = list(codewords)

        gen_matrix.remove("0"*len_codeword)
        # NOTE - Removes scalar mults
        for word in gen_matrix:
            for scalar in range(2, q_field):
                scalar_word = LinearCode.scalar_mult(word, scalar, q_field)
                if scalar_word in gen_matrix:
                    gen_matrix.remove(scalar_word)

        # NOTE - Remove vector adds
        for word1 in gen_matrix:
            for word2 in gen_matrix:
                for i in range(1, q_field):
                    for j in range(1, q_field):
                        s_word1 = LinearCode.scalar_mult(word1, i, q_field)
                        s_word2 = LinearCode.scalar_mult(word2, j, q_field)
                        vector_word = LinearCode.vector_add(s_word1, s_word2, q_field)  # noqa
                        if vector_word in gen_matrix \
                            and vector_word != word1 \
                                and vector_word != word2:
                            gen_matrix.remove(vector_word)

        return gen_matrix

    def info_rate(self) -> str:
        return str(int(math.log(self.num_words, self.q_field))) + "/" + str(self.word_size)  # noqa

    def __str__(self) -> str:
        return_string = ""

        return_string += "A ({0}, {1}, {2}) or [{0}, {3}] Code over a {4}-field\n".format(self.word_size, self.num_words, self.distance, self.rank, self.q_field)  # noqa
        return_string += "Can detect {} error(s)\nCan correct {} error(s)\n".format(self.detection, self.correction)  # noqa
        return_string += "Has an info rate of {}\n".format(self.info_rate())
        return_string += "="*50 + "\n"
        return_string += "Is generated by the matix:\n"
        for word in self.basis:
            return_string += str([int(digit) for digit in word]) + "\n"
        return_string += "="*50 + "\n"
        return_string += "Codewords:\n"
        for i in range(self.num_words):
            return_string += "{}, ".format(self.codewords[i])
            # arbitrary cutoff for formatting
            cutoff = 7
            if i % cutoff == cutoff - 1:
                return_string += "\n"

        return return_string + "\n"


if __name__ == "__main__":
    input()
    print("\n"*100)
    codewords = ["000", "011", "101", "110"]
    code_test = LinearCode(codewords)
    print(code_test)

    input()
    print("\n"*100)
    codewords = ["0000", "0111", "0222", "1012", "1120", "1201", "2021", "2102", "2210"]  # noqa
    code_test = LinearCode(codewords)
    print(code_test)

    input()
    print("\n"*100)
    codewords = ["00000", "10001", "01010", "00111", "11011", "10110", "01101", "11100"]  # noqa
    code_test = LinearCode(codewords)
    print(code_test)
