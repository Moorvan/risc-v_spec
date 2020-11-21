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

        # CI format
        self._rd_rs1_CI = Bit_Utils.bit_slice(self._instr, 11, 7)
        self._imm6_CI = (Bit_Utils.bit_slice(self._instr, 12, 12) << 5) | \
                        (Bit_Utils.bit_slice(self._instr, 6, 2))
        self._imm8_CI = (Bit_Utils.bit_slice(self._instr, 12, 12) << 5) | \
                        (Bit_Utils.bit_slice(self._instr, 6, 4) << 2) | \
                        (Bit_Utils.bit_slice(self._instr, 3, 2) << 6)
        self._imm9_CI = (Bit_Utils.bit_slice(self._instr, 12, 12) << 5) | \
                        (Bit_Utils.bit_slice(self._instr, 6, 5) << 3) | \
                        (Bit_Utils.bit_slice(self._instr, 4, 2) << 6)
        self._imm10_CI = (Bit_Utils.bit_slice(self._instr, 12, 12) << 5) | \
                         (Bit_Utils.bit_slice(self._instr, 6, 6) << 4) | \
                         (Bit_Utils.bit_slice(self._instr, 5, 2) << 6)
        self._nzimm10_CI = (Bit_Utils.bit_slice(self._instr, 12, 12) << 9) | \
                           (Bit_Utils.bit_slice(self._instr, 6, 6) << 4) | \
                           (Bit_Utils.bit_slice(self._instr, 5, 5) << 6) | \
                           (Bit_Utils.bit_slice(self._instr, 4, 3) << 7) | \
                           (Bit_Utils.bit_slice(self._instr, 2, 2) << 5)

        # CSS format
        self._rs2_CSS = Bit_Utils.bit_slice(self._instr, 6, 2)
        self._uimm8_CSS = (Bit_Utils.bit_slice(self._instr, 12, 9) << 2) | \
                          (Bit_Utils.bit_slice(self._instr, 8, 7) << 6)
        self._uimm9_CSS = (Bit_Utils.bit_slice(self._instr, 12, 10) << 3) | \
                          (Bit_Utils.bit_slice(self._instr, 9, 7) << 6)
        self._uimm10_CSS = (Bit_Utils.bit_slice(self._instr, 12, 11) << 4) | \
                           (Bit_Utils.bit_slice(self._instr, 10, 7) << 6)

        # CIW format
        self._rd_CIW = (0x8 | Bit_Utils.bit_slice(self._instr, 4, 2))
        self._nzuimm10_CIW = (Bit_Utils.bit_slice(self._instr, 12, 11) << 4) | \
                             (Bit_Utils.bit_slice(self._instr, 10, 7) << 6) | \
                             (Bit_Utils.bit_slice(self._instr, 6, 6) << 2) | \
                             (Bit_Utils.bit_slice(self._instr, 5, 5) << 3)

        # CL format
        self._rd_CL = (0x8 | Bit_Utils.bit_slice(self._instr, 4, 2))
        self._rs1_CL = (0x8 | Bit_Utils.bit_slice(self._instr, 9, 7))
        self._uimm7_CL = (Bit_Utils.bit_slice(self._instr, 12, 10) << 3) | \
                         (Bit_Utils.bit_slice(self._instr, 6, 6) << 2) | \
                         (Bit_Utils.bit_slice(self._instr, 5, 5) << 6)
        self._uimm8_CL = (Bit_Utils.bit_slice(self._instr, 12, 10) << 3) | \
                         (Bit_Utils.bit_slice(self._instr, 6, 5) << 6)
        self._uimm9_CL = (Bit_Utils.bit_slice(self._instr, 12, 11) << 3) | \
                         (Bit_Utils.bit_slice(self._instr, 10, 10) << 8) | \
                         (Bit_Utils.bit_slice(self._instr, 6, 5) << 6)

        # CS format
        self._rs2_CS = (0x8 | Bit_Utils.bit_slice(self._instr, 4, 2))
        self._rs1_CS = (0x8 | Bit_Utils.bit_slice(self._instr, 9, 7))
        self._uimm7_CS = (Bit_Utils.bit_slice(self._instr, 12, 10) << 3) | \
                         (Bit_Utils.bit_slice(self._instr, 6, 6) << 2) | \
                         (Bit_Utils.bit_slice(self._instr, 5, 5) << 6)
        self._uimm8_CS = (Bit_Utils.bit_slice(self._instr, 12, 10) << 3) | \
                         (Bit_Utils.bit_slice(self._instr, 6, 5) << 6)
        self._uimm9_CS = (Bit_Utils.bit_slice(self._instr, 12, 11) << 4) | \
                         (Bit_Utils.bit_slice(self._instr, 10, 10) << 8) | \
                         (Bit_Utils.bit_slice(self._instr, 6, 5) << 6)

        # CA format
        self._funct6_CA = Bit_Utils.bit_slice(self._instr, 15, 10)
        self._rd_rs1_CA = 0x8 | Bit_Utils.bit_slice(self._instr, 9, 7)
        self._funct2_CA = Bit_Utils.bit_slice(self._instr, 6, 5)
        self._rs2_CA = 0x8 | Bit_Utils.bit_slice(self._instr, 4, 2)

        # CB format
        self._rd_rs1_CB = (0x8 | Bit_Utils.bit_slice(self._instr, 9, 7))
        self._imm6_CB = (Bit_Utils.bit_slice(self._instr, 12, 12) << 5) | \
                        (Bit_Utils.bit_slice(self._instr, 6, 2))
        self._imm9_CB = (Bit_Utils.bit_slice(self._instr, 12, 12) << 8) | \
                        (Bit_Utils.bit_slice(self._instr, 11, 10) << 3) | \
                        (Bit_Utils.bit_slice(self._instr, 6, 5) << 6) | \
                        (Bit_Utils.bit_slice(self._instr, 4, 3) << 1) | \
                        (Bit_Utils.bit_slice(self._instr, 2, 2) << 5)

        # CJ format
        self._imm12_CJ = (Bit_Utils.bit_slice(self._instr, 12, 12) << 11) | \
                         (Bit_Utils.bit_slice(self._instr, 11, 11) << 4) | \
                         (Bit_Utils.bit_slice(self._instr, 10, 9) << 8) | \
                         (Bit_Utils.bit_slice(self._instr, 8, 8) << 10) | \
                         (Bit_Utils.bit_slice(self._instr, 7, 7) << 6) | \
                         (Bit_Utils.bit_slice(self._instr, 6, 6) << 7) | \
                         (Bit_Utils.bit_slice(self._instr, 5, 3) << 1) | \
                         (Bit_Utils.bit_slice(self._instr, 2, 2) << 5)

        self._op = self._C_ADD
        if self._opcode == RISCV_OPCODE.C0:
            if self._funct3 == RISCV_FUNCT3.C_ADDI4SPN and self._nzuimm10_CIW != 0:
                self._op = self._C_ADDI4SPN
            elif self._funct3 == RISCV_FUNCT3.C_LW:
                self._op = self._C_LW
            elif self._funct3 == RISCV_FUNCT3.C_LD:
                self._op = self._C_LD
            elif self._funct3 == RISCV_FUNCT3.C_SW:
                self._op = self._C_SW
            elif self._funct3 == RISCV_FUNCT3.C_SD:
                self._op = self._C_SD
        elif self._opcode == RISCV_OPCODE.C1:
            if self._funct3 == RISCV_FUNCT3.C_NOP and self._rd_rs1_CI == 0 and self._imm6_CI == 0:
                self._op = self._C_NOP
            elif self._funct3 == RISCV_FUNCT3.C_ADDI and self._rd_rs1_CI != 0 and self._imm6_CI != 0:
                self._op = self._C_ADDI
            elif self._funct3 == RISCV_FUNCT3.C_JAL:
                self._op = self._C_JAL
            elif self._funct3 == RISCV_FUNCT3.C_ADDIW and self._rd_rs1_CI != 0:
                self._op = self._C_ADDIW
            elif self._funct3 == RISCV_FUNCT3.C_LI and self._rd_rs1_CI != 0:
                self._op = self._C_LI
            elif self._funct3 == RISCV_FUNCT3.C_ADDI16SP and self._rd_rs1_CI == 2 and self._nzimm10_CI != 0:
                self._op = self._C_ADDI16SP
            elif self._funct3 == RISCV_FUNCT3.C_LUI and self._rd_rs1_CI != 0 and \
                    self._rd_rs1_CI != 2 and self._imm6_CI != 0:
                self._op = self._C_LUI
            elif self._is_C_SRLI():
                self._op = self._C_SRLI
            elif self._is_C_SRAI():
                self._op = self._C_SRAI
            elif self._is_C_ANDI():
                self._op = self._C_ANDI
            elif self._funct6_CA == RISCV_OTHER.FUNCT6_C_SUB and self._funct2_CA == RISCV_OTHER.FUNCT2_C_SUB:
                self._op = self._C_SUB
            elif self._funct6_CA == RISCV_OTHER.FUNCT6_C_XOR and self._funct2_CA == RISCV_OTHER.FUNCT2_C_XOR:
                self._op = self._C_XOR
            elif self._funct6_CA == RISCV_OTHER.FUNCT6_C_OR and self._funct2_CA == RISCV_OTHER.FUNCT2_C_OR:
                self._op = self._C_OR
            elif self._funct6_CA == RISCV_OTHER.FUNCT6_C_AND and self._funct2_CA == RISCV_OTHER.FUNCT2_C_AND:
                self._op = self._C_AND
            elif self._funct6_CA == RISCV_OTHER.FUNCT6_C_SUBW and self._funct2_CA == RISCV_OTHER.FUNCT2_C_SUBW:
                self._op = self._C_SUBW
            elif self._funct6_CA == RISCV_OTHER.FUNCT6_C_ADDW and self._funct2_CA == RISCV_OTHER.FUNCT2_C_ADDW:
                self._op = self._C_ADDW
            elif self._funct3 == RISCV_FUNCT3.C_J:
                self._op = self._C_J
            elif self._funct3 == RISCV_FUNCT3.C_BEQZ:
                self._op = self._C_BEQZ
            elif self._funct3 == RISCV_FUNCT3.C_BNEZ:
                self._op = self._C_BNEZ
        elif self._opcode == RISCV_OPCODE.C2:
            if self._is_C_SLLI():
                self._op = self._C_SLLI
            elif self._funct3 == RISCV_FUNCT3.C_LWSP and self._rd_rs1_CI != 0:
                self._op = self._C_LWSP
            elif self._funct3 == RISCV_FUNCT3.C_LDSP and self._rd_rs1_CI != 0:
                self._op = self._C_LDSP
            elif self._funct4_CR == RISCV_OTHER.FUNCT4_C_JR and self._rd_rs1_CR != 0 and self._rs2_CR == 0:
                self._op = self._C_JR
            elif self._funct4_CR == RISCV_OTHER.FUNCT4_C_MV and self._rd_rs1_CR != 0 and self._rs2_CR != 0:
                self._op = self._C_MV
            elif self._funct4_CR == RISCV_OTHER.FUNCT4_C_EBREAK and self._rd_rs1_CR == 0 and self._rs2_CR == 0:
                self._op = self._C_EBREAK
            elif self._funct4_CR == RISCV_OTHER.FUNCT4_C_JALR and self._rd_rs1_CR != 0 and self._rs2_CR == 0:
                self._op = self._C_JALR
            elif self._funct4_CR == RISCV_OTHER.FUNCT4_C_ADD and self._rd_rs1_CR != 0 and self._rs2_CR != 0:
                self._op = self._C_ADD
            elif self._funct3 == RISCV_FUNCT3.C_SWSP:
                self._op = self._C_SWSP
            elif self._funct3 == RISCV_FUNCT3.C_SDSP:
                self._op = self._C_SDSP
        print(self._op)

    def _instr_fields_CI(self):
        funct3 = Bit_Utils.bit_slice(self._instr, 15, 13)
        imm_12 = Bit_Utils.bit_slice(self._instr, 12, 12)
        rd_rs1 = Bit_Utils.bit_slice(self._instr, 11, 7)
        imm_6_2 = Bit_Utils.bit_slice(self._instr, 6, 2)
        op = Bit_Utils.bit_slice(self._instr, 1, 0)
        return funct3, imm_12, rd_rs1, imm_6_2, op

    def _instr_fields_CB(self):
        funct3 = Bit_Utils.bit_slice(self._instr, 15, 13)
        offset_12_10 = Bit_Utils.bit_slice(self._instr, 12, 10)
        rs1_prime = Bit_Utils.bit_slice(self._instr, 9, 7)
        offset_6_2 = Bit_Utils.bit_slice(self._instr, 6, 2)
        op = Bit_Utils.bit_slice(self._instr, 1, 0)
        return funct3, offset_12_10, rs1_prime, offset_6_2, op

    def execute(self, m_state: Machine_State):
        self._op(m_state)

    def _C_ADDI4SPN(self, m_state):
        rs1 = 2
        imm12 = self._nzuimm10_CIW
        rd = self._rd_CIW
        Instr_I.exec_OP_IMM(ALU.alu_add, True, rd, rs1, imm12, m_state)

    def _C_LW(self, m_state):
        imm12 = self._uimm7_CL
        rd = self._rd_CL
        rs1 = self._rs1_CL
        Instr_I.exec_LOAD(True, rd, rs1, imm12, RISCV_FUNCT3.LW, m_state)

    def _C_LD(self, m_state):
        imm12 = self._uimm8_CL
        rd = self._rd_CL
        rs1 = self._rs1_CL
        Instr_I.exec_LOAD(True, rd, rs1, imm12, RISCV_FUNCT3.LD, m_state)

    def _C_SW(self, m_state):
        imm12 = self._uimm7_CS
        rs1 = self._rs1_CS
        rs2 = self._rs2_CS
        Instr_I.exec_STORE(True, rs1, rs2, imm12, RISCV_FUNCT3.SW, m_state)

    def _C_SD(self, m_state):
        imm12 = self._uimm8_CS
        rs1 = self._rs1_CS
        rs2 = self._rs2_CS
        Instr_I.exec_STORE(True, rs1, rs2, imm12, RISCV_FUNCT3.SD, m_state)

    # C_NOP: expands to 'nop' (ADDI x0, x0, 0)
    def _C_NOP(self, m_state):
        rd = 0
        rs1 = 0
        imm12 = 0
        Instr_I.exec_OP_IMM(ALU.alu_add, True, rd, rs1, imm12, m_state)

    def _C_ADDI(self, m_state):
        imm12 = Bit_Utils.get_signed(6, self._imm6_CI)
        rd_rs1 = self._rd_rs1_CI
        Instr_I.exec_OP_IMM(ALU.alu_add, True, rd_rs1, rd_rs1, imm12, m_state)

    def _C_JAL(self, m_state):
        rd = 1
        imm21 = Bit_Utils.get_signed(12, self._imm12_CJ)
        Instr_I.exec_JAL(True, rd, imm21, m_state)

    def _C_ADDIW(self, m_state):
        imm12 = Bit_Utils.get_signed(6, self._imm6_CI)
        rd_rs1 = self._rd_rs1_CI
        Instr_I.exec_OP_IMM_32(ALU.alu_addw, True, rd_rs1, rd_rs1, imm12, m_state)

    def _C_LI(self, m_state):
        imm12 = Bit_Utils.get_signed(6, self._imm6_CI)
        rd_rs1 = self._rd_rs1_CI
        Instr_I.exec_OP_IMM(ALU.alu_add, True, rd_rs1, rd_rs1, imm12, m_state)

    def _C_ADDI16SP(self, m_state):
        imm12 = Bit_Utils.get_signed(10, self._nzimm10_CI)
        rd = 2
        rs1 = 2
        Instr_I.exec_OP_IMM(ALU.alu_add, True, rd, rs1, imm12, m_state)

    def _C_LUI(self, m_state):
        imm20 = Bit_Utils.get_signed(6, self._imm6_CI)
        rd_rs1 = self._rd_rs1_CI
        Instr_I.exec_LUI(True, rd_rs1, imm20, m_state)

    def _is_C_SRLI(self):
        funct3, offset_12_10, r_prime, offset_6_2, op = self._instr_fields_CB()
        shamt6_5 = Bit_Utils.bit_slice(offset_12_10, 2, 2)
        shamt6 = (shamt6_5 << 5) | offset_6_2
        funct2 = Bit_Utils.bit_slice(offset_12_10, 1, 0)
        if funct3 == RISCV_FUNCT3.C_SRLI and funct2 == RISCV_OTHER.FUNCT2_C_SRLI and \
           op == RISCV_OPCODE.C1 and shamt6 != 0:
            return True
        return False

    def _C_SRLI(self, m_state):
        rd_rs1 = self._rd_rs1_CB
        shamt6 = self._imm6_CB
        Instr_I.exec_OP_IMM(ALU.alu_srl, True, rd_rs1, rd_rs1, shamt6, m_state)

    def _is_C_SRAI(self):
        funct3, offset_12_10, r_prime, offset_6_2, op = self._instr_fields_CB()
        shamt6_5 = Bit_Utils.bit_slice(offset_12_10, 2, 2)
        shamt6 = (shamt6_5 << 5) | offset_6_2
        funct2 = Bit_Utils.bit_slice(offset_12_10, 1, 0)
        if funct3 == RISCV_FUNCT3.C_SRAI and funct2 == RISCV_OTHER.FUNCT2_C_SRAI and \
           op == RISCV_OPCODE.C1 and shamt6 != 0:
            return True
        return False

    def _C_SRAI(self, m_state):
        rd_rs1 = self._rd_rs1_CB
        shamt6 = self._imm6_CB
        Instr_I.exec_OP_IMM(ALU.alu_sra, True, rd_rs1, rd_rs1, shamt6, m_state)

    def _is_C_ANDI(self):
        funct3, offset_12_10, r_prime, offset_6_2, op = self._instr_fields_CB()
        funct2 = Bit_Utils.bit_slice(offset_12_10, 1, 0)
        if funct3 == RISCV_FUNCT3.ANDI and funct2 == RISCV_OTHER.FUNCT2_C_ANDI and \
           op == RISCV_OPCODE.C1:
            return True
        return False

    def _C_ANDI(self, m_state):
        rd_rs1 = self._rd_rs1_CB
        imm12 = Bit_Utils.get_signed(6, self._imm6_CB)
        Instr_I.exec_OP_IMM(ALU.alu_and, True, rd_rs1, rd_rs1, imm12, m_state)

    def _C_SUB(self, m_state):
        rd_rs1 = self._rd_rs1_CA
        rs2 = self._rs2_CA
        Instr_I.exec_OP(ALU.alu_sub, True, rd_rs1, rd_rs1, rs2, m_state)

    def _C_XOR(self, m_state):
        rd_rs1 = self._rd_rs1_CA
        rs2 = self._rs2_CA
        Instr_I.exec_OP(ALU.alu_xor, True, rd_rs1, rd_rs1, rs2, m_state)

    def _C_OR(self, m_state):
        rd_rs1 = self._rd_rs1_CA
        rs2 = self._rs2_CA
        Instr_I.exec_OP(ALU.alu_or, True, rd_rs1, rd_rs1, rs2, m_state)

    def _C_AND(self, m_state):
        rd_rs1 = self._rd_rs1_CA
        rs2 = self._rs2_CA
        Instr_I.exec_OP(ALU.alu_and, True, rd_rs1, rd_rs1, rs2, m_state)

    def _C_SUBW(self, m_state):
        rd_rs1 = self._rd_rs1_CA
        rs2 = self._rs2_CA
        Instr_I.exec_OP_32(ALU.alu_subw, True, rd_rs1, rd_rs1, rs2, m_state)

    def _C_ADDW(self, m_state):
        rd_rs1 = self._rd_rs1_CA
        rs2 = self._rs2_CA
        Instr_I.exec_OP_32(ALU.alu_addw, True, rd_rs1, rd_rs1, rs2, m_state)

    def _C_J(self, m_state):
        imm12 = self._imm12_CJ
        rd = 0
        imm21 = Bit_Utils.get_signed(12, imm12)
        Instr_I.exec_JAL(True, rd, imm21, m_state)

    def _C_BEQZ(self, m_state):
        rs1 = self._rd_rs1_CB
        imm9 = self._imm9_CB
        rs2 = 0
        imm13 = Bit_Utils.get_signed(9, imm9)
        Instr_I.exec_BRANCH(ALU.alu_eq, True, rs1, rs2, imm13, m_state)

    def _C_BNEZ(self, m_state):
        rs1 = self._rd_rs1_CB
        imm9 = self._imm9_CB
        rs2 = 0
        imm13 = Bit_Utils.get_signed(9, imm9)
        Instr_I.exec_BRANCH(ALU.alu_ne, True, rs1, rs2, imm13, m_state)

    def _is_C_SLLI(self):
        funct3, imm_12, rd_rs1, imm_6_2, op = self._instr_fields_CI()
        shamt6_5 = imm_12
        shamt6 = (shamt6_5 << 5) | imm_6_2
        if funct3 == RISCV_FUNCT3.SLLI and op == RISCV_OPCODE.C2 and shamt6 != 0:
            return True
        return False

    def _C_SLLI(self, m_state):
        rd_rs1 = self._rd_rs1_CI
        shamt6 = self._imm6_CI
        Instr_I.exec_OP_IMM(ALU.alu_sll, True, rd_rs1, rd_rs1, shamt6, m_state)

    def _C_LWSP(self, m_state):
        rd = self._rd_rs1_CI
        uimm8 = self._imm8_CI
        rs1 = 2
        imm12 = uimm8
        Instr_I.exec_LOAD(True, rd, rs1, imm12, RISCV_FUNCT3.LW, m_state)

    def _C_LDSP(self, m_state):
        rd = self._rd_rs1_CI
        uimm9 = self._imm9_CI
        rs1 = 2
        imm12 = uimm9
        Instr_I.exec_LOAD(True, rd, rs1, imm12, RISCV_FUNCT3.LD, m_state)

    def _C_JR(self, m_state):
        rs1 = self._rd_rs1_CR
        rd = 0
        imm12 = 0
        Instr_I.exec_JALR(True, rd, rs1, imm12, m_state)

    def _C_MV(self, m_state):
        rd = self._rd_rs1_CR
        rs2 = self._rs2_CR
        rs1 = 0
        Instr_I.exec_OP(ALU.alu_add, True, rd, rs1, rs2, m_state)

    def _C_EBREAK(self, m_state):
        pass

    def _C_JALR(self, m_state):
        rs1 = self._rd_rs1_CR
        rd = 1
        imm12 = 0
        Instr_I.exec_JALR(True, rd, rs1, imm12, m_state)

    def _C_ADD(self, m_state):
        rd = self._rd_rs1_CR
        rs2 = self._rs2_CR
        rs1 = rd
        Instr_I.exec_OP(ALU.alu_add, True, rd, rs1, rs2, m_state)

    def _C_SWSP(self, m_state):
        rs2 = self._rs2_CSS
        uimm8 = self._uimm8_CSS
        rs1 = 2
        imm12 = uimm8
        Instr_I.exec_STORE(True, rs1, rs2, imm12, RISCV_FUNCT3.SW, m_state)

    def _C_SDSP(self, m_state):
        rs2 = self._rs2_CSS
        uimm9 = self._uimm9_CSS
        rs1 = 2
        imm12 = uimm9
        Instr_I.exec_STORE(True, rs1, rs2, imm12, RISCV_FUNCT3.SD, m_state)


if __name__ == '__main__':
    i = Instr_C(0xeca6)
