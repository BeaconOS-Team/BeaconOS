import Messages_Declear
from threading import Thread
from pathlib import Path
signatures = [ ]
class signatureCheck:
    def __init__(self,target, flag: str | None = ...):
        path = Path(target)
        indecator = open(path,'r')
        motherSig = open(Path("Signatures.txt").absolute(),'r')
        for motherSig.readlines in motherSig:
            signatures.append(motherSig.readlines)
        for indecator.readlines in indecator:
            if signatures.index(indecator.readlines):
                pass
            else:
                print(Messages_Declear.SignatureVeriFail)
class instalation:
    def __init__(self, flag: str | None = ...):
        global installThread,sigCheckThread
        sigCheckThread = Thread(target=signatureCheck,name="Signature Check",daemon=True)
        installThread = Thread(target=instalation,name="Installation",daemon=False)
    def run():
        if sigCheckThread.start:
            if installThread.start:
                pass
            else:
                print(Messages_Declear.InstallationFailed)
        else:
            print(Messages_Declear.InstallationFailed)
