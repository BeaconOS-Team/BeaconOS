from sys import flags
import Messages_Declear as Messages_Declear
import Console_Delcear
from pathlib import Path
import os
class strictRemove:
    def __init__(self,fileName,tag: str | None = ..., flag: str | None = ...):
        self.filename = fileName
        filePath = os.getcwd()
        if tag == "-ly":
            sonPath = str(filePath) + "/" + fileName
            if os.path.exists(sonPath):
                print("rmf Removing directory: ", fileName)
                os.remove(sonPath)
            else:
                print("rmf: ", Messages_Declear.DirectoryNotFound)
        else:
            sonPath = str(filePath) + "/" + tag + "/" + self.filename
            if os.path.exists(sonPath):
                print("rmf: Deleting ",fileName)
                os.remove(sonPath)
            else:
                print("rmf: ",Messages_Declear.CanNotFindFile)
class rmf:
    def __init__(self,Name,tag: str | None = ..., flag: str | None = ...):
        strictRemove(Name, tag=tag)

def rmf_info():
    print("rmf: remove files or layers")
    print("Command Syntax: rmf [file name] [file tag] [flag]")
    print("[file name]: name of the file, with extension name or layer name")
    print("[file tag]: tag of the file: tpa, tpb, tpc, others, scripts")
    print("[flag]: -s: strict mode, used to remove layers")