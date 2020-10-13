from Read_File import *
from Instr_I import *
from Machine_State import *


def main():
    pass


if __name__ == '__main__':
    instr_s0 = "addi x2, x0, 1"
    instr_s1 = "add x1, x2, x3"
    instr_s2 = "sd x1, 8(x0)"
    instr_I0 = Read_File.decode(instr_s0)
    instr_I1 = Read_File.decode(instr_s1)
    instr_I2 = Read_File.decode(instr_s2)
    m_state = Machine_State()
    instr_I0.execute(m_state)
    m_state.printState()
    instr_I1.execute(m_state)
    m_state.printState()
    instr_I2.execute(m_state)
    m_state.printState()
