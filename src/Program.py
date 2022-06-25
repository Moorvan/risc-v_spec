import Read_ELF_file
from Instr_C import *
from Instr_I import *


class Program:
    def __init__(self, fileName):
        self._m_state = Machine_State()
        self._m_state.pc, self._instrs = Read_ELF_file.read_elf(fileName, self._m_state.mem)
        self._instr_cnt = 0

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

    def run_with_info(self):
        self._instr_cnt = 1
        while True:
            print()
            print("%d  pc  0x%x  instr 0x%x" % (self._instr_cnt, self._m_state.pc, self._instrs[self._m_state.pc]))
            cur_pc = self._m_state.pc
            self._instr_cnt += 1
            self.run_one_step()
            self.print_info()
            if cur_pc == self._m_state.pc:
                print("Reached jump-to-self infinite loop; exiting.")
                break

    def run_without_info(self):
        while True:
            cur_pc = self._m_state.pc
            self.run_one_step()
            if cur_pc == self._m_state.pc:
                print("Reached jump-to-self infinite loop; exiting.")
                break

    @classmethod
    def is_C(cls, instr: int):
        if instr & 0b11 == 0b11:
            return False
        return True


if __name__ == '__main__':
    p = Program("../cases/hello64")
    p.run_with_info()
    # p.run_without_info()


