from fileinput import filename
import Messages_Declear
from pathlib import Path
import os
import gnureadline
class mdoc:
    def __init__(self,filename: str | None = ..., tag: str | None = "others"):
        path_to_file = str(Path(tag).absolute()) + "/" + filename
        while True:
            try:
                contents = str(input(f"|{filename} >> "))
                with open(path_to_file) as file:
                    file.write(contents)
                    file.write('\n')
            except EOFError:
                break
            except KeyboardInterrupt:
                ...
def mdoc_info():
    print("mdoc: make a text document")
    print("Command Syntax: mdoc [file name] [file tag]")
    print("[file name]: name of the file, with extension name")
    print("[file tag]: tag of the file: tpa, tpb, tpc. If empty, the file will be taged as others")
    print("Use command `mkly` to make custom tags")