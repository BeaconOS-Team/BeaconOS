import os, Messages_Declear
class mkly:
    def __init__(self,name: str | None = ..., flag: str | None = ...) -> None:
        mkly.make(name=name)
    def make(name: str | None = "Unnamed Layer"):
        try:
            os.makedirs(name,exist_ok=False)
        except OSError:
            print("mkly: ",Messages_Declear.DirectoryExists)

def mkly_info():
    print("mkly: Make new layers")
    print("Syntax: mkly [directory name]")