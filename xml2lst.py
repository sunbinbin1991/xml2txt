import xmltodict
import json
import os
import cv2

img_num = 0
def list_files(root,myfile):
    # list all files in certain root
    print root
    fpath_d= [] #
    for path, dirs, files in os.walk(root, followlinks=True):
        dirs.sort()
        files.sort()
        print files,"ss"
        for fname in files:
            print fname
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
    # print xdict['annotationlist']['annotation'][0]['image']['name']
    label = str('%.4f'% (float(0)))
    print len(xdict['annotationlist']['annotation'])
    print xdict['annotationlist']['annotation'][0]['annorect']
    # print xdict['annotationlist']['annotation'][1]
    # print xdict['annotationlist']['annotation'][2]
    lenth = len(xdict['annotationlist']['annotation'])
    for i in range(lenth):
        # print xmlNum,type(xmlNum),
        # imagenum = xdict['annotationlist']['annotation'][i]['imgnum']
        name =xdict['annotationlist']['annotation'][i]['image']['name']
        imgPath = name
        img = cv2.imread(working_dir+imgPath)
        pic_h= img.shape[0]
        pic_w= img.shape[1]
        # print name,name.split('\\')[1].split('.')
        pos= xdict['annotationlist']['annotation'][i]['annorect']
        # print len(pos)
        if len(pos)>=7:
            # get position and width and height
            x1 = int(pos['x1'])
            y1 = int(pos['y1'])
            x2= int(pos['x2'])
            y2= int(pos['y2'])
            x1_ratio = str('%.4f'% (x1/float(pic_w)))
            y1_ratio = str('%.4f'% (y1/float(pic_h)))
            x2_ratio = str('%.4f'% (x2/float(pic_w)))
            y2_ratio = str('%.4f'% (y2/float(pic_h)))

            # h_ratio = str('%.4f'% (h/float(pic_h)))
            # w_ratio = str('%.4f'% (w/float(pic_w)))
            # print "ss",x1_ratio,x1,pic_w,x1/pic_w
            myfile.write(str(img_num)+'\t'+ '2'+'\t'+'6'+'\t'+label+'\t'+x1_ratio+'\t'+y1_ratio+'\t'+x2_ratio+'\t'+y2_ratio+'\t'+str(float(0))+'\t'+name+'\n')
            img_num +=1
        else:
            myfile.write(str(img_num)+'\t'+'2'+'\t'+'6'+'\t')
            for ii in range(len(pos)):
                x1 = int(pos[ii]['x1'])
                y1 = int(pos[ii]['y1'])
                x2= int(pos[ii]['x2'])
                y2= int(pos[ii]['y2'])
                x1_ratio = str('%.4f'% (x1/float(pic_w)))
                y1_ratio = str('%.4f'% (y1/float(pic_h)))
                x2_ratio = str('%.4f'% (x2/float(pic_w)))
                y2_ratio = str('%.4f'% (y2/float(pic_h)))
                myfile.write(label+'\t'+x1_ratio+'\t'+y1_ratio+'\t'+x2_ratio+'\t'+y2_ratio+'\t'+str(float(0))+'\t')
            myfile.write(name+"\n")
            img_num +=1
        i+=1
    return None

if __name__ == "__main__":

    myfile = open('pds_train.lst','w')
    working_dir = "D:\data\pedestrain_video\cvpr10_multiview_pedestrians/"
    list_files(working_dir,myfile)
