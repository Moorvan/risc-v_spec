from collections import OrderedDict
from Error import *
from RISCV_Defs import *
from Bit_Utils import *


# define the module of Memory

class Memory:
    def __init__(self):
        self._data = OrderedDict()

    def get_mem(self, addr: int, funct3: int):
        print("addr = %x" % addr)
        res = Bit_Utils.bit_slice(self._data.get(addr), 7, 0)  # LB or LBU, H, W, D
        w = 8
        if funct3 % 4 >= 1:  # LH or LHU, W, D
            res += Bit_Utils.bit_slice(self._data.get(addr + 1), 7, 0) << 8
            w += 8
        if funct3 % 4 >= 2:  # LW or LWU, D
            res += Bit_Utils.bit_slice(self._data.get(addr + 2), 7, 0) << (8 * 2)
            res += Bit_Utils.bit_slice(self._data.get(addr + 3), 7, 0) << (8 * 3)
            w += 16
        if funct3 % 4 >= 3:  # LD or LDU
            res += Bit_Utils.bit_slice(self._data.get(addr + 4), 7, 0) << (8 * 4)
            res += Bit_Utils.bit_slice(self._data.get(addr + 5), 7, 0) << (8 * 5)
            res += Bit_Utils.bit_slice(self._data.get(addr + 6), 7, 0) << (8 * 6)
            res += Bit_Utils.bit_slice(self._data.get(addr + 7), 7, 0) << (8 * 7)
            w += 32

        if funct3 < 4:
            print("w = %d" % w)
            res = Bit_Utils.get_signed(w, res)
        return res

    def set_mem(self, addr: int, v: int, funct3: int):
        self._data[addr] = Bit_Utils.bit_slice(v, 7, 0)  # SB
        v = v >> 8
        if funct3 >= 1:  # SH, SW, SD
            self._data[addr + 1] = Bit_Utils.bit_slice(v, 7, 0)
            v = v >> 8
        if funct3 >= 2:  # SW, SD
            self._data[addr + 2] = Bit_Utils.bit_slice(v, 7, 0)
            v = v >> 8
            self._data[addr + 3] = Bit_Utils.bit_slice(v, 7, 0)
            v = v >> 8
        if funct3 >= 3:  # SD
            self._data[addr + 4] = Bit_Utils.bit_slice(v, 7, 0)
            v = v >> 8
            self._data[addr + 5] = Bit_Utils.bit_slice(v, 7, 0)
            v = v >> 8
            self._data[addr + 6] = Bit_Utils.bit_slice(v, 7, 0)
            v = v >> 8
            self._data[addr + 7] = Bit_Utils.bit_slice(v, 7, 0)

    def clear(self):
        self._data.clear()

    def print_mem(self):
        for (addr, v) in self._data.items():
            print("0x%x: 0x%x" % (addr, v))


if __name__ == '__main__':
    print(4 % 3)
