from pathlib import Path
import os
import Messages_Declear

class view:
    def __init__(self,filename,tag: str | None = "Beacon2.3.1") -> None:
        if view.tag(tag=tag):
            view.main(filename=filename)
        else:
            print("view: ", Messages_Declear.DirectoryNotFound)
    def tag(tag: str | None = "Docs") -> bool:
        global path
        path = str(Path(tag).absolute())
        if tag == "build_information" or tag == "passwords":
            print("view: Access denied")
            return False
        if os.path.exists(path):
            return True
        else:
            return False
    def main(filename: str | None = ...):
        Path = path + "/" + filename
        if os.path.exists(Path):
            with open(Path) as file_name:
                for x in file_name:
                    print(x)
        else:
            print("view: ", Messages_Declear.CanNotFindFile)
def view_info():
    print("view: Show contents of any files")
    print("Syntax: view [file name] [tag]")