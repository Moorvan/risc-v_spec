# This class defines various RISC-V ALU Functions
class ALU:

    @classmethod
    def alu_eq(cls, a, b):
        return a == b

    @classmethod
    def alu_ne(cls, a, b):
        return a != b

    @classmethod
    def alu_lt(cls, a, b):
        return a < b

    @classmethod
    def alu_ge(cls, a, b):
        return a >= b

    @classmethod
    def alu_ltu(cls, a, b):
        mask = 0xffff_ffff_ffff_ffff
        ua = a & mask
        ub = b & mask
        return ua < ub

    @classmethod
    def alu_geu(cls, a, b):
        mask = 0xffff_ffff_ffff_ffff
        ua = a & mask
        ub = b & mask
        return ua >= ub

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
    if ALU.alu_ltu(100, -1):
        print("YES")