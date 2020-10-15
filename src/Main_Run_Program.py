from Read_File import *
from Instr_I import *
from Machine_State import *


def main():
    print("This is a risc-v Emulator.")
    m_state = Machine_State()
    while process(m_state):
        print("Do you want to clean the Memory?(Y/N)")
        ch = input().strip()
        if ch == 'Y':
            m_state.mem.clear()
        m_state.gprs.clear()
        m_state.pc = 0


def process(m_state):
    # read the assembly file
    print("Please input the risc-v assembly file:")
    showTrack = False
    fileName = input().strip()
    instrs, pc = Read_File.file_decode(fileName)
    m_state.pc = pc
    if instrs == Error.FileNotFound:
        print("The input file is not exist.")
        return 1

    print("Do you want to show the machine state every step?(Y/N")
    ch = input().strip()
    if ch == 'Y':
        showTrack = True

    while

    print("Continue?(Y/N)")
    ch = input().strip()
    if ch == 'Y':
        return 1
    else:
        return 0


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
