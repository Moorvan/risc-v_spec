from ALU import *
from Machine_State import *


# This class defines part of the RISC-V 'I' (Base) instructions.

class Instr_I:
    def __init__(self, instr, op, rd, rs1, rs2=0, imm=0):
        # Map the str of op to the function of how to execute the instruction
        self.map = {
            'add': self._ADD,
            'addi': self._ADDI,
            'sd': self._SD,
            'beq': self._BEQ
        }
        self._str = instr
        self.op = self.map.get(op)
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm

    def print_instr(self):
        print(self._str)

    # this function can change the input machine state after executing the instruction
    def execute(self, m_state):
        self.op(m_state)

    def _ADD(self, m_state):
        a = m_state.gprs.get_reg(self.rs1)
        b = m_state.gprs.get_reg(self.rs2)
        m_state.gprs.set_reg(self.rd, ALU.alu_add(a, b))
        m_state.pc += 1

    def _ADDI(self, m_state):
        a = m_state.gprs.get_reg(self.rs1)
        b = self.imm
        m_state.gprs.set_reg(self.rd, ALU.alu_add(a, b))
        m_state.pc += 1

    def _SD(self, m_state):
        addr = m_state.gprs.get_reg(self.rs2) + self.imm
        a = m_state.gprs.get_reg(self.rs1)
        m_state.mem.set_mem(addr, a)

    def _BEQ(self, m_state):
        a = m_state.gprs.get_reg(self.rs1)
        b = m_state.gprs.get_reg(self.rs2)
        if ALU.alu_eq(a, b):
            m_state.pc = self.imm
