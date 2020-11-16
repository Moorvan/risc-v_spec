from Machine_State import *


class Instr_Common:

    @classmethod
    def finish_rd_and_pc_incr(cls, rd: int, rd_val: int, is_C: bool, m_state: Machine_State):
        if is_C:
            m_state.pc += 2
        else:
            m_state.pc += 4
        m_state.gprs.set_reg(rd, rd_val)

    @classmethod
    def finish_pc_incr(cls, is_C: bool, m_state: Machine_State):
        if is_C:
            m_state.pc += 2
        else:
            m_state.pc += 4

    @classmethod
    def finish_rd_and_pc(cls, rd: int, rd_val: int, new_pc: int, m_state: Machine_State):
        m_state.gprs.set_reg(rd, rd_val)
        m_state.pc = new_pc

    @classmethod
    def finish_pc(cls, new_pc: int, m_state: Machine_State):
        m_state.pc = new_pc
