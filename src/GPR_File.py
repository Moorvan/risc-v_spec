from Error import *


# define General Purpose Register File

class GPR_File:

    def __init__(self):
        self._regs = [0] * 32

    def get_reg(self, n: int):
        if n > 31 or n < 0:
            return Error.IllegalRegisterIndex
        return self._regs[n]

    def set_reg(self, n: int, v: int):
        if n == 0:
            return
        if n > 31 or n < 0:
            return Error.IllegalRegisterIndex
        self._regs[n] = v

    def clear(self):
        for index in range(0, len(self._regs)):
            self._regs[index] = 0

    def print_regs(self):
        for i, v in enumerate(self._regs):
            if i % 4 == 0:
                print("x%d-x%d:" % (i, i + 3), end='  ')
            print("0x%x" % v, end='  ')
            if (i + 1) % 4 == 0:
                print()


if __name__ == '__main__':
    pass
