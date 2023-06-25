import string
import os

k = 0
listF = []

def fdir(dir):
    global k
    global listF
    names = os.listdir(dir)
    for name in names:
        if(name == "index.js"):
            continue
        # print(f"file: {name}")
        f = os.path.join(dir, name)
        if os.path.isfile(f):
            print(f) 
            dot = name.find(".") + 1
            ext = name[dot:] 
            if ext == "js":
                listF.append(f) # [k] = f
                k = k + 1
        if os.path.isdir(f):
            fdir(f)

def getList():
    cwd = os.getcwd()
    d = os.path.join(cwd, "data")
    dir = os.path.join(d, "txt")  # /data/txt
    print(f"getcwd: {dir}")
    fdir(dir) 
    return listF  