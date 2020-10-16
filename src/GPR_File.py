from Error import *


# define General Purpose Register File

class GPR_File:

    def __init__(self):
        self._regs = [0] * 32

    def get_reg(self, n):
        if n > 31 or n < 0:
            return Error.IllegalRegisterIndex
        return self._regs[n]

    def set_reg(self, n, v):
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
            print("x" + str(i) + ": " + str(v))


if __name__ == '__main__':
    p_GPR_File = GPR_File()
    p_GPR_File.print_regs()
