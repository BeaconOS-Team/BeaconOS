from pathlib import Path
from os import system, path as exist
import Messages_Declear

class run:
    def type_verifier(filename: str | None = ...) -> bool:
        if filename[-4:] == ".pyc":
            return True
        else:
            return False

    def path_verifier(filename: str | None = ...) -> str | bool:
        path = str(Path("Applications").absolute()) + "/" + filename
        if exist.exists(path=path):
            return path
        else:
            return False
    
    def __init__(self, filename: str | None,  *arg, **kwarg) -> None:
        if run.type_verifier(filename=filename) and type(run.path_verifier(filename=filename)) is str:
            cmd = "python3" + run.path_verifier(filename=filename)
            system(cmd)
        else:
            print("run: ", Messages_Declear.CanNotFindFile)

def run_info():
    print("run: execute softwares provided by developers")
    print("Syntax: run [file name: .pyc file]")