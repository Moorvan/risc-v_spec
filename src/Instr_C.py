from riscv_def import *


# This class defines part of the RISC-V 'C' (Compressed) instructions.
class Instr_C:
    def __init__(self, instr):
        self._instr = instr
        self._opcode = self._instr & 0x3
        self._funct3 = self._instr >> 13 & 0x7
        # CA format
        self._funct6_CA = self._instr >> 10 & 0x3f
        self._rd_rs1_CA = 0x8 + (self._instr >> 7 & 0x7)
        self._funct2_CA = self._instr >> 5 & 0x3
        self._rs2_CA = 0x8 + (self._instr >> 2 & 0x7)
        # CR format
        self._funct4_CR = self._instr >> 12 & 0xf
        self._rd_rs1_CR = self._instr >> 7 & 0x1f
        self._rs2_CR = self._instr >> 2 & 0x1f

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

    def execute(self, m_state):
        self._op(m_state)

    def _C_SUB(self, m_state):
        pass

    def _C_XOR(self, m_state):
        pass

    def _C_OR(self, m_state):
        pass

    def _C_AND(self, m_state):
        pass

    def _C_JR(self, m_state):
        pass

    def _C_MV(self, m_state):
        pass

    def _C_EBREAK(self, m_state):
        pass

    def _C_JALR(self, m_state):
        pass

    def _C_ADD(self, m_state):
        pass


if __name__ == '__main__':
    i = Instr_C(0x87aa)