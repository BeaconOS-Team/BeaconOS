from maskpass import askpass
from pathlib import Path
import sys
import Messages_Declear as msg
class password:
    def check(password: str | None = False) -> bool:
        if password:
            path = str(Path("passwords").absolute()) + "/passwords.bpass"
            with open(path) as file:
                for x in file:
                    if x == password:
                        return True
                else:
                    return False
        else:
            print("debug",msg.PasswordIncorrect)
            return False
    def main() -> bool:
        for x in range(3):
            usr_password = askpass(prompt="Enter Password: ", mask="*")
            if password.check(password=usr_password):
                return True
            else:
                print("debug: ",msg.PasswordIncorrect)
        else:
            print("debug: Too many false attemps")
            return False
class debug:
    def __init__(self, target: str | None = ..., flag: str | None = ...) -> None:
        if password.main():
            print("debug: Starting Debug Session...")
            sys.exit()
