import Main_Run_Program
import os


if __name__ == '__main__':
    # Main_Run_Program.main()
    hello = "riscv64-unknown-elf-gcc a.c"
    hellos = "riscv64-unknown-elf-gcc -S a.c"
    os.system(hellos)
    os.system(hello)
    execu = "riscv64-unknown-elf-run a.out"
    os.system(execu)
    f = open("a.s")
    print(f.read())
