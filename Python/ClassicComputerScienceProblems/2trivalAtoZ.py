class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # start with sentinel
        for nucleotide in gene.upper():
            # print('original : ',bin(self.bit_string))
            self.bit_string <<= 6  # shift left two bits
            # print('<<=2 ',bin(self.bit_string))
            if nucleotide == 'A':
                self.bit_string |= 0b000000
            elif nucleotide == 'B':
                self.bit_string |= 0b000001
            elif nucleotide == 'C':
                self.bit_string |= 0b000010
            elif nucleotide == 'D':
                self.bit_string |= 0b000011

            elif nucleotide == 'E':
                self.bit_string |= 0b000100
            elif nucleotide == 'F':
                self.bit_string |= 0b000101
            elif nucleotide == 'G':
                self.bit_string |= 0b000110
            elif nucleotide == 'H':
                self.bit_string |= 0b000111

            elif nucleotide == 'I':
                self.bit_string |= 0b001000
            elif nucleotide == 'J':
                self.bit_string |= 0b001001
            elif nucleotide == 'K':
                self.bit_string |= 0b001010
            elif nucleotide == 'L':
                self.bit_string |= 0b001011

            elif nucleotide == 'M':
                self.bit_string |= 0b001100
            elif nucleotide == 'N':
                self.bit_string |= 0b001101
            elif nucleotide == 'O':
                self.bit_string |= 0b001110
            elif nucleotide == 'P':
                self.bit_string |= 0b001111

            elif nucleotide == 'Q':
                self.bit_string |= 0b010000
            elif nucleotide == 'R':
                self.bit_string |= 0b010001
            elif nucleotide == 'S':
                self.bit_string |= 0b010010
            elif nucleotide == 'T':
                self.bit_string |= 0b010011

            elif nucleotide == 'U':
                self.bit_string |= 0b010100
            elif nucleotide == 'V':
                self.bit_string |= 0b010101
            elif nucleotide == 'W':
                self.bit_string |= 0b010110
            elif nucleotide == 'X':
                self.bit_string |= 0b010111

            elif nucleotide == 'Y':
                self.bit_string |= 0b0110000
            elif nucleotide == 'Z':
                self.bit_string |= 0b0110001
            elif nucleotide == ' ':
                self.bit_string |= 0b0110010

        ##print('Compress :',bin(self.bit_string))

    def decompress(self) -> str:
        gene: str = ""
        # print(self.bit_string.bit_length()-1)

        for i in range(0, self.bit_string.bit_length() - 1, 6):  # - 1 to exclude         sentinel
            ##print(i)
            bits: int = self.bit_string >> i & 0b111111  # get just 2 relevant bits
            ##print('Binary Decompress : ',bin(bits))

            if bits == 0b000000:  # A
                gene += "A"
            elif bits == 0b000001:  # C
                gene += "B"
            elif bits == 0b000010:  # G
                gene += "C"
            elif bits == 0b000011:  # T
                gene += "D"

            elif bits == 0b000100:  # C
                gene += "E"
            elif bits == 0b000101:  # G
                gene += "F"
            elif bits == 0b000110:  # T
                gene += "G"
            elif bits == 0b000111:  # T
                gene += "H"

            elif bits == 0b001000:  # C
                gene += "I"
            elif bits == 0b001001:  # G
                gene += "J"
            elif bits == 0b001010:  # T
                gene += "K"
            elif bits == 0b001011:  # T
                gene += "L"

            elif bits == 0b001100:  # C
                gene += "M"
            elif bits == 0b001101:  # G
                gene += "N"
            elif bits == 0b001110:  # T
                gene += "O"
            elif bits == 0b001111:  # T
                gene += "P"

            elif bits == 0b010000:  # C
                gene += "Q"
            elif bits == 0b010001:  # G
                gene += "R"
            elif bits == 0b010010:  # T
                gene += "S"
            elif bits == 0b010011:  # T
                gene += "T"

            elif bits == 0b010100:  # C
                gene += "U"
            elif bits == 0b010101:  # G
                gene += "V"
            elif bits == 0b010110:  # T
                gene += "W"
            elif bits == 0b010111:  # T
                gene += "X"

            elif bits == 0b0110000:  # T
                gene += "Y"
            elif bits == 0b0110001:  # T
                gene += "Z"
            elif bits == 0b0110010:  # T
                gene += " "

            # print(gene)
        return gene[::-1]

    def __str__(self) -> str:  # string representation for pretty printing
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof

    original: str = input("Enter Your Data : ").upper()
    print("original is {} bytes".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # compress
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print("Your Data :", compressed)
    print("original and decompressed are the same: {}".format(original == compressed.decompress()))
