import Messages_Declear
from pathlib import *
import os

class REFRESH(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class install:
    def check_type(filename: str | None = ...) -> bool:
        if filename[-1][1:] == "pyc":
            return True
        else:
            return False

    def check_exists(pkg_name: str | None = ...) -> bool:
        path = os.getcwd() + pkg_name
        if os.path.exists(path=path):
            return True
        else:
            print("adcmd: ",Messages_Declear.CannotFindTarget)
            return False
    
    def install(name: str | None = ...) -> None | bool:
        try:
            with open(Path("MShell_Support.py").absolute(), 'w') as file:
                contents = f"from {name} import *"
                file.write(contents)
        except:
            return False
        else:
            return True
        finally:
            install.refresh()

    def refresh(target: str | None = ..., flag: str | None = ...) -> bool:
        raise REFRESH