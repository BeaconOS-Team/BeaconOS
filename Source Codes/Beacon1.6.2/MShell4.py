from importlib import reload
import datetime
import threading
from debug import debug
from MShell_Support import *
import MShell_Support as ms
from Shell_Prerequ import pre
import Messages_Declear
from adcmd import REFRESH

class cmd:
    def split(input: str | None = ...) -> list:
        repsitory = [ ]
        for x in input.split():
            repsitory.append(x)
        return repsitory
    
    def length(source: list | None = ...) -> int | bool:
        if not len(source) < 1:
            return len(source)
        else:
            return False
    
    def exec(length: int | None = 1, source: list | None = ...) -> None:
        try:
            if length == 1:
                globals()[source[0]]()
            else:
                globals()[source[0]](*source[1:])
        except REFRESH:
            reload(ms)
        except KeyError:
            print("Shell Child Thread Error:",source[0],Messages_Declear.CanNotFindCommand)
    
def run(source: list | None = ..., name: str | None = "Thread") -> None:
    process = threading.Thread(target=cmd.exec, args=(cmd.length(source=source), source), name=name)
    process.start()
    process.join()

class interface:
    def io() -> str:
        inputs = input(">>> ")
        if inputs == "debug":
            debug()
        else: 
            return inputs
    
    def main():
        inputs = interface.io()
        run(source=cmd.split(input=inputs), name=cmd.split(input=inputs)[0])
pre()
print(f"Login time {datetime.datetime.now()}")
while __name__ == '__main__':
    try:
        interface.main()
    except KeyboardInterrupt or EOFError:
        print('\n')
    except Exception as e:
        print("Interpreter Error: ", e, "@shell")