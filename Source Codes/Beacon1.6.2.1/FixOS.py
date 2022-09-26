import os
class CanNotConnetError(Exception):
    def __init__(self):
        message = "Errors and Exceptions: Unable to Establish Connection to the Server"
        try:
            raise CanNotConnetError
        except CanNotConnetError:
            print(message)
class LocalTypeError(Exception):
    def __init__(self):
        message = "Errors and Exceptions: Input Type From User Does Not Meet the Expectations"
        try:
            raise LocalTypeError
        except LocalTypeError:
            print(message)
class fix:
    def __init__(self,inputType:str, flag: str | None = ...):
        try:
            if (inputType == "-l"):
                currentDir = os.getcwd()
                tarDir = str(currentDir) + "/OFT"
                os.chdir(tarDir)
                sonDir = tarDir + "Local_Fix.py"
                exec(open(sonDir).read())
        except:
            pass