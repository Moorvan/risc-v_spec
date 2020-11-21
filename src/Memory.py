from collections import OrderedDict
from Error import *


# define the module of Memory

class Memory:
    def __init__(self):
        self._data = OrderedDict()

    def get_mem(self, addr):
        if self._data.get(addr):
            return self._data.get(addr)
        return Error.AccessUndefinedMemory

    def set_mem(self, addr, v):
        self._data[addr] = v

    def clear(self):
        self._data.clear()

    def print_mem(self):
        for (addr, v) in self._data.items():
            print("0x%x: 0x%x" % (addr, v))


if __name__ == '__main__':
    mem = Memory()
    mem.set_mem(12, 12)
    mem.print_mem()
