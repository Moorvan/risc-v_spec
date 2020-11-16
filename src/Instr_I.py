from ALU import *
from Machine_State import *
from RISCV_Defs import *
from Instr_Common import *
from Bit_Utils import *


# This class defines part of the RISC-V 'I' (Base) instructions.

class Instr_I:

    # decode the instruction and get the op of the instruction
    def __init__(self, instr: int, is_C: bool):
        self._instr = instr
        self._is_C = is_C
        self._opcode = Bit_Utils.bit_slice(self._instr, 6, 0)
        self._rd = Bit_Utils.bit_slice(self._instr, 11, 7)
        self._funct3 = Bit_Utils.bit_slice(self._instr, 14, 12)
        self._rs1 = Bit_Utils.bit_slice(self._instr, 19, 15)
        self._rs2 = Bit_Utils.bit_slice(self._instr, 24, 20)
        self._funct7 = Bit_Utils.bit_slice(self._instr, 31, 25)

        self._imm12_I = Bit_Utils.bit_slice(self._instr, 31, 25)

        self._imm12_S = (Bit_Utils.bit_slice(self._instr, 31, 25) << 5) | \
                        (Bit_Utils.bit_slice(self._instr, 11, 7))
        self._imm13_B = (Bit_Utils.bit_slice(self._instr, 31, 31) << 12) | \
                        (Bit_Utils.bit_slice(self._instr, 30, 25) << 5) | \
                        (Bit_Utils.bit_slice(self._instr, 11, 8) << 1) | \
                        (Bit_Utils.bit_slice(self._instr, 7, 7) << 11)
        self._imm21_J = (Bit_Utils.bit_slice(self._instr, 31, 31) << 20) | \
                        (Bit_Utils.bit_slice(self._instr, 30, 21) << 1) | \
                        (Bit_Utils.bit_slice(self._instr, 20, 20) << 11) | \
                        (Bit_Utils.bit_slice(self._instr, 19, 12) << 12)
        self._imm20_U = Bit_Utils.bit_slice(self._instr, 31, 12)

        # for SLLI/SRLI/SRAI
        self._msbs6 = Bit_Utils.bit_slice(self._instr, 31, 26)
        if self._msbs6 == RISCV_OTHER.msbs6_SLLI or \
           self._msbs6 == RISCV_OTHER.msbs6_SRLI or \
           self._msbs6 == RISCV_OTHER.msbs6_SRAI:
            self._shamt_ok = True
        else:
            self._shamt_ok = False
        self._shamt = Bit_Utils.bit_slice(self._instr, 25, 20)
        self._shamt5 = Bit_Utils.bit_slice(self._instr, 24, 20)

        self._op = self._ADD
        if self._opcode == RISCV_OPCODE.AUIPC:
            self._op = self._AUIPC
        elif self._opcode == RISCV_OPCODE.LUI:
            self._op = self._LUI
        elif self._opcode == RISCV_OPCODE.JAL:
            self._op = self._JAL
        elif self._opcode == RISCV_OPCODE.JALR and self._funct3 == RISCV_FUNCT3.JALR:
            self._op = self._JALR
        elif self._opcode == RISCV_OPCODE.BRANCH:
            if self._funct3 == RISCV_FUNCT3.BEQ:
                self._op = self._BEQ
            elif self._funct3 == RISCV_FUNCT3.BNE:
                self._op = self._BNE
            elif self._funct3 == RISCV_FUNCT3.BLT:
                self._op = self._BLT
            elif self._funct3 == RISCV_FUNCT3.BGE:
                self._op = self._BGE
            elif self._funct3 == RISCV_FUNCT3.BLTU:
                self._op = self._BLTU
            elif self._funct3 == RISCV_FUNCT3.BGEU:
                self._op = self._BGEU
        elif self._opcode == RISCV_OPCODE.LOAD:
            if self._funct3 == RISCV_FUNCT3.LB:
                self._op = self._LB
            elif self._funct3 == RISCV_FUNCT3.LH:
                self._op = self._LH
            elif self._funct3 == RISCV_FUNCT3.LW:
                self._op = self._LW
            elif self._funct3 == RISCV_FUNCT3.LD:
                self._op = self._LD
            elif self._funct3 == RISCV_FUNCT3.LBU:
                self._op = self._LBU
            elif self._funct3 == RISCV_FUNCT3.LHU:
                self._op = self._LHU
            elif self._funct3 == RISCV_FUNCT3.LWU:
                self._op = self._LWU
        elif self._opcode == RISCV_OPCODE.STORE:
            if self._funct3 == RISCV_FUNCT3.SB:
                self._op = self._SB
            elif self._funct3 == RISCV_FUNCT3.SH:
                self._op = self._SH
            elif self._funct3 == RISCV_FUNCT3.SW:
                self._op = self._SH
            elif self._funct3 == RISCV_FUNCT3.SD:
                self._op = self._SD
        elif self._opcode == RISCV_OPCODE.OP_IMM:
            if self._funct3 == RISCV_FUNCT3.ADDI:
                self._op = self._ADDI
            elif self._funct3 == RISCV_FUNCT3.SLTI:
                self._op = self._SLTI
            elif self._funct3 == RISCV_FUNCT3.SLTIU:
                self._op = self._SLTIU
            elif self._funct3 == RISCV_FUNCT3.XORI:
                self._op = self._XORI
            elif self._funct3 == RISCV_FUNCT3.ORI:
                self._op = self._ORI
            elif self._funct3 == RISCV_FUNCT3.ANDI:
                self._op = self._ANDI
            elif self._funct3 == RISCV_FUNCT3.SLLI and self._msbs6 == RISCV_OTHER.msbs6_SLLI and self._shamt_ok:
                self._op = self._SLLI
            elif self._funct3 == RISCV_FUNCT3.SRLI and self._msbs6 == RISCV_OTHER.msbs6_SRLI and self._shamt_ok:
                self._op = self._SRLI
            elif self._funct3 == RISCV_FUNCT3.SRAI and self._msbs6 == RISCV_OTHER.msbs6_SRAI and self._shamt_ok:
                self._op = self._SRAI
        elif self._opcode == RISCV_OPCODE.OP_IMM_32:
            if self._funct3 == RISCV_FUNCT3.ADDIW:
                self._op = self._ADDIW
            elif self._funct3 == RISCV_FUNCT3.SLLIW and self._funct7 == RISCV_FUNCT7.SLLIW:
                self._op = self._SLLIW
            elif self._funct3 == RISCV_FUNCT3.SRLIW and self._funct7 == RISCV_FUNCT7.SRLIW:
                self._op = self._SRLIW
            elif self._funct3 == RISCV_FUNCT3.SRAIW and self._funct7 == RISCV_FUNCT7.SRAIW:
                self._op = self._SRAIW
        elif self._opcode == RISCV_OPCODE.OP:
            if self._funct3 == RISCV_FUNCT3.ADD and self._funct7 == RISCV_FUNCT7.ADD:
                self._op = self._ADD
            elif self._funct3 == RISCV_FUNCT3.SUB and self._funct7 == RISCV_FUNCT7.SUB:
                self._op = self._SUB
            elif self._funct3 == RISCV_FUNCT3.SLL and self._funct7 == RISCV_FUNCT7.SLL:
                self._op = self._SLL
            elif self._funct3 == RISCV_FUNCT3.SLT and self._funct7 == RISCV_FUNCT7.SLT:
                self._op = self._SLT
            elif self._funct3 == RISCV_FUNCT3.SLTU and self._funct7 == RISCV_FUNCT7.SLTU:
                self._op = self._SLTU
            elif self._funct3 == RISCV_FUNCT3.XOR and self._funct7 == RISCV_FUNCT7.XOR:
                self._op = self._XOR
            elif self._funct3 == RISCV_FUNCT3.SRL and self._funct7 == RISCV_FUNCT7.SRL:
                self._op = self._SRL
            elif self._funct3 == RISCV_FUNCT3.SRA and self._funct7 == RISCV_FUNCT7.SRA:
                self._op = self._SRA
            elif self._funct3 == RISCV_FUNCT3.OR and self._funct7 == RISCV_FUNCT7.OR:
                self._op = self._OR
            elif self._funct3 == RISCV_FUNCT3.AND and self._funct7 == RISCV_FUNCT7.AND:
                self._op = self._AND
        elif self._opcode == RISCV_OPCODE.OP_32:
            if self._funct3 == RISCV_FUNCT3.ADDW and self._funct7 == RISCV_FUNCT7.ADDW:
                self._op = self._ADDW
            elif self._funct3 == RISCV_FUNCT3.SUBW and self._funct7 == RISCV_FUNCT7.SUBW:
                self._op = self._SUBW
            elif self._funct3 == RISCV_FUNCT3.SLLW and self._funct7 == RISCV_FUNCT7.SLLW:
                self._op = self._SLLW
            elif self._funct3 == RISCV_FUNCT3.SRLW and self._funct7 == RISCV_FUNCT7.SRLW:
                self._op = self._SRLW
            elif self._funct3 == RISCV_FUNCT3.SRAW and self._funct7 == RISCV_FUNCT7.SRAW:
                self._op = self._SRAW
        print(self._op)

    # this function can change the input machine state after executing the instruction
    def execute(self, m_state: Machine_State):
        self._op(m_state)

    def _AUIPC(self, m_state):
        Instr_I.exec_AUIPC(False, self._rd, self._imm20_U, m_state)

    def _LUI(self, m_state):
        rd_val = self._imm20_U << 12
        m_state.gprs.set_reg(self._rd, rd_val)

    def _JAL(self, m_state):
        Instr_I.exec_JAL(False, self._rd, self._imm21_J, m_state)

    def _JALR(self, m_state):
        Instr_I.exec_JALR(False, self._rd, self._rs1, self._imm12_I, m_state)

    def _BEQ(self, m_state):
        Instr_I.exec_BRANCH(ALU.alu_eq, False, self._rs1, self._rs2, self._imm13_B, m_state)

    def _BNE(self, m_state):
        Instr_I.exec_BRANCH(ALU.alu_ne, False, self._rs1, self._rs2, self._imm13_B, m_state)

    def _BLT(self, m_state):
        Instr_I.exec_BRANCH(ALU.alu_lt, False, self._rs1, self._rs2, self._imm13_B, m_state)

    def _BGE(self, m_state):
        Instr_I.exec_BRANCH(ALU.alu_ge, False, self._rs1, self._rs2, self._imm13_B, m_state)

    def _BLTU(self, m_state):
        Instr_I.exec_BRANCH(ALU.alu_ltu, False, self._rs1, self._rs2, self._imm13_B, m_state)

    def _BGEU(self, m_state):
        Instr_I.exec_BRANCH(ALU.alu_geu, False, self._rs1, self._rs2, self._imm13_B, m_state)

    def _LB(self, m_state):
        Instr_I.exec_LOAD(False, self._rd, self._rs1, self._imm12_I, self._funct3, m_state)

    def _LH(self, m_state):
        Instr_I.exec_LOAD(False, self._rd, self._rs1, self._imm12_I, self._funct3, m_state)

    def _LW(self, m_state):
        Instr_I.exec_LOAD(False, self._rd, self._rs1, self._imm12_I, self._funct3, m_state)

    def _LD(self, m_state):
        Instr_I.exec_LOAD(False, self._rd, self._rs1, self._imm12_I, self._funct3, m_state)

    def _LBU(self, m_state):
        Instr_I.exec_LOAD(False, self._rd, self._rs1, self._imm12_I, self._funct3, m_state)

    def _LHU(self, m_state):
        Instr_I.exec_LOAD(False, self._rd, self._rs1, self._imm12_I, self._funct3, m_state)

    def _LWU(self, m_state):
        Instr_I.exec_LOAD(False, self._rd, self._rs1, self._imm12_I, self._funct3, m_state)

    def _SB(self, m_state):
        Instr_I.exec_STORE(False, self._rs1, self._rs2, self._imm12_S, self._funct3, m_state)

    def _SH(self, m_state):
        Instr_I.exec_STORE(False, self._rs1, self._rs2, self._imm12_S, self._funct3, m_state)

    def _SW(self, m_state):
        Instr_I.exec_STORE(False, self._rs1, self._rs2, self._imm12_S, self._funct3, m_state)

    def _SD(self, m_state):
        Instr_I.exec_STORE(False, self._rs1, self._rs2, self._imm12_S, self._funct3, m_state)

    def _ADDI(self, m_state):
        Instr_I.exec_OP_IMM(ALU.alu_add, False, self._rd, self._rs1, self._imm12_I, m_state)

    def _SLTI(self, m_state):
        Instr_I.exec_OP_IMM(ALU.alu_slt, False, self._rd, self._rs1, self._imm12_I, m_state)

    def _SLTIU(self, m_state):
        Instr_I.exec_OP_IMM(ALU.alu_sltu, False, self._rd, self._rs1, self._imm12_I, m_state)

    def _XORI(self, m_state):
        Instr_I.exec_OP_IMM(ALU.alu_xor, False, self._rd, self._rs1, self._imm12_I, m_state)

    def _ORI(self, m_state):
        Instr_I.exec_OP_IMM(ALU.alu_or, False, self._rd, self._rs1, self._imm12_I, m_state)

    def _ANDI(self, m_state):
        Instr_I.exec_OP_IMM(ALU.alu_and, False, self._rd, self._rs1, self._imm12_I, m_state)

    def _SLLI(self, m_state):
        Instr_I.exec_OP_IMM(ALU.alu_sll, False, self._rd, self._rs1, self._shamt, m_state)

    def _SRLI(self, m_state):
        Instr_I.exec_OP_IMM(ALU.alu_srl, False, self._rd, self._rs1, self._shamt, m_state)

    def _SRAI(self, m_state):
        Instr_I.exec_OP_IMM(ALU.alu_sra, False, self._rd, self._rs1, self._shamt, m_state)

    def _ADDIW(self, m_state):
        Instr_I.exec_OP_IMM_32(ALU.alu_addw, False, self._rd, self._rs1, Bit_Utils.get_signed(12, self._imm12_I),
                               m_state)

    def _SLLIW(self, m_state):
        Instr_I.exec_OP_IMM_32(ALU.alu_sllw, False, self._rd, self._rs1, self._shamt5, m_state)

    def _SRLIW(self, m_state):
        Instr_I.exec_OP_IMM_32(ALU.alu_srlw, False, self._rd, self._rs1, self._shamt5, m_state)

    def _SRAIW(self, m_state):
        Instr_I.exec_OP_IMM_32(ALU.alu_sraw, False, self._rd, self._rs1, self._shamt5, m_state)

    def _ADD(self, m_state):
        Instr_I.exec_OP(ALU.alu_add, False, self._rd, self._rs1, self._rs2, m_state)

    def _SUB(self, m_state):
        Instr_I.exec_OP(ALU.alu_sub, False, self._rd, self._rs1, self._rs2, m_state)

    def _SLT(self, m_state):
        Instr_I.exec_OP(ALU.alu_slt, False, self._rd, self._rs1, self._rs2, m_state)

    def _SLTU(self, m_state):
        Instr_I.exec_OP(ALU.alu_sltu, False, self._rd, self._rs1, self._rs2, m_state)

    def _XOR(self, m_state):
        Instr_I.exec_OP(ALU.alu_xor, False, self._rd, self._rs1, self._rs2, m_state)

    def _OR(self, m_state):
        Instr_I.exec_OP(ALU.alu_or, False, self._rd, self._rs1, self._rs2, m_state)

    def _AND(self, m_state):
        Instr_I.exec_OP(ALU.alu_and, False, self._rd, self._rs1, self._rs2, m_state)

    def _SLL(self, m_state):
        Instr_I.exec_OP(ALU.alu_sll, False, self._rd, self._rs1, self._rs2, m_state)

    def _SRL(self, m_state):
        Instr_I.exec_OP(ALU.alu_srl, False, self._rd, self._rs1, self._rs2, m_state)

    def _SRA(self, m_state):
        Instr_I.exec_OP(ALU.alu_sra, False, self._rd, self._rs1, self._rs2, m_state)

    def _ADDW(self, m_state):
        Instr_I.exec_OP_32(ALU.alu_addw, False, self._rd, self._rs1, self._rs2, m_state)

    def _SUBW(self, m_state):
        Instr_I.exec_OP_32(ALU.alu_subw, False, self._rd, self._rs1, self._rs2, m_state)

    def _SLLW(self, m_state):
        Instr_I.exec_OP_32(ALU.alu_sllw, False, self._rd, self._rs1, self._rs2, m_state)

    def _SRLW(self, m_state):
        Instr_I.exec_OP_32(ALU.alu_srlw, False, self._rd, self._rs1, self._rs2, m_state)

    def _SRAW(self, m_state):
        Instr_I.exec_OP_32(ALU.alu_sraw, False, self._rd, self._rs1, self._rs2, m_state)

    @classmethod
    def exec_AUIPC(cls, is_C, rd, imm20, m_state):
        s_offset = Bit_Utils.get_signed(32, imm20 << 12)
        rd_val = ALU.alu_add(s_offset, m_state.pc)
        Instr_Common.finish_rd_and_pc_incr(rd, rd_val, is_C, m_state)

    @classmethod
    def exec_JAL(cls, is_C, rd, imm21, m_state):
        pc = m_state.pc
        if is_C:
            rd_val = pc + 2
        else:
            rd_val = pc + 4

        s_offset = Bit_Utils.get_signed(21, imm21)
        new_pc = ALU.alu_add(pc, s_offset)
        Instr_Common.finish_rd_and_pc(rd, rd_val, new_pc, m_state)

    @classmethod
    def exec_JALR(cls, is_C, rd, rs1, imm12, m_state):
        pc = m_state.pc
        if is_C:
            rd_val = pc + 2
        else:
            rd_val = pc + 4
        rs1_val = m_state.gprs.get_reg(rs1)
        s_offset = Bit_Utils.get_signed(12, imm12)
        new_pc = ALU.alu_add(rs1_val, s_offset)
        Instr_Common.finish_rd_and_pc(rd, rd_val, new_pc, m_state)

    @classmethod
    def exec_OP(cls, alu_op, is_C, rd, rs1, rs2, m_state):
        rs1_val = m_state.gprs.get_reg(rs1)
        rs2_val = m_state.gprs.get_reg(rs2)
        rd_val = alu_op(rs1_val, rs2_val)
        Instr_Common.finish_rd_and_pc_incr(rd, rd_val, is_C, m_state)

    @classmethod
    def exec_OP_32(cls, alu_op, is_C, rd, rs1, rs2, m_state):
        rs1_val = m_state.gprs.get_reg(rs1)
        rs2_val = m_state.gprs.get_reg(rs2)
        rd_val = alu_op(rs1_val, rs2_val)
        Instr_Common.finish_rd_and_pc_incr(rd, rd_val, is_C, m_state)

    @classmethod
    def exec_OP_IMM(cls, alu_op, is_C, rd, rs1, imm12, m_state):
        rs1_val = m_state.gprs.get_reg(rs1)
        s_imm = Bit_Utils.get_signed(12, imm12)
        rd_val = alu_op(rs1_val, s_imm)
        Instr_Common.finish_rd_and_pc_incr(rd, rd_val, is_C, m_state)

    @classmethod
    def exec_OP_IMM_32(cls, alu_op, is_C, rd, rs1, v2, m_state):
        rs1_val = m_state.gprs.get_reg(rs1)
        rd_val = alu_op(rs1_val, v2)
        Instr_Common.finish_rd_and_pc_incr(rd, rd_val, is_C, m_state)

    @classmethod
    def exec_LOAD(cls, is_C, rd, rs1, imm12, funct3, m_state):
        # Compute effective address
        rs1_val = m_state.gprs.get_reg(rs1)
        s_imm12 = Bit_Utils.get_signed(12, imm12)
        addr = ALU.alu_add(rs1_val, s_imm12)

        res = m_state.mem.get_mem(addr)
        if funct3 == RISCV_FUNCT3.LBU or funct3 == RISCV_FUNCT3.LHU or funct3 == RISCV_FUNCT3.LWU:
            mask = 0xffff_ffff_ffff_ffff
            rd_val = res & mask
        else:
            rd_val = res

        Instr_Common.finish_rd_and_pc_incr(rd, rd_val, is_C, m_state)

    @classmethod
    def exec_STORE(cls, is_C, rs1, rs2, imm12, funct3, m_state):
        rs2_val = m_state.gprs.get_reg(rs2)

        rs1_val = m_state.gprs.get_reg(rs1)
        s_imm12 = Bit_Utils.get_signed(12, imm12)
        addr = ALU.alu_add(rs1_val, s_imm12)

        m_state.mem.set_mem(addr, rs2_val)
        Instr_Common.finish_pc_incr(is_C, m_state)

    @classmethod
    def exec_BRANCH(cls, branch_alu_op, is_C, rs1, rs2, imm13, m_state):
        rs1_val = m_state.gprs.get_reg(rs1)
        rs2_val = m_state.gprs.get_reg(rs2)
        taken = branch_alu_op(rs1_val, rs2_val)

        pc = m_state.pc
        s_offset = Bit_Utils.get_signed(13, imm13)
        target = ALU.alu_add(pc, s_offset)
        if taken:
            new_pc = target
        elif is_C:
            new_pc = pc + 2
        else:
            new_pc = pc + 4

        Instr_Common.finish_pc(new_pc, m_state)


if __name__ == '__main__':
    m = Machine_State()
    i = Instr_I(0x4197, False)
    i.execute(m)
    m.printState()
