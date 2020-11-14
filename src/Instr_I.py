from ALU import *
from Machine_State import *
from riscv_def import *
from Instr_Common import *


# This class defines part of the RISC-V 'I' (Base) instructions.

class Instr_I:

    # decode the instruction and get the op of the instruction
    def __init__(self, instr, is_C):
        self._instr = instr
        self._is_C = is_C
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
        elif self._opcode == RISCV_OPCODE.LUI:
            self._op = self._LUI
        elif self._opcode == RISCV_OPCODE.JAL:
            self._op = self._JAL
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
        Instr_I.exec_AUIPC(False, self._rd, self._imm20_U, m_state)

    def _LUI(self, m_state):
        rd_val = self._imm20_U << 12
        m_state.gprs.set_reg(self._rd, rd_val)

    def _JAL(self, m_state):
        Instr_I.exec_JAL(False, self._rd, self._imm21_J, m_state)

    def _ADD(self, m_state):
        Instr_I.exec_OP(ALU.alu_add, False, self._rd, self._rs1, self._rs2, m_state)

    def _SUB(self, m_state):
        Instr_I.exec_OP(ALU.alu_sub, False, self._rd, self._rs1, self._rs2, m_state)

    def _ADDI(self, m_state):
        Instr_I.exec_OP_IMM(ALU.alu_add, False, self._rd, self._rs1, self._imm12_I)

    def _SD(self, m_state):
        Instr_I.exec_STORE(False, self._rs1, self._rs2, self._imm12_S, self._funct3, m_state)

    def _BEQ(self, m_state):
        Instr_I.exec_BRANCH(ALU.alu_eq, False, self._rs1, self._rs2, self._imm13_B, m_state)

    @classmethod
    def exec_AUIPC(cls, is_C, rd, imm20, m_state):
        offset = imm20 << 12
        rd_val = ALU.alu_add(offset, m_state.pc)
        Instr_Common.finish_rd_and_pc_incr(rd, rd_val, is_C, m_state)

    @classmethod
    def exec_JAL(cls, is_C, rd, imm21, m_state):
        pc = m_state.pc
        if is_C:
            rd_val = pc + 2
        else:
            rd_val = pc + 4

        new_pc = ALU.alu_add(pc, imm21)
        Instr_Common.finish_rd_and_pc(rd, rd_val, new_pc, m_state)

    @classmethod
    def exec_JALR(cls, is_C, rd, rs1, imm12, m_state):
        pc = m_state.pc
        if is_C:
            rd_val = pc + 2
        else:
            rd_val = pc + 4
        rs1_val = m_state.gprs.get_reg(rs1)
        new_pc = ALU.alu_add(rs1_val, imm12)
        Instr_Common.finish_rd_and_pc(rd, rd_val, new_pc, m_state)


    @classmethod
    def exec_OP(cls, alu_op, is_C, rd, rs1, rs2, m_state):
        rs1_val = m_state.gprs.get_reg(rs1)
        rs2_val = m_state.gprs.get_reg(rs2)
        rd_val = alu_op(rs1_val, rs2_val)
        Instr_Common.finish_rd_and_pc_incr(rd, rd_val, is_C, m_state)

    @classmethod
    def exec_OP_IMM(cls, alu_op, is_C, rd, rs1, imm12, m_state):
        rs1_val = m_state.gprs.get_reg(rs1)
        rd_val = alu_op(rs1_val, imm12)
        Instr_Common.finish_rd_and_pc_incr(rd, rd_val, is_C, m_state)

    @classmethod
    def exec_STORE(cls, is_C, rs1, rs2, imm12, funct3, m_state):
        rs2_val = m_state.gprs.get_reg(rs2)

        rs1_val = m_state.gprs.get_reg(rs1)
        addr = ALU.alu_add(rs1_val, imm12)

        m_state.mem.set_mem(addr, rs2_val)
        Instr_Common.finish_pc_incr(is_C, m_state)

    @classmethod
    def exec_BRANCH(cls, branch_alu_op, is_C, rs1, rs2, imm13, m_state):
        rs1_val = m_state.gprs.get_reg(rs1)
        rs2_val = m_state.gprs.get_reg(rs2)
        taken = branch_alu_op(rs1_val, rs2_val)

        pc = m_state.pc
        target = ALU.alu_add(pc, imm13)
        if taken:
            new_pc = target
        elif is_C:
            new_pc = pc + 2
        else:
            new_pc = pc + 4

        Instr_Common.finish_pc(new_pc, m_state)



if __name__ == '__main__':
    m = Machine_State()
    i = Instr_I(0x4197)
    i.execute(m)
    m.printState()
