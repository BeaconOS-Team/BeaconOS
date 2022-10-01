'''
This script should be run before load in to MShell. this will make all dir and get all files if needed
'''
def pre():
    import os
    from os import system as cmd
    from pathlib import Path
    fatherPath = os.getcwd()
    sonPath1 = str(fatherPath) + "/tpa"
    sonPath2 = str(fatherPath) + "/tpb"
    sonPath3 = str(fatherPath) + "/tpc"
    sonPath4 = str(fatherPath) + "/others"
    sonPath5 = str(fatherPath) + "/scripts"
    sonPath6 = str(fatherPath) + "/Documentations"
    sonPath7 = str(fatherPath) + "/temp"
    if os.path.exists(sonPath1):
        pass
    else: 
        os.makedirs(sonPath1)

    if os.path.exists(sonPath2):
        pass
    else: 
        os.makedirs(sonPath2)

    if os.path.exists(sonPath3):
        pass
    else: 
        os.makedirs(sonPath3)

    if os.path.exists(sonPath4):
        pass
    else: 
        os.makedirs(sonPath4)

    if os.path.exists(sonPath5):
        pass
    else: 
        os.makedirs(sonPath5)

    if os.path.exists(sonPath6):
        pass
    else: 
        os.makedirs(sonPath6)

    if os.path.exists(sonPath7):
        pass
    else: 
        os.makedirs(sonPath7)

    try:
        cmd("python3 -m pip --version")
        cmd("clear")
    except OSError:
        print("Installer: Installing pip....")
        command = "python3" + str(Path("pkg").absolute()) + "/pip-22.2.2/setup.py install"
        cmd(command)
    try:
        import gnureadline
    except:
        print("Installer: Installing dependent package `gnureadline`")
        architecture = os.uname()
        command = str(Path("pkg").absolute()) + "/pkg_whl/gnureadline-8.1.2-cp310-cp310-" + architecture + ".whl" + " maskpass-0.3.6-py3-none-any.whl"
        cmd(command)
