'''
What is compiler.py? 
BeaconOS's software execution is conducted via python3 module, in addtion, the executable file can only be .pyc in order to publish
on BeaconOS's server, this file or tool is used to help developers compile there .py to .pyc. 
'''
import py_compile, sys

class compile:
    def __init__(self, *arg, **kwarg) -> None:
        compile.compile(*arg, **kwarg)

    def compile(*arg, **kwarg):
        try:
            py_compile.compile(*arg, *kwarg)
        except Exception as e:
            print("Compiler py_compile Error: ", e)

if __name__ == '__main__':
    compile(' '.join(sys.argv[1:]))