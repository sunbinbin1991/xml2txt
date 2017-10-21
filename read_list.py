#read list and show all list
import cv2
import os


def read_list(path_in):
    # read list and show recangle in picture
    with open(path_in) as fin:
        while True:
            line = fin.readline()
            if not line:
                break
            line = [i.strip() for i in line.strip().split()]
            line_len = len(line)
            print line,line_len
            img = cv2.imread(working_dir+line[-1])
            print working_dir+line[-1]
            h,w = img.shape[0],img.shape[1]
            newimg= img.copy()
            for  i in range(int(line_len/6)):
                print len(line),float(line[3+6*i+1]),line[-1]
                print len(line),float(line[3+6*i+1]),line[-1]
                print w,h
                x1 = int(w * float(line[3+6*i+1]))
                y1 = int(h * float(line[3+6*i+2]))
                x2 = int(w * float(line[3+6*i+3]))
                y2 = int(h * float(line[3+6*i+4]))
                print working_dir+line[-1],x1,x2,y1,y2
                cv2.rectangle(newimg,(x1,y1),(x2,y2),(0,255,255),3)
                continue
            cv2.imshow("img",newimg)
            cv2.waitKey(0)


def save_list(path_in,pathout):
    img_num = 4732
    with open(path_in) as fin:
        while True:
            line = fin.readline()
            if not line:
                break
            line = [i.strip() for i in line.strip().split('\t')]
            line_len = len(line)
            img = cv2.imread(working_dir+line[-1])
            print working_dir+line[-1]
            h,w = img.shape[0],img.shape[1]
            name = line[-1]
            has_person = False
            # pathout.write(str(img_num)+'\t'+'2'+'\t'+'6'+'\t')
            for  i in range(int(line_len/6)):
                label = line[3+6*i]
                if label==str('%.4f'% (14)):# represent person
                    pathout.write(str(img_num)+'\t'+'2'+'\t'+'6'+'\t')
                    img_num+=1
                    has_person = True
                    break
            for  i in range(int(line_len/6)):
                label = line[3+6*i]
                if label==str('%.4f'% (14)):# represent person
                    x1 = str(float(line[3+6*i+1]))
                    y1 = str(float(line[3+6*i+2]))
                    x2 = str(float(line[3+6*i+3]))
                    y2 = str(float(line[3+6*i+4]))
                    pathout.write(str('%.4f'% (0))+'\t'+x1+'\t'+y1+'\t'+x2+'\t'+y2+'\t'+str(float(0))+'\t')
                    print label
            if has_person:
                pathout.write('VOCdevkit/'+name+"\n")
    path_out.close()
            # print working_dir+line[-1],x1,x2,y1,y2
            #     cv2.rectangle(newimg,(x1,y1),(x2,y2),(0,255,255),1)
            # cv2.imshow("img",newimg)
            # cv2.waitKey(0)


if __name__ == '__main__':
    # print "ss"
    # working_dir = "D:\data\pedestrain_video\cvpr10_multiview_pedestrians/"
    working_dir ="../data/VOCdevkit/"
    # list_dir = "path_out.txt"
    # list_dir = "pds_test2.txt"
    list_dir = "../train.lst"
    # read_list(list_dir)
    path_out = open('path_out.lst','w')
    save_list(list_dir,path_out)

