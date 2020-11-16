import struct

elfHeader = {}


def verify_elf(fileName: str):
    f = open(fileName, "rb")
    magic = f.read(16)
    elfStr = chr(magic[1]) + chr(magic[2]) + chr(magic[3])
    if magic[0] != 127 or elfStr != 'ELF':
        print("not ELF file")
        return False
    tmp = f.read(struct.calcsize('2HI3QI6H'))
    tmp = struct.unpack('2HI3QI6H', tmp)
    elfHeader['magic'] = magic
    elfHeader['e_type'] = tmp[0]
    elfHeader['e_machine'] = tmp[1]
    elfHeader['e_version'] = tmp[2]
    elfHeader['e_entry'] = tmp[3]
    elfHeader['e_phoff'] = tmp[4]
    elfHeader['e_shoff'] = tmp[5]
    elfHeader['e_flags'] = tmp[6]
    elfHeader['e_ehsize'] = tmp[7]
    elfHeader['e_phentsize'] = tmp[8]
    elfHeader['e_phnum'] = tmp[9]
    elfHeader['e_shentsize'] = tmp[10]
    elfHeader['e_shnum'] = tmp[11]
    elfHeader['e_shstrndx'] = tmp[12]
    f.close()
    return True


def show_elfHeader(fileName: str):
    if not verify_elf(fileName):
        return
    magic = elfHeader['magic']
    if magic[4] == 1:
        print("Class:                              ELF32")
    else:
        print("Class:                              ELF64")
    if magic[5] == 1:
        print("Data:                               2's complement, little endian")
    else:
        print("Data:                               2's complement, big endian")
    print("Version:                            %d(current)" % (magic[6]))
    if magic[7] == 0:
        os_abi = 'System V ABI'
    if magic[7] == 1:
        os_abi = 'System V ABI'
    if magic[7] == 255:
        os_abi = 'Standalone (embedded) application'
    print("OS/ABI:                             %s" % os_abi)
    print("ABI Version:                        %d" % magic[8])
    if elfHeader['e_type'] == 0:
        type = 'No file type'
    elif elfHeader['e_type'] == 1:
        type = 'Relocatable object file'
    elif elfHeader['e_type'] == 2:
        type = 'Executable file'
    elif elfHeader['e_type'] == 3:
        type = 'Core file'
    print("Type:                               %s" % type)
    print("Machine:                            %d" % elfHeader['e_machine'])
    print("Version:                            0x%x" % elfHeader['e_version'])
    print("Entry point address:                0x%x" % elfHeader['e_entry'])
    print("Start of program header:            %d (bytes into file)" % elfHeader['e_phoff'])
    print("Start of section header:            %d (bytes into file)" % elfHeader['e_shoff'])
    print("Flags:                              0x%x" % elfHeader['e_flags'])
    print("Size of this header:                %d (bytes)" % elfHeader['e_ehsize'])
    print("Size of program header:             %d (bytes)" % elfHeader['e_phentsize'])
    print("Number of program headers           %d" % elfHeader['e_phnum'])
    print("Size of section header:             %d (bytes)" % elfHeader['e_shentsize'])
    print("Number of section headers:          %d" % elfHeader['e_shnum'])
    print("Section header string table index:  %d" % elfHeader['e_shstrndx'])


def get_Instrs(fileName: str):
    if not verify_elf(fileName):
        return
    sec_start = elfHeader['e_shoff']
    sec_size = elfHeader['e_shentsize']
    f = open(fileName, 'rb')
    f.seek(sec_start)
    f.read(sec_size)
    tmp = f.read(sec_size)
    tmp = struct.unpack('2I4Q2I2Q', tmp)
    text_start_addr = tmp[3]
    text_offset = tmp[4]
    text_size = tmp[5]
    text_end_addr = text_start_addr + text_size
    # print('%x' % text_offset)
    pc = elfHeader['e_entry']
    # print('%x' % pc)
    f.close()

    instrs = {}
    addr = text_start_addr
    f = open(fileName, 'rb')
    f.seek(text_offset)
    while addr != text_end_addr:
        tmp = int.from_bytes(f.read(2), byteorder='little', signed=False)
        # print('%x: ' % addr, end='')
        if tmp & 0b11 == 0b11:
            tmp += int.from_bytes(f.read(2), byteorder='little', signed=False) << 16
            instrs[addr] = tmp
            addr += 4
        else:
            instrs[addr] = tmp
            addr += 2
        # print('%x' % tmp)

    return pc, instrs


if __name__ == '__main__':
    pc, instrs = get_Instrs("a.out")
    print('pc: %x' % pc)
#     show_elfHeader("a.out")
