from Bit_Utils import *


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
    def alu_addw(cls, a, b):
        sa = Bit_Utils.get_signed(32, a)
        sb = Bit_Utils.get_signed(32, b)
        return Bit_Utils.get_signed(32, sa + sb)

    @classmethod
    def alu_sub(cls, a, b):
        return a - b

    @classmethod
    def alu_subw(cls, a, b):
        sa = Bit_Utils.get_signed(32, a)
        sb = Bit_Utils.get_signed(32, b)
        return Bit_Utils.get_signed(32, sa - sb)

    @classmethod
    def alu_slt(cls, a, b):
        if a < b:
            return 1
        else:
            return 0

    @classmethod
    def alu_sltu(cls, a, b):
        mask = 0xffff_ffff_ffff_ffff
        ua = a & mask
        ub = b & mask
        if ua < ub:
            return 1
        else:
            return 0

    @classmethod
    def alu_xor(cls, a, b):
        return a ^ b

    @classmethod
    def alu_or(cls, a, b):
        return a | b

    @classmethod
    def alu_and(cls, a, b):
        return a & b

    @classmethod
    def alu_sll(cls, a, b):
        mask = 0xffff_ffff_ffff_ffff
        ua = a & mask
        shamt = b & 0x3f
        res = ua << shamt & mask
        return res

    @classmethod
    def alu_sllw(cls, a, b):
        mask = 0xffff_ffff
        ua = a & mask
        shamt = b & 0x1f
        res = ua << shamt & mask
        return Bit_Utils.get_signed(32, res)

    @classmethod
    def alu_srl(cls, a, b):
        mask = 0xffff_ffff_ffff_ffff
        ua = a & mask
        shamt = b & 0x3f
        res = ua >> shamt & mask
        return res

    @classmethod
    def alu_srlw(cls, a, b):
        mask = 0xffff_ffff
        ua = a & mask
        shamt = b & 0x1f
        res = ua >> shamt & mask
        return Bit_Utils.get_signed(32, res)

    @classmethod
    def alu_sra(cls, a, b):
        shamt = b & 0x3f
        res = a >> shamt
        return res

    @classmethod
    def alu_sraw(cls, a, b):
        sa = Bit_Utils.get_signed(32, a)
        shamt = b & 0x1f
        res = sa >> shamt
        return res


if __name__ == '__main__':
    print("%d" % ALU.alu_addw(-1, -1))
