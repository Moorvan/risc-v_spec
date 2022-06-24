import unittest

from Instr_I import Instr_I, Bit_Utils
from Machine_State import Machine_State
from RISCV_Defs import *


class InstrTest(unittest.TestCase):
    def test_addi(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_sd(self):
        m_state = Machine_State()

        # sd rs1: x8, rs2: x15, imm12: 4072
        m_state.gprs.set_reg(n=8, v=0x10)
        m_state.gprs.set_reg(n=15, v=0x23)
        instr = Instr_I(instr=0xfef43423, is_C=False)
        instr.execute(m_state)
        imm12 = Bit_Utils.get_signed(12, 4072)
        self.assertEqual(m_state.mem.get_mem(addr=imm12 + 0x10, funct3=RISCV_FUNCT3.SD)
                         , 0x23)

    def test_jalr(self):
        m_state = Machine_State()

        # jalr rd: x1, rs1: x1, imm12: 108
        m_state.pc = 23
        m_state.gprs.set_reg(n=1, v=88)
        instr = Instr_I(0x06c080e7, False)
        instr.execute(m_state)
        offset = Bit_Utils.get_signed(12, 108)
        self.assertEqual(m_state.pc, 88 + offset)
        self.assertEqual(m_state.gprs.get_reg(n=1), 23 + 4)

    def test_add(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_lui(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_jal(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_beq(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_bne(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_blt(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_bge(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_lb(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_lw(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_ld(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_sb(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_sh(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_sw(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_or(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_and(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_slr(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)

    def test_sra(self):
        m_state = Machine_State()

        # addi rd: x2, rs1: x2, imm: 0x20
        m_state.gprs.set_reg(n=2, v=0x10)
        instr = Instr_I(instr=0x02010113, is_C=False)
        instr.execute(m_state)
        self.assertEqual(m_state.gprs.get_reg(n=2), 0x10 + 0x20)