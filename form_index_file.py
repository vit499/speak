import os


# import m0 from "./a/0.mp3";
# import m1 from "./a/1.mp3";
# import m2 from "./a/2.mp3";
# import m3 from "./a/3.mp3";
# import m4 from "./a/4.mp3";
# import m5 from "./a/5.mp3";

# const mp3 = [m0, m1, m2, m3, m4, m5];

# export default mp3;



def form_index_file(folder, len_list):
    s1 = ""
    for i in range(0, len_list):
        s1 += f"import m{i} from \"./{i}.mp3\";\n"
    s2 = "const mp3 = [\n"
    for i in range(0, len_list):
        s2 += f"  m{i},\n"
    s2 += "];\r\n"
    s2 += "export default mp3;\n"
    s = s1 + s2
    file = os.path.join(folder, "index.js")
    f = open(file, 'w')
    f.write(s)
    f.close()

    

