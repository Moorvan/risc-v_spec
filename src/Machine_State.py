from GPR_File import *
from Memory import *


class Machine_State:
    def __init__(self):
        self.pc = 0
        self.gprs = GPR_File()  # General Purpose Register File
        self.mem = Memory()

    def printState(self):
        print("==============Machine State================")
        print("PC Reg:" + " " + "0x%x" % self.pc + "\n")
        print("GPR File:")
        self.gprs.print_regs()
        print()
        # print("Memory:")
        # self.mem.print_mem()
        print("====================END====================")


if __name__ == '__main__':
    pass
