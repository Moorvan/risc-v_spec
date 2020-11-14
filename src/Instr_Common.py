
class Instr_Common:

    @classmethod
    def finish_rd_and_pc_incr(cls, rd, rd_val, is_C, m_state):
        if is_C:
            m_state.pc += 2
        else:
            m_state.pc += 4
        m_state.gprs.set_reg(rd, rd_val)

    @classmethod
    def finish_pc_incr(cls, is_C, m_state):
        if is_C:
            m_state.pc += 2
        else:
            m_state.pc += 4

    @classmethod
    def finish_rd_and_pc(cls, rd, rd_val, new_pc, m_state):
        m_state.gprs.set_reg(rd, rd_val)
        m_state.pc = new_pc

    @classmethod
    def finish_pc(cls, new_pc, m_state):
        m_state.pc = new_pc