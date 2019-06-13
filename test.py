import fasm

fasmDll = fasm.FASM("FASM.DLL")

byte_str = fasmDll.AssembleAsStr("use32\n pop eax")

print(byte_str, "= 0x58")