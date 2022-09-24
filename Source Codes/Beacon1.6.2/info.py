from pathlib import *

class info:
    def __init__(self,pkg_name:str, flags: str | None = ...) -> None:
        info.get(pkg_name=pkg_name)
        info.run()

    def get(pkg_name: str) -> None:
        path = str(Path("temp").absolute()) + "/info_commands.txt"
        with open(path,'w') as temp:
            imports = "from " + pkg_name + " import *"
            func_name = pkg_name + "_info()"
            temp.write(imports)
            temp.write('\n')
            temp.write(func_name)
    
    def run():
        path = str(Path("temp").absolute()) + "/info_commands.txt"
        with open(path, 'r') as read:
            for x in read:
                exec(x)

def info_info():
    print("info: get a manual for a command")
    print("Command Syntax: info [command name]")
    print("[command name]: command that you want to read the manual")