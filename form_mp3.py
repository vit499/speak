
import string
from gtts import gTTS
import os
from get_texts_from_js import *
from form_index_file import *


def get_folder(file):
    # file = D:\work\bc\python\speak\data\txt\sunshine\s10.js
    dot = file.find(".")
    f = file[0:dot]
    print(f"folder={f}")
    try:
        os.mkdir(f)
    except:
        pass
    return(f)

def form_name_mp3_file(folder, ind):
    n = f"{ind}.mp3"
    f = os.path.join(folder, n)
    print(f"n={f}")   # f= D:\work\bc\python\speak\data\txt\sunshine\s10\0.mp3
    return(f)

def get_list_names_files_mp3(file, len_strs):
    list = []
    for i in range(0, len_strs):
        f = form_name_mp3_file(file, i)  
        list.append(f) 
    return list

def form_mp3_file(file, str):
    try:
        tts = gTTS(str, lang='ru')
        tts.save(file)
    except:
        pass


# form folder with mp3 files from one js-file
def mp(file):
    folder = get_folder(file)
    strs = getTexts(file)            # list of texts for audio from one js-file
    list_names_files_mp3 = get_list_names_files_mp3(folder, len(strs))  # [ 0.mp3, 1.mp3, ]
    form_index_file(folder, len(strs))
    for i in range(0, len(strs)):
        form_mp3_file(list_names_files_mp3[i], strs[i])

