from capstone import *

MOV = "mov	cx, word ptr [edi + "
SHR = "shr	cx, "
CMP = "cmp	cx, "

code = [[0]*8]*0x400

def patchBytes():
    f = open('data.bin', 'rb')
    dat = f.read()
    dat = dat.replace(b'\x00\x00\x00\xe9', b'\x00\x00\x00\x90')
    g = open('patchedData.bin', 'ab')
    g.write(dat)
    g.close()
    f.close()


def disasm():
    f = open('patchedData.bin', 'rb')
    dat = f.read()
    md = Cs(CS_ARCH_X86, CS_MODE_32)
    for (address, size, mnemonic, op_str) in md.disasm_lite(dat, 0x1000):
        print("%s\t%s" %(mnemonic, op_str))
    f.close()

    
info = []
def parse():
    
    with open('disasm.txt', 'r') as f:
        while (line := f.readline().strip()):
            if MOV in line:
                offset = int(line[len(MOV):-1], 0)
                line2 = f.readline().strip()
                bitoff = int(line2[len(SHR)])
                line3 = f.readline().strip()
                line3 = f.readline().strip()
                setbit = int(line3[len(CMP):])
                info.append((offset, bitoff, setbit))
    info.sort(key=lambda y: y[0])

code = []
def getflag():
    parse()

    tmp = []
    for (offset, bitoff, setbit) in info:
        if len(tmp) >= 8:
            tmp.sort(key=lambda y: y[1])
            tmp = tmp[::-1]
            dig = []
            for (off, bit, setb) in tmp:
                dig.append(setb)
            code.append(dig)
            tmp = []
      
        tmp.append((offset, bitoff, setbit))

    flag = []
    for binList in code:
        a = int("".join(str(i) for i in binList),2)
        flag.append(a)

    flag = ''.join([chr(i) for i in flag])
    return flag


flag = getflag()

print(flag)





