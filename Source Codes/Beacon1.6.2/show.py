import os
from layer import Desktop
import Messages_Declear as Messages_Declear
dekstop = ["/Desktop","/desktop"]
documents = ["/Docs", "/docs"]
def show(directory, tag, flag: str | None = ...):
    try:
        if directory in dekstop:
            print(Desktop)
        elif directory in documents:
            fpath = os.getcwd()
            sonPath = str(fpath) + "/" + tag
            files = os.listdir(sonPath)
            print("show: Under",tag,"BeaconOS found: ",' '.join(files))
        else:
            print("show:", Messages_Declear.DirectoryNotFound)
    except FileNotFoundError:
        print("show:",Messages_Declear.CanNotFindFile)

def show_info():
    print("show: show all files under a layer")
    print("Command Syntax: show [layer name]")