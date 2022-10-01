from pathlib import Path
import json
from os.path import exists
import Messages_Declear

class configure_path:
    def init(file_name: str | None = "Errors.json") -> str | bool:
        configured_path = str(Path("data").absolute()) + "/" +file_name
        if exists(configured_path):
            return configured_path
        else:
            print("fder:", Messages_Declear.DirectoryNotFound)
            return False

class load_js:
    def init(path: str | bytes | None = ...) -> dict | bool:
        if exists(path):
            with open(path, 'r') as js:
                error_data = json.load(js)
            return error_data
        else:
            return False

    def verify(result) -> bool:
        if not type(result) == dict | list:
            return False
        else:
            return True

class search:
    def configure_path_func() -> bool | bytes:
        path = configure_path.init()
        if path:
            return path
        else:
            return False
    
    def search(object: str | None = ...) -> bool:
        if search.configure_path_func():
            js_dict = load_js.init(search.configure_path_func())
            if js_dict[object]:
                print("Error Archives:",'\n',f"  Error Index: {object}",'\n',f"  Details: {js_dict[object]}")
            else:
                print("fder:", Messages_Declear.CannotFindTarget)
        else:
            print("fder:", Messages_Declear.DirectoryNotFound)
            return False

def fder(object: str | int | None = ..., flag: str | None = ...):
    search.search(object=object)

def fder_info():
    print("fder: Find error code and display detail information within BeaconOS Error Archives")
    print("Syntax: fder [error code]")
    print("[error code]: The hexadecimal number set within '||' after an error message")