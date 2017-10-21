import xmltodict
import json
import os
import cv2


img_num = 0
def list_files(root,myfile):
    # list all files in certain root
    fpath_d= [] #
    for path, dirs, files in os.walk(root, followlinks=True):
        dirs.sort()
        files.sort()
        print files,"ss"
        for fname in files:
            if fname.endswith('.xml'):
                XML2JSON(working_dir+fname,myfile)
    return fpath_d

def write_list(dir,file):
    #list all files in certain folder and save it as a "sysnet.txt" for perdict
    file.write(dir + '\n')
    fielnum = 0
    list = os.listdir(dir)
    print len(list)
    count = 0
    for line in list:
        filepath = os.path.join(dir,line)
        print line
        # count_t = str(count)
        if os.path.isdir(filepath):
            myfile.write(line +'\n')
        elif os.path:
            myfile.write(line +'\n')
            fielnum = fielnum + 1
        count += 1

def XML2JSON(fxml, myfile):
    global img_num
    if fxml is None:
        fxml = os.path.splitext(fxml)[0] + ".lst"
    xdict = xmltodict.parse(open(fxml))
    a = xdict['annotation']['object']
    print len(a)
    img_num +=len(a)
    return None

if __name__ == "__main__":
    myfile = open('headcount.lst','w')
    working_dir = "D:/biaotu\done\pede/30/"
    list_files(working_dir,myfile)
    print img_num
