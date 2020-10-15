import re
from Instr_I import *
from Error import *


# This class defines the utils of read Assembly code file.

class Read_File:

    # read the assembly code file and return the instr list
    @classmethod
    def file_decode(cls, src_url):
        fs = ''
        try:
            f = open('../' + src_url)
            fs = f.read()
            f.close()
        except FileNotFoundError:
            return Error.FileNotFound, Error.FileNotFound
        ls = fs.split("\n")
        lines = []
        labels = {}
        cnt = -1
        instr_Is = []
        pc = 0
        for line in ls:
            if line.find(':') != -1:
                labels[line[0:line.find(':')]] = cnt + 1
                if line[0:line.find(':')] == 'main':
                    pc = cnt + 1
            elif line.find(',') != -1:
                cnt += 1
                lines.append(line)
        for line in lines:
            instr_I = Read_File.decode(line, labels)
            instr_Is.append(instr_I)
        return instr_Is, pc

    # read a string of assembly instruction and return a instr
    @classmethod
    def decode(cls, instr, labelTable):
        strList = re.split(" |, |,|\(|\)", instr)
        op = strList[0]
        # print(op)
        return op_type.get(op)(strList, labelTable)

    @classmethod
    def decode_add(cls, strList, labelTable):
        op = strList[0]
        rs1 = int(strList[2][1:])
        rs2 = int(strList[3][1:])
        rd = int(strList[1][1:])
        return Instr_I(op, rd, rs1, rs2)

    @classmethod
    def decode_addi(cls, strList, labelTable):
        op = strList[0]
        rd = int(strList[1][1:])
        rs1 = int(strList[2][1:])
        imm = int(strList[3])
        return Instr_I(op, rd, rs1, 0, imm)

    @classmethod
    def decode_sd(cls, strList, labelTable):
        op = strList[0]
        rs1 = int(strList[1][1:])
        rs2 = int(strList[3][1:])
        imm = int(strList[2])
        return Instr_I(op, 0, rs1, rs2, imm)

    @classmethod
    def decode_beq(cls, strList, labelTable):
        op = strList[0]
        rs1 = int(strList[1][1:])
        rs2 = int(strList[2][1:])
        if strList[3][0] < '0' or strList[3][0] > '9':
            if labelTable.get(strList[3]):
                imm = labelTable.get(strList[3])
            else:
                return "Error"
        else:
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
    a, b = Read_File.file_decode("./a.s")
    if a == Error.FileNotFound:
        print("File not found")
    else:
        print("Yes")
