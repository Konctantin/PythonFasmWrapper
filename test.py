import fasm

fasm = fasm.FASM("FASM.DLL")

byte_str = fasm.AssembleAsStr("use32\n pop eax")

print(byte_str, "= 0x58")