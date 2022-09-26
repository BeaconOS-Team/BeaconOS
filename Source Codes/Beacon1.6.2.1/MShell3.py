from importlib import reload
import os,datetime
from Messages_Declear import *
import MShell_Support
from debug import *
from multiprocessing import *
from MShell_Support import *
import gnureadline

def rms(*arg, **kwarg):
    os.system("clear")

class commands:
    def split(commands: str):
        global header,target,flag
        splitted = commands.split()
        if len(splitted) == 2:
            header = splitted[0]
            target = splitted[1]
            flag = False
        elif len(splitted) == 1:
            header = commands
            target = False
            flag = False
        elif len(splitted) == 3:
            header = splitted[0]
            target = splitted[1]
            flag = splitted[2]
        else:
            print("Shell Main Process Error: ",UnexceptedLenght)
    
    def exec(header: str, target: str | None = ..., flag: str | None = ...):
        try:
            if flag == None: 
                globals()[header](target)
            else:
                globals()[header](target,flag)
        except KeyError:
            print(f"Shell Child Process Error: {header}{CanNotFindCommand}")
        except Exception as e:
            print("Shell Child Process Error: ", e)

def main():
    global thread
    commandInput = str(input(">>> "))
    if commandInput == "debug":
        debug()
    commands.split(commandInput)
    if target:
        thread = Process(target=commands.exec, args=(header),name=header)
    if flag: 
        thread = Process(target=commands.exec, args=(header,target),name=header)
    else:
        thread = Process(target=commands.exec, args=(header,target,flag),name=header)
    if refresh():
        reload(MShell_Support)
    thread.start()
    thread.join()

rms()
current_dir = os.getcwd()
path = current_dir + "/Shell_Prerequ.py"
with open(path) as shell_pre:
    exec(shell_pre.read())
    time = datetime.datetime.now()
    path = current_dir + "/build_information/current.binf"
    file = open(path)
    contents = file.readlines()
    print(f"BeaconOS version {contents[0]}")
    print(f"Login Time: {time}", '\n')
    
if __name__ == "__main__":
    set_start_method('fork') 
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('\n')
        except Exception as e:
            print("Shell Main Process Error: ",e)
    os.system("python3 login_assets.py"); os.system("reboot")
else:
    os.system("reboot")