from exc import *
from rmf import * 
from show import *
from layer import *
from mdoc import *
from rt import *
from scrte import *
from info import * 
from EasterEgg import *
from power import *
from get import *
import os, sys
from run import *
from mkly import *
from view import *
from Messages_Declear import *
from adpsd import *
from installer import *
from logout import *
from debug import *
from fder import *
from multiprocessing import *
import gnureadline

def rms(*arg, **kwarg):
    os.system("clear")

def kill_self(*arg, **kwarg):
    sys.exit()

class commands:
    def split(commands: str):
        global header,target,flag
        splitted = commands.split()
        if len(splitted) == 2:
            header = splitted[0]
            target = splitted[1]
            flag = None
        elif len(splitted) == 1:
            header = commands
            target = None
            flag = None
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
    if target == None:
        thread = Process(target=commands.exec, args=(header),name=header)
    if flag == None: 
        thread = Process(target=commands.exec, args=(header,target),name=header)
    else:
        thread = Process(target=commands.exec, args=(header,target,flag),name=header)
    thread.start()
    thread.join()

#Boot Entry
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
    print("Shell System Alert: BeaconOS encountered a fatal error which need reboot...")
    print("Look up following Exit Code or use `fder` tool to display full messages.")
    os.system("reboot")