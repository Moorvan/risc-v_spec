class RISCV_OPCODE:
    # I
    LUI = 0x37
    AUIPC = 0x17
    JAL = 0x6f
    JALR = 0x67
    BRANCH = 0x63
    LOAD = 0x03
    STORE = 0x23
    OP_IMM = 0x13
    OP = 0x33
    MISC_MEM = 0x0f
    OP_IMM_32 = 0x1b
    OP_32 = 0x3b
    SYSTEM = 0x73

    # C
    C0 = 0x0
    C1 = 0x1
    C2 = 0x2


class RISCV_FUNCT3:
    # OPCODE.LOAD
    LB = 0x0
    LH = 0x1
    LW = 0x2
    LD = 0x3
    LBU = 0x4
    LHU = 0x5
    LWU = 0x6

    # OPCODE.STORE
    SB = 0x0
    SH = 0x1
    SW = 0x2
    SD = 0x3

    # OPCODE.JALR
    JALR = 0x0

    # OPCODE.BRANCH
    BEQ = 0x0
    BNE = 0x1
    BLT = 0x4
    BGE = 0x5
    BLTU = 0x6
    BGEU = 0x7

    # OPCODE.OP_IMM
    ADDI = 0x0
    SLTI = 0x2
    SLTIU = 0x3
    XORI = 0x4
    ORI = 0x6
    ANDI = 0x7
    SLLI = 0x1
    SRLI = 0x5
    SRAI = 0x5

    # OPCODE.OP_IMM_32
    ADDIW = 0x0
    SLLIW = 0x1
    SRLIW = 0x5
    SRAIW = 0x5

    # OPCODE.OP
    ADD = 0x0
    SUB = 0x0
    SLT = 0x2
    SLTU = 0x3
    XOR = 0x4
    OR = 0x6
    AND = 0x7
    SLL = 0x1
    SRL = 0x5
    SRA = 0x5

    # OPCODE.OP_32
    ADDW = 0x0
    SUBW = 0x0
    SLLW = 0x1
    SRLW = 0x5
    SRAW = 0x5

    # C
    C_LW = 0x2
    C_LD = 0x3
    C_SW = 0x6
    C_SD = 0x7
    C_JAL = 0x1
    C_J = 0x5
    C_BEQZ = 0x6
    C_BNEZ = 0x7
    C_LI = 0x2
    C_LUI = 0x3

    C_NOP = 0x0
    C_ADDI = 0x0
    C_ADDIW = 0x1
    C_ADDI16SP = 0x3
    C_ADDI4SPN = 0x0
    C_SLLI = 0x0
    C_SRLI = 0x4
    C_ANDI = 0x4


class RISCV_FUNCT7:
    # OPCODE.OP_IMM_32
    SLLIW = 0x00
    SRLIW = 0x00
    SRAIW = 0x20

    # OPCODE.OP
    ADD = 0x00
    SUB = 0x20
    SLT = 0x00
    SLTU = 0x00
    XOR = 0x00
    OR = 0x00
    AND = 0x00
    SLL = 0x00
    SRL = 0x00
    SRA = 0x20

    # OPCODE.OP_32
    ADDW = 0x00
    SUBW = 0x20
    SLLW = 0x00
    SRLW = 0x00
    SRAW = 0x20


class RISCV_OTHER:
    # OPCODE.SYSTEM
    FUNCT12_ECALL = 0x000
    FUNCT12_EBREAK = 0x001

    # for SLLI/SRLI/SRAI
    msbs6_SLLI = 0x00
    msbs6_SRLI = 0x00
    msbs6_SRAI = 0x10

    # C
    FUNCT4_C_JR = 0x8
    FUNCT4_C_JALR = 0x9
    FUNCT2_C_SRLI = 0x0
    FUNCT2_C_SRAI = 0x1
    FUNCT2_C_ANDI = 0x2
    FUNCT4_C_MV = 0x8
    FUNCT4_C_ADD = 0x9
    FUNCT6_C_AND = 0x23
    FUNCT2_C_AND = 0x3
    FUNCT6_C_OR = 0x23
    FUNCT2_C_OR = 0x2
    FUNCT6_C_XOR = 0x23
    FUNCT2_C_XOR = 0x1
    FUNCT6_C_SUB = 0x23
    FUNCT2_C_SUB = 0x0
    FUNCT4_C_EBREAK = 0x9
