import Messages_Declear
from pathlib import Path
import os
import gnureadline
class mdoc:
    def __init__(self,filename: str | None = ..., tag: str | None = "others"):
        path_to_file = str(Path(tag).absolute()) + "/" + filename
        if not os.path.exists(path=path_to_file):
            file = open(path_to_file, 'w')
            while True:
                try:
                    inputs = str(input("|t|"))
                    file.write(inputs)
                    file.write('\n')
                except EOFError:
                    break
                except KeyboardInterrupt:
                    ...
        else:
            print("mdoc:", Messages_Declear.FileExists)

def mdoc_info():
    print("mdoc: make a text document")
    print("Command Syntax: mdoc [file name] [file tag]")
    print("[file name]: name of the file, with extension name")
    print("[file tag]: tag of the file: tpa, tpb, tpc. If empty, the file will be taged as others")
    print("Use command `mkly` to make custom tags")