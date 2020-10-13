import re
from Instr_I import *


# This class defines the utils of read Assembly code file.

class Read_File:

    # read the assembly code file and return the instr list
    @classmethod
    def file_decode(cls, src_url):
        f = open(src_url)
        fs = f.read()
        

    # read a string of assembly instruction and return a instr
    @classmethod
    def decode(cls, instr):
        strList = re.split(" |, |,|\(|\)", instr)
        op = strList[0]
        return op_type.get(op)(strList)

    @classmethod
    def decode_add(cls, strList):
        op = strList[0]
        rs1 = int(strList[2][1:])
        rs2 = int(strList[3][1:])
        rd = int(strList[1][1:])
        return Instr_I(op, rd, rs1, rs2)

    @classmethod
    def decode_addi(cls, strList):
        op = strList[0]
        rd = int(strList[1][1:])
        rs1 = int(strList[2][1:])
        imm = int(strList[3])
        return Instr_I(op, rd, rs1, 0, imm)

    @classmethod
    def decode_sd(cls, strList):
        op = strList[0]
        rs1 = int(strList[1][1:])
        rs2 = int(strList[3][1:])
        imm = int(strList[2])
        return Instr_I(op, 0, rs1, rs2, imm)

    @classmethod
    def decode_beq(cls, strList):
        op = strList[0]
        rs1 = int(strList[1][1:])
        rs2 = int(strList[2][1:])
        imm = int(strList[3])
        return Instr_I(op, 0, rs1, rs2, imm)


# Map str of op to the function of how to decode the assembly code

op_type = {
    'add': Read_File.decode_add,
    'addi': Read_File.decode_addi,
    'sd': Read_File.decode_sd,
    'beq': Read_File.decode_beq
}

if __name__ == '__main__':
    instr_s = "sd x5, 16(x7)"
    a = Read_File.decode(instr_s)
    # print(a.op)
