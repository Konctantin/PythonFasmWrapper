# PythonFasmWrapper

Python binding to [fasm.dll](http://board.flatassembler.net/topic.php?t=6239)

### Usage
```py
import fasm

fasmDll = fasm.FASM("<fasm_dll_folder>\\fasm.dll") # init
byte_arr = fasmDll.Assemble("use32\n pop eax") # return byte array
byte_str = fasmDll.AssembleAsStr("use32\n pop eax")
```
