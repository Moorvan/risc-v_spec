from functools import reduce

from Program import *
from Instr_I import *
from Machine_State import *
import os


def main():
    print("This is a risc-v Emulator.")
    while process():
        continue
    print("Bye!")


def handleCSource():
    print("Please input the c source code file path: ")
    path = input().strip()
    exe_file = reduce(lambda x, y: x+"."+y, path.split(".")[:-1]) + ".out"
    print("Converting to risc-v executable file...")
    c2out(path, exe_file)
    print("Completed. Output executable file: " + exe_file)
    print("Do you want to simulate running the risc-v executable file? (Y/N)")
    ch = input().strip()
    if ch == "Y":
        p = Program(exe_file)
        print("Do you want to show the machine state every step? (Y/N)")
        ch1 = input().strip()
        if ch1 == "Y":
            p.run_with_info()
        else:
            p.run_without_info()
        print("Completed.")


def handleEXESource():
    print("Please input the risc-v executable file path: ")
    path = input().strip()
    print("Do you want to show the machine state every step? (Y/N)")
    p = Program(path)
    ch = input().strip()
    if ch == "Y":
        p.run_with_info()
    else:
        p.run_without_info()
    print("Completed.")


def process():
    # read the assembly file
    print("Please choose the input type: (input 1 or 2 or input q to exit)")
    print(" (1) c source code.")
    print(" (2) risc-v executable file.")

    ch = input().strip()
    if ch == "1":
        handleCSource()
    elif ch == "2":
        handleEXESource()
    else:
        print("Please input 1 or 2.")

    print("Continue? (Y/N)")
    ch1 = input().strip()
    if ch1 == "Y":
        return True
    else:
        return False


def c2out(fileName, outFileName):
    rungcc = "riscv64-unknown-elf-gcc " + fileName + " -o " + outFileName
    os.system(rungcc)
    return "../" + fileName[0:fileName.find('.')] + ".out"


def c2ass(fileName):
    modName = reduce(lambda x, y: x + '.' + y, fileName.split('.')[:-1])
    rungcc = "riscv64-unknown-elf-gcc -S " + fileName + " -o " + modName + ".s"
    os.system(rungcc)
    return "../" + fileName[0:fileName.find('.')] + ".s"


def runOut(fileName):
    rungccrun = "riscv64-unknown-elf-run " + fileName
    ret = os.system(rungccrun)
    return ret
