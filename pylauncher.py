#!/usr/bin/python3

import sys
import os
from ctypes import *

def main():
    if len(sys.argv) < 2:
        return -1
    if len(sys.argv) >= 4:
        entry = sys.argv[3]
    else: entry = "main"
    try:
        lib = cdll.LoadLibrary(sys.argv[1])
    except OSError as e:
        lib = cdll.LoadLibrary("/Users/KellyNicholasI/Library/Python/3.9/bin/" + sys.argv[1])
    entry = getattr(lib, entry)
    argv = [  ]
    i = 0
    for s in sys.argv:
        if i != 0:
            argv.append(s.encode("utf-8"))
        i += 1
    argvptr = (c_char_p * len(sys.argv))(*argv)

    os.environ["PWD"] = os.getcwd()

    return entry(len(argv), argvptr)

sys.exit(main())
