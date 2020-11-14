import Read_ELF_file
from Machine_State import *
from Instr_C import *
from Instr_I import *


class Program:
    def __init__(self, fileName):
        self._m_state = Machine_State()
        self._m_state.pc, self._instrs = Read_ELF_file.get_Instrs(fileName)

    def run_one_step(self):
        instr = self._instrs[self._m_state.pc]
        if Program.is_C(instr):
            instr_C = Instr_C(instr)
            instr_C.execute(self._m_state)
        else:
            instr_I = Instr_I(instr, False)
            instr_I.execute(self._m_state)

    def print_info(self):
        self._m_state.printState()

    @classmethod
    def is_C(cls, instr):
        if instr & 0b11 == 0b11:
            return False
        return True


if __name__ == '__main__':
    p = Program("a.out")
    p.run_one_step()
    p.print_info()
