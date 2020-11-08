from ALU import *
from Machine_State import *
from riscv_def import *


# This class defines part of the RISC-V 'I' (Base) instructions.

class Instr_I:
    def __init__(self, instr):
        self._instr = instr
        self._opcode = self._instr & 0x7f
        self._rd = self._instr >> 7 & 0x1f
        self._funct3 = self._instr >> 12 & 0x7
        self._rs1 = self._instr >> 15 & 0x1f
        self._rs2 = self._instr >> 20 & 0x1f
        self._funct7 = self._instr >> 25 & 0x7f

        self._imm12_I = self._instr >> 20 & 0xfff

        self._imm12_S = (self._instr >> 25 & 0x7f) << 5 + (self._instr >> 7 & 0x1f)
        self._imm13_B = (self._instr >> 31 & 0x1) << 12 + (self._instr >> 25 & 0x3f) << 5 + (
                self._instr >> 8 & 0xf) << 1 + (self._instr >> 7 & 0x1) << 11
        self._imm21_J = (self._instr >> 31 & 0x1) << 20 + (self._instr >> 21 & 0x3ff) << 1 + (
                self._instr >> 20 & 0x1) << 11 + (self._instr >> 12 & 0xff) << 12
        self._imm20_U = self._instr >> 12 & 0xfffff

        self._op = self._ADD
        if self._opcode == RISCV_OPCODE.AUIPC:
            self._op = self._AUIPC
        elif self._opcode == RISCV_OPCODE.OP:
            if self._funct3 == RISCV_FUNCT3.ADD and self._funct7 == RISCV_FUNCT7.ADD:
                self._op = self._ADD
            elif self._funct3 == RISCV_FUNCT3.SUB and self._funct7 == RISCV_FUNCT7.SUB:
                self._op = self._SUB
        elif self._opcode == RISCV_OPCODE.OP_IMM:
            if self._funct3 == RISCV_FUNCT3.ADDI:
                self._op = self._ADDI

        print(self._op)

    # this function can change the input machine state after executing the instruction
    def execute(self, m_state):
        self._op(m_state)

    def _AUIPC(self, m_state):
        offset = self._imm20_U << 12
        rd_val = ALU.alu_add(offset, m_state.pc)
        m_state.gprs.set_reg(self._rd, rd_val)

    def _ADD(self, m_state):
        a = m_state.gprs.get_reg(self._rs1)
        b = m_state.gprs.get_reg(self._rs2)
        m_state.gprs.set_reg(self._rd, ALU.alu_add(a, b))
        m_state.pc += 4

    def _SUB(self, m_state):
        a = m_state.gprs.get_reg(self._rs1)
        b = m_state.gprs.get_reg(self._rs2)
        m_state.gprs.set_reg(self._rd, ALU.alu_sub(a, b))
        m_state.pc += 4

    def _ADDI(self, m_state):
        a = m_state.gprs.get_reg(self._rs1)
        b = self._imm12_I
        m_state.gprs.set_reg(self._rd, ALU.alu_add(a, b))
        m_state.pc += 4

    def _SD(self, m_state):
        addr = m_state.gprs.get_reg(self.rs2) + self.imm
        a = m_state.gprs.get_reg(self.rs1)
        m_state.mem.set_mem(addr, a)

    def _BEQ(self, m_state):
        a = m_state.gprs.get_reg(self.rs1)
        b = m_state.gprs.get_reg(self.rs2)
        if ALU.alu_eq(a, b):
            m_state.pc = self.imm


if __name__ == '__main__':
    m = Machine_State()
    i = Instr_I(0x4197)
    i.execute(m)
    m.printState()
