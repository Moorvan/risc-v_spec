# This class defines various RISC-V ALU Functions
class ALU:

    @classmethod
    def alu_eq(cls, a, b):
        return a == b

    @classmethod
    def alu_ne(cls, a, b):
        return a != b

    @classmethod
    def alu_add(cls, a, b):
        return a + b

    @classmethod
    def alu_sub(cls, a, b):
        return a - b

    @classmethod
    def alu_xor(cls, a, b):
        return a ^ b

    @classmethod
    def alu_or(cls, a, b):
        return a or b

    @classmethod
    def alu_and(cls, a, b):
        return a and b


if __name__ == '__main__':
    if ALU.alu_ne(1, 3):
        print("1 != 3")
