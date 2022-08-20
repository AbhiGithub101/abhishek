import os


def file_create(filename,path=r'C:\Users\abhis\OneDrive\Desktop\flip'):
    if(os.path.exists(fr'{path}\{filename}.txt')==False):
        f = open(fr'{path}\{filename}.txt','x')
        return 1
    else:
        return 0

def file_read(filename,path):
    if(os.path.exists(fr'{path}\{filename}.txt')==True):
        f = open(fr'{path}\{filename}.txt', 'r')
        data = f.read()
        return data
    else:
        return 0

def file_overwrite(filename,path,message):
    if (os.path.exists(fr'{path}\{filename}.txt') == True):
        f = open(fr'{path}\{filename}.txt', 'w')
        f.write(message)
        return 1
    else:
        return 0

def file_append(filename,path,message):
    if (os.path.exists(fr'{path}\{filename}.txt') == True):
        f = open(fr'{path}\{filename}.txt', 'a')
        f.write(message)
        return 1
    else:
        return 0

def show_files(path):
    if (os.path.exists(fr'{path}') == True):
            return os.listdir(path)
    else:
        return 0
