from Program import *
from Instr_I import *
from Machine_State import *
import os


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

    print("Bye!")


def process(m_state):
    # read the assembly file
    print("Please input the risc-v executable file: (input q to exit)")
    showTrack = False
    fileName = input().strip()
    if fileName == 'q':
        return False
    instrs, pc = Read_File.file_decode(fileName)
    m_state.pc = pc
    if instrs == Error.FileNotFound:
        print("The input file is not exist.")
        return True
    if instrs == Error.LabelUsedButNoDefine:
        print("There is a Label used but not define at \n   \"" + pc + "\"")
        return True

    print("Do you want to show the machine state every step?(Y/N)")
    ch = input().strip()
    if ch == 'Y':
        showTrack = True

    while m_state.pc < len(instrs):
        cur_pc = m_state.pc
        cur_instr = instrs[cur_pc]
        cur_instr.execute(m_state)

        if showTrack:
            print("pc:" + str(cur_pc) + " ", end='')
            cur_instr.print_instr()
            m_state.printState()
            print()

    if not showTrack:
        m_state.printState()

    print("Continue?(Y/N)")
    ch = input().strip()
    if ch == 'Y':
        return True
    else:
        return False


def c2out(fileName):
    rungcc = "riscv64-unknown-elf-gcc ../" + fileName + " -o ../" + fileName[0:fileName.find('.')] + ".out"
    os.system(rungcc)
    return "../" + fileName[0:fileName.find('.')] + ".out"


def c2ass(fileName):
    rungcc = "riscv64-unknown-elf-gcc -S ../" + fileName + " -o ../" + fileName[0:fileName.find('.')] + ".s"
    os.system(rungcc)
    return "../" + fileName[0:fileName.find('.')] + ".s"


def runOut(fileName):
    rungccrun = "riscv64-unknown-elf-run ../" + fileName
    ret = os.system(rungccrun)
    return ret


if __name__ == '__main__':
    c2ass("hello.c")
    c2out("hello.c")
    runOut("hello.out")
    # instr_s0 = "addi x2, x0, 1"
    # instr_s1 = "add x1, x2, x3"
    # instr_s2 = "sd x1, 8(x0)"
    # instr_I0 = Read_File.decode(instr_s0)
    # instr_I1 = Read_File.decode(instr_s1)
    # instr_I2 = Read_File.decode(instr_s2)
    # m_state = Machine_State()
    # instr_I0.execute(m_state)
    # m_state.printState()
    # instr_I1.execute(m_state)
    # m_state.printState()
    # instr_I2.execute(m_state)
    # m_state.printState()
