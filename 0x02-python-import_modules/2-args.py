#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argvs = sys.argv[1:]
    argc = len(argvs)
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(argc))

        for i, arg in enumerate(argvs, start=1):
            print("{}: {}".format(i, arg))
