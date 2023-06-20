
import string
from gtts import gTTS
import os



def xx():
  print(f"abcd")
  tts = gTTS(text='Good morning', lang='en')
  tts.save("good.mp3")
  # os.system(f"{player} good.mp3")

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
            print(f"ext= {ext}")
            if ext == "js":
                listF.append(f) # [k] = f
                k = k + 1
        if os.path.isdir(f):
            fdir(f)

def getList():
    cwd = os.getcwd()
    d = os.path.join(cwd, "txt")
    dir = os.path.join(d, "txt")
    print(f"getcwd: {dir}")
    fdir(dir)   

def getStr(file):
    list = []
    print(f"file: {file}")
    f = open(file, 'r', encoding='utf-8')
    str2 = f.read()
    
    # i = str.find("[") + 1
    # str2 = str[i:]

    s1 = 0
    s2 = 0
    s = False
    
    k = 0
    for i in range(0, len(str2)):
        if(s == True):
            if(str2[i] == '"'):
                s2 = i
                if k % 2 == 0:
                    list.append(str2[s1:s2])
                k = k + 1
                s = False
        else:
            if(str2[i] == '"'):
                s1 = i + 1
                s = True
    return(list)
 
def getMp(file, str, ind):
    i = 0
    
    dot = file.find(".")
    file = file[0:dot]
    f1 = os.path.join(os.getcwd(), "audio")
    try:
        os.mkdir(f1)
    except:
        pass
    f2 = os.path.join(f1, file)
    try:
        os.mkdir(f2)
    except:
        pass
    n = f"{ind}.mp3"
    f = os.path.join(f2, n)
    print(f"n={f}")

    tts = gTTS(str, lang='ru')
    tts.save(f)

def mp(file):
    strs = getStr(file)
    for i in range(0, len(strs)):
        getMp(file, strs[i], i)

if __name__ == '__main__':
    getList()
    # list = getStr(listF[0])
    mp(listF[0])
