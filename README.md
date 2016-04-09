# PythonFasmWrapper

Python 2.7 binding to [fasm.dll](http://board.flatassembler.net/topic.php?t=6239)

### Usage
```py
fasm = FASM("<fasm_dll_folder>\\fasm.dll") # init
byte_arr = fasm.Assemble("use32\n pop eax") # return byte array
byte_str = fasm.AssembleAsStr("use32\n pop eax") # return byte array presents as string
```
