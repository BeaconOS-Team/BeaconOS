from pathlib import Path
import os, Messages_Declear as Messages_Declear
python_file = ["py"]
text_file = ["txt"]
shell_cmd = ["sh"]
def read(path):
    index = open(path, 'r')
    lines = index.readlines
    for lines in index:
        print(lines)
def exc(fileName,tag, flag: str | None = ...):
    global target_file
    target_file = fileName
    fpath = os.getcwd()
    global new_path 
    file_type = os.path.splitext(target_file)[-1][1:]
    try:
        if file_type in python_file:
            global get_path
            get_path = str(fpath) + "/scripts" + "/" + fileName
            print("exc: File Executing:", get_path)
            exec(open(get_path).read())
        elif file_type in text_file:
            if (tag == "tpa"):
                get_path = str(fpath) + "/tpa" + "/" + fileName
                read(get_path)
            elif (tag == "tpb"):
                get_path = str(fpath) + "/tpb" + "/" + fileName
                read(get_path)
            elif (tag == "tpc"):
                get_path = str(fpath) + "/tpc" + "/" + fileName
                read(get_path)
            else:
                get_path = str(fpath) + "/others" + "/" + fileName
                read(get_path)
        elif file_type in shell_cmd:
            get_path = str(fpath) + "/scripts" + "/" + fileName
            command = "chmod u+X " + get_path + " && sh " + get_path
            print("exc: File Executing: ",get_path)
            os.system(command)
        elif file_type == ("sfw"):
            get_path = str(fpath) + "/Applications" + "/" + fileName
            print("exc: Opening Application:", get_path)
            exec(open(get_path).read())
        else:
            print("exc:", Messages_Declear.UnexecutableFile)
    except FileNotFoundError:
            print("exc:", Messages_Declear.CanNotFindFile)
    except:
        print("exc:", Messages_Declear.ErrorInFile)   
    
def exc_info():
    print("exc: Run a file")
    print("Command Syntax: exc [file name] [file tag]")
    print("[file name]: name of the file with its extension name. Including: .py, .sh, etc...")
    print("[file tag]: tag of the file: tpa, tpb, tpc, scripts, others")

