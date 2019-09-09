import sys
from termcolor import colored

def warn(msg, sameline=False):
    log(msg, 2, sameline)

def error(msg, sameline=False):
    log(msg, 3, sameline)

def debug(msg, sameline=False):
    log(msg, 4, sameline)

def success(msg, sameline=False):
    log(msg, 1, sameline)

def print(msg, sameline=False):
    log(msg, 0, sameline)

def log(msg, msgType, sameline=False, color=None):

    if (isinstance(msg, int)):
        msg = str(msg)

    if msgType == 1:
        msg = colored("[+] ", 'green') + msg
    elif msgType == 2:
        msg = colored("[-] ", 'yellow') + msg
    elif msgType == 3:
        msg = colored("[!] ", 'red') + msg
    elif msgType == 4:
        msg = colored("[DBG] ", 'blue') + msg

    if color:
        msg = colored(msg, color)
        
    try:
        if not sameline:
            sys.stdout.write('\r' + msg + '\r\n')
        else:
            sys.stdout.write(msg)
    except:
        if not sameline:
            sys.stdout.write(b'\r' + msg.encode() + b'\r\n')
        else:
            sys.stdout.write(msg.encode())
    try:
        sys.stdout.flush()
    except:
        # traceback.print_exc()
        pass
