import os
import sys

from task9 import *


def main(args):
    cwd = Directory(os.getcwd())
    while True:
        cmdtokens = input('{path}$ '.format(path=cwd.path)).split()
        if not cmdtokens:
            continue
        cmd = cmdtokens[0]
        cmdargs = cmdtokens[1:]

        if cmd == 'ls':
            print()
            path = cwd.path if not cmdargs else cmdargs[0]
            directory = cwd.getsubdirectory(path)
            for item in directory.items():
                if item.isfile():
                    print('{name}\tFILE\t{size}'.
                          format(name=item.getname(), size=len(item)))
                else:
                    print('{name}\tDIR'.format(name=item.getname()))
            print()
        elif cmd == 'cd':
            print()

            new_dir = cmdargs[0]
            if FSItem(new_dir).exists() and FSItem(new_dir).isdirectory():
                os.chdir(new_dir)
                cwd = Directory(os.getcwd())
            else:
                print("Directory doesn't exist")

        elif cmd == 'cat':
            if not cmdargs:
                print("Arguments for the command are needed")
            else:
                for file in cmdargs:
                    if FSItem(file).exists() and FSItem(file).isfile():
                        for i in File(file).getcontent():
                            print(i[:-1] if i[-1] == '\n' else i)
                    else:
                        print('There is no file {file}'.
                              format(file=FSItem(file).getname()))

        elif cmd == 'head':
            if not cmdargs:
                print("Arguments for the command are needed")
            else:
                for file in cmdargs:
                    if FSItem(file).exists() and FSItem(file).isfile():
                        for i in File(file).getcontent()[:10]:
                            print(i[:-1] if i[-1] == '\n' else i)
                    else:
                        print('There is no file {file}'.
                              format(file=FSItem(file).getname()))

        elif cmd == 'tail':
            if not cmdargs:
                print("Arguments for the command are needed")
            else:
                for file in cmdargs:
                    if FSItem(file).exists() and FSItem(file).isfile():
                        for i in File(file).getcontent()[-10:]:
                            print(i[:-1] if i[-1] == '\n' else i)
                    else:
                        print("There is no file {file}".
                              format(file=FSItem(file).getname()))

        elif cmd == 'pwd':
            print(os.path.abspath('.'))

        elif cmd == 'touch':
            if not cmdargs:
                print("Arguments for the command are needed")
            else:
                for file in cmdargs:
                    if FSItem(file).exists() and FSItem(file).isfile():
                        print("File {file} already exist".
                              format(file=FSItem(file).getname()))
                    elif FSItem(file).isdirectory():
                        print("{file} is directory".
                              format(file=FSItem(file).getname()))
                    else:
                        File(file).create()

        elif cmd == 'find':
            if not cmdargs:
                print("Arguments for the command are needed")
            else:
                for name in cmdargs:
                    files = cwd.filesrecursive()
                    for f in files:
                        if f.getname() == name:
                            print(f.path)
            pass
        elif cmd == 'exit':
            print("Bye bye!")
            break
        else:
            print('Unknown command: {cmd}'.format(cmd=cmd))


if __name__ == '__main__':
    main(sys.argv)
