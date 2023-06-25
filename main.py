

from gtts import gTTS
from get_files_js import *
from get_texts_from_js import *
from form_mp3 import *




if __name__ == '__main__':
    listFilesJs = getList()
    for i in range(0, len(listFilesJs)):
        mp(listFilesJs[i])
