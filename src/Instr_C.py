from RISCV_Defs import *
from Instr_I import *


# This class defines part of the RISC-V 'C' (Compressed) instructions.
class Instr_C:
    def __init__(self, instr: int):
        self._instr = instr
        self._opcode = Bit_Utils.bit_slice(self._instr, 1, 0)
        self._funct3 = Bit_Utils.bit_slice(self._instr, 15, 13)

        # CR format
        self._funct4_CR = Bit_Utils.bit_slice(self._instr, 15, 12)
        self._rd_rs1_CR = Bit_Utils.bit_slice(self._instr, 11, 7)
        self._rs2_CR = Bit_Utils.bit_slice(self._instr, 6, 2)

        # CA format
        self._funct6_CA = Bit_Utils.bit_slice(self._instr, 15, 10)
        self._rd_rs1_CA = 0x8 | Bit_Utils.bit_slice(self._instr, 9, 7)
        self._funct2_CA = Bit_Utils.bit_slice(self._instr, 6, 5)
        self._rs2_CA = 0x8 | Bit_Utils.bit_slice(self._instr, 4, 2)

        self._op = self._C_ADD
        if self._opcode == RISCV_OPCODE.C1:
            if self._funct6_CA == RISCV_OTHER.FUNCT6_C_SUB and self._funct2_CA == RISCV_OTHER.FUNCT2_C_SUB:
                self._op = self._C_SUB
            elif self._funct6_CA == RISCV_OTHER.FUNCT6_C_XOR and self._funct2_CA == RISCV_OTHER.FUNCT2_C_XOR:
                self._op = self._C_XOR
            elif self._funct6_CA == RISCV_OTHER.FUNCT6_C_OR and self._funct2_CA == RISCV_OTHER.FUNCT2_C_OR:
                self._op = self._C_OR
            elif self._funct6_CA == RISCV_OTHER.FUNCT6_C_AND and self._funct2_CA == RISCV_OTHER.FUNCT2_C_AND:
                self._op = self._C_AND
        elif self._opcode == RISCV_OPCODE.C2:
            if self._funct4_CR == RISCV_OTHER.FUNCT4_C_JR and self._rd_rs1_CR != 0 and self._rs2_CR == 0:
                self._op = self._C_JR
            elif self._funct4_CR == RISCV_OTHER.FUNCT4_C_MV and self._rd_rs1_CR != 0 and self._rs2_CR != 0:
                self._op = self._C_MV
            elif self._funct4_CR == RISCV_OTHER.FUNCT4_C_EBREAK and self._rd_rs1_CR == 0 and self._rs2_CR == 0:
                self._op = self._C_EBREAK
            elif self._funct4_CR == RISCV_OTHER.FUNCT4_C_JALR and self._rd_rs1_CR != 0 and self._rs2_CR == 0:
                self._op = self._C_JALR
            elif self._funct4_CR == RISCV_OTHER.FUNCT4_C_ADD and self._rd_rs1_CR != 0 and self._rs2_CR != 0:
                self._op = self._C_ADD
        print(self._op)

    def execute(self, m_state: Machine_State):
        self._op(m_state)

    def _C_SUB(self, m_state):
        Instr_I.exec_OP(ALU.alu_sub, True, self._rd_rs1_CA, self._rd_rs1_CA, self._rs2_CA, m_state)

    def _C_XOR(self, m_state):
        Instr_I.exec_OP(ALU.alu_xor, True, self._rd_rs1_CA, self._rd_rs1_CA, self._rs2_CA, m_state)

    def _C_OR(self, m_state):
        Instr_I.exec_OP(ALU.alu_or, True, self._rd_rs1_CA, self._rd_rs1_CA, self._rs2_CA, m_state)

    def _C_AND(self, m_state):
        Instr_I.exec_OP(ALU.alu_and, True, self._rd_rs1_CA, self._rd_rs1_CA, self._rs2_CA, m_state)

    def _C_JR(self, m_state):
        rd = 0
        imm12 = 0
        Instr_I.exec_JALR(True, rd, self._rd_rs1_CR, imm12, m_state)

    def _C_MV(self, m_state):
        rs1 = 0
        Instr_I.exec_OP(ALU.alu_add, True, self._rd_rs1_CR, rs1, self._rs2_CR, m_state)

    def _C_EBREAK(self, m_state):
        pass

    def _C_JALR(self, m_state):
        rd = 1
        imm12 = 0
        Instr_I.exec_JALR(True, rd, self._rd_rs1_CR, imm12, m_state)

    def _C_ADD(self, m_state):
        Instr_I.exec_OP(ALU.alu_add, True, self._rd_rs1_CR, self._rd_rs1_CR, m_state)


if __name__ == '__main__':
    i = Instr_C(0x87aa)
