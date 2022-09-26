import Messages_Declear as Messages_Declear
import os
python_script = ["py"]
shell_command = ["sh"]
class scrte:
    def __init__(self,fileName, flag: str | None = ...):
        fileType = os.path.splitext(fileName)[1]
        if fileType == ".py":
            fatherPath = os.getcwd()
            sonPath = str(fatherPath) + "/scripts" + "/" + fileName
            pythonFile = open(sonPath,'w')
            while True:
                try:
                    userEnter = str(input("/s-p/ "))
                    pythonFile.write(userEnter)
                    pythonFile.write('\n')
                except EOFError:
                    print('\n')
                    break
        elif fileType == ".sh":
            fatherPath = os.getcwd()
            sonPath = str(fatherPath) + "/scripts" + "/" + fileName
            shellFile = open(sonPath,'w')
            while True:
                try:
                    userEnter = str(input("/s-s/ "))
                    shellFile.write(userEnter)
                    shellFile.write('\n')
                except EOFError:
                    print('\n')
                    break
        elif fileType == ".beval":
            fatherPath = os.getcwd()
            sonPath = str(fatherPath) + "/EvalScript" + "/" + fileName
            shellFile = open(sonPath,'w')
            while True:
                try:
                    userEnter = str(input("/s-e/ "))
                    shellFile.write(userEnter)
                    shellFile.write('\n')
                except EOFError:
                    break
        else:
            print("scrt_e:", Messages_Declear.FileTypeNotSupported)

def scrte_info():
    print("scrte: create a script file under layer: scripts")
    print("Command Syntax: scrte [file name]")
    print("[file name]: name of the file, with extension name")