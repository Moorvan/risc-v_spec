class Bit_Utils:
    @classmethod
    def get_signed(cls, w: int, x: int):
        x = x & (pow(2, w) - 1)
        mask = pow(2, w - 1)
        signed = x & mask
        if signed == 0:
            return x
        else:
            return x - pow(2, w)

    @classmethod
    def bit_slice(cls, x: int, l: int, r: int):
        return x >> r & (pow(2, l - r + 1) - 1)


if __name__ == '__main__':
    print(Bit_Utils.get_signed(10, -1))
