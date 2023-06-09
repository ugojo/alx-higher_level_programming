#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argvs = sys.argv[1:]
    argc = len(argvs)
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))
    for i, arg in enumerate(argvs, start=1):
            print("{}: {}".format(i, arg))
