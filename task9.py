import os


class FileSystemError(Exception):
    ''' Class for errors in filesystem module '''
    pass


class FSItem(object):
    ''' Common class for OS items OS: Files and Directories '''

    def __init__(self, path):
        ''' Creates new FSItem instance by given path to file '''
        self.path = path

    def rename(self, newname):
        ''' Renames current item
                raise FileSystemError if item does not exist
                raise FileSystemError if item "newname" already exists '''
        if not self.exists():
            raise FileSystemError("File {0} does not exist".
                                  format(self.getname()))
        elif self.getname() == newname:
            raise FileSystemError("Item {0} already exists".
                                  format(newname))
        else:
            os.rename(self.path, os.path.join(os.path.dirname(self.path),
                                              newname))
            self.path = os.path.join(os.path.dirname(self.path), newname)
            return "New path is " + self.path

    def create(self):
        ''' Creates new item in OS
                raise FileSystemError if item with such path already exists '''
        if not self.exists():
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
        else:
            raise FileSystemError("Item {0} with such path already exists".
                                  format(self.getname()))

    def getname(self):
        ''' Returns name of current item '''
        return os.path.basename(self.path)

    def isfile(self):
        ''' Returns True if current item exists and current item is file,
         False otherwise '''
        return self.exists() and os.path.isfile(self.path)

    def isdirectory(self):
        ''' Returns True if current item exists and current item is directory,
         False otherwise '''
        return self.exists() and os.path.isdir(self.path)

    def exists(self):
        ''' Returns True if current item exists, False otherwise '''
        return os.path.exists(self.path)


class File(FSItem):
    ''' Class for working with files '''

    def __init__(self, path):
        ''' Creates new File instance by given path to file
                raise FileSystemError if there exists directory
                 with the same path '''
        super(File, self).__init__(path)

    def __len__(self):
        ''' Returns size of file in bytes
                raise FileSystemError if file does not exist '''
        if not self.exists():
            raise FileSystemError("File {0} does not exist".
                                  format(self.getname()))
        else:
            return os.path.getsize(self.path)

    def create_file(self):
        self.create()
        open(self.path, "w")

    def getcontent(self):
        ''' Returns list of lines in file (without trailing end-of-line)
                raise FileSystemError if file does not exist '''
        if not self.exists():
            raise FileSystemError("File {0} does not exist".
                                  format(self.getname()))
        else:
            return open(self.path, 'r').read().split('\n')

    def __iter__(self):
        ''' Returns iterator for lines of this file
                raise FileSystemError if file does not exist '''
        if not self.exists():
            raise FileSystemError("File {0} does not exist".
                                  format(self.getname()))
        else:
            return iter(self.getcontent())


class Directory(FSItem):
    ''' Class for working with directories '''

    def __init__(self, path):
        ''' Creates new Directory instance by given path
                raise FileSystemError if there exists file
                with the same path '''
        super(Directory, self).__init__(path)

    def create_dir(self):
        self.create()
        os.mkdir(self.path)

    def items(self):
        ''' Yields FSItem instances of items inside of current directory
                raise FileSystemError if current directory does not exists '''
        if not self.exists():
            raise FileSystemError("File {0} does not exist".
                                  format(self.getname()))
        else:
            return os.listdir(self.path)

    def files(self):
        ''' Yields File instances of files inside of current directory
                raise FileSystemError if current directory does not exists '''
        if not self.exists():
            raise FileSystemError("File {0} does not exist".
                                  format(self.getname()))
        else:
            return [f for f in self.items() if
                    File(os.path.join(self.path, f)).isfile()]

    def subdirectories(self):
        ''' Yields Directory instances of directories inside of current directory
                raise FileSystemError if current directory does not exists '''
        if not self.exists():
            raise FileSystemError("File {0} does not exist".
                                  format(self.getname()))
        else:
            return next(os.walk(self.path))[1]

    def filesrecursive(self):
        ''' Yields File instances of files inside of this directory,
                inside of subdirectories of this directory and so on...
                raise FileSystemError if directory does not exist '''
        if not self.exists():
            raise FileSystemError("File {0} does not exist".
                                  format(self.getname()))
        else:
            return [x[2] for x in os.walk(self.path)]

    def getsubdirectory(self, name):
        ''' Returns Directory instance with subdirectory
                of current directory with name "name"
                raise FileSystemError if item "name"
                already exists and item "name" is not directory '''
        if not self.exists():
            raise FileSystemError("File {0} does not exist".
                                  format(self.getname()))
        elif name in self.items():
            if File(os.path.join(self.path, name)).isdirectory():
                return name
            else:
                raise FileSystemError("File {0} is not directory".
                                      format(name))
        else:
            raise FileSystemError("Subdirectory with name {0} does not exist".
                                  format(name))


if __name__ == '__main__':

    File("baz/te1.txt").create_file()
    File("baz/te2.txt").create_file()
    File("baz2/te3.txt").create_file()
    File("baz2/dir1/te4.txt").create_file()
    File("baz/dir1/te5.txt").create_file()
    File("baz/dir1/te6.txt").create_file()
    File("baz/dir1/dir3/te7.txt").create_file()
    File("baz/dir2/te8.txt").create_file()
    File("baz/dir2/dir5/te9.txt").create_file()
    Directory("baz3/dir1/dir3").create_dir()
    Directory("baz3/dir2/dir4").create_dir()
    Directory("baz3/dir2/dir5").create_dir()

    path1 = File("baz/dir1/te4.txt")

    with open(path1.path, 'w') as f:
        f.write('Hello!\n'+'How are you?\n'+'\n' +
                "Thanks, i'm fine.\n" + 'And you?')
    f.close()

    print(path1.__len__())
    print(path1.getcontent())
    print(path1.isfile(), path1.isdirectory(), path1.exists(), path1.getname())
    print(path1.rename("te44.txt"))

    path2 = Directory("baz")
    path2.rename("baz_new")
    print(path2.getname())
    print(path2.isdirectory(), path2.isfile(), path2.items(), path2.files())
    print(path2.subdirectories())
    print(path2.filesrecursive())
    print(path2.getsubdirectory("dir2"))
