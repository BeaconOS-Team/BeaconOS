from pathlib import Path
import os, Messages_Declear

class out:
    def construct(path: str | None  = ...) -> str | bool:
        if os.path.exists(path):
            return path
        else:
            return False
    
    def read(path: str | None = ...) -> None:
        with open(path,'r') as file:
            for x in file:
                print(x)

    def init(path: str | None = ...) -> None:
        try:
            if out.construct(path=path):
                out.read(out.construct(path=path))
            else:
                print("exc: ",Messages_Declear.CanNotFindFile)
        except Exception as e:
            print("exc:",Messages_Declear.ErrorInFile, e)

class construct:
    def make(file_name: str, tag: str) -> str | bool:
        path = str(Path(tag).absolute()) + "/" + file_name
        if os.path.exists(path):
            return path
        else:
            return False
    
    def verify(path: str, file_name: str) -> bool | str:
        extension_name = Path(file_name).suffix
        if extension_name == ".py":
            with open(path,'r') as python:
                for x in python:
                    exec(x)
        else:
            out.init(path=path)

def exc(filename: str, tag: str):
    if construct.make(file_name=filename,tag=tag):
        construct.verify(construct.make(file_name=filename,tag=tag),file_name=filename)
    else:
        print("exc:", Messages_Declear.CanNotFindFile)