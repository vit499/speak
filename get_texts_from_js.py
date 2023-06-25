

def getTexts(file):
    list = []
    print(f"file: {file}")
    f = open(file, 'r', encoding='utf-8')
    str2 = f.read()

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

    