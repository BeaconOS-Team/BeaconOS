import sys
import Messages_Declear as md
import os
class power:
    def __init__(self,statement: str, timePower: int, flag: str | None = ...) -> None:
        power.pwadm(statement=statement, timePower=timePower,flag=flag)
        os.remove("__pycache__")
    def pwadm(statement:str,timePower:int, flag: str | None = ...):
        if statement == ("-s"):
            if int(timePower) < 0:
                print("poweradm:",md.InvalidInput)
            else:
                if timePower == 0:
                    os.system("poweroff")
                else:
                    import time
                    time.sleep(float(timePower))
                    os.system("poweroff")
        elif statement == ("-r"):
            if int(timePower) < 0:
                print("power:",md.InvalidInput)
            else:
                if int(timePower) == 0:
                    os.system("reboot")
                else:
                    import time
                    time.sleep(float(timePower))
                    os.system("reboot")
        else:
            print("power:",md.IllegalOperation)  

def power_info():
    print("power: operate the power of the machine")
    print("Command Syntax: power [option] [time]")
    print("[option]: -F: power off; -lr: full reboot")
    print("[time]: time before the operation, during this time, all other threads will be stoped.")