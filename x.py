


    # file = D:\work\bc\python\speak\data\txt\sunshine\s10.js
    # dir_start = D:\work\bc\python\speak\data\
    # dir_end = txt\sunshine\s10.js -> audio\sunshine\s10
    # dst = D:\work\bc\python\speak\data\audio\sunshine\s10
    # s1 = file.find("data") + 5
    # dir_start = file[0:s1]
    # print(f"dir_start={dir_start}")
    # s2 = file.find("txt") + 3
    # s3 = file.find(".")
    # dir_end = file[s2:s3]
    # print(f"dir_end={dir_end}")
    
    # f1 = os.path.join(dir_start, "audio")
    # print(f"f1={f1}")
    # try:
    #     os.mkdir(f1)
    # except:
    #     pass
    # f2 = os.path.join(f1, dir_end)
    # print(f"f1={f2}")
    # try:
    #     os.mkdir(f2)
    # except:
    #     pass
    # # f1 = os.path.join(os.getcwd(), "audio")
    # # print(f"f1={f1}")
    # # try:
    # #     os.mkdir(f1)
    # # except:
    # #     pass
