import os
from PIL import Image

#<bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,<score>,<object_category>,<truncation>,<occlusion>
#/content/drive/Shareddrives/Dataset UAV/Iga/Tensorflow/VisDrone2019-DET-train


root_dir = "D:/codingan_serius/dataset/VisDrone2019-DET-train/"
annotations_dir = root_dir+"annotations/"
image_dir = root_dir + "images/"
xml_dir = root_dir+"annotations_xml_shifted/"
class_name = ['','ignored regions','pedestrian','people','bicycle','car','van','truck','tricycle','awning-tricycle','bus','motor','others']
file_yolo = "train.txt"
for filename in os.listdir(annotations_dir):
    fin = open(annotations_dir+filename, 'r')
    image_name = filename.split('.')[0]
    img = Image.open(image_dir+image_name+".jpg")
    xml_name = xml_dir+image_name+'.xml'
    with open(xml_name, 'w') as fout:
        fout.write('<annotation>'+'\n')

        fout.write('\t'+'<folder>VOC2007</folder>'+'\n')
        fout.write('\t'+'<filename>'+image_name+'.jpg'+'</filename>'+'\n')

        fout.write('\t'+'<source>'+'\n')
        fout.write('\t\t'+'<database>'+'VisDrone2018 Database'+'</database>'+'\n')
        fout.write('\t\t'+'<annotation>'+'VisDrone2018'+'</annotation>'+'\n')
        fout.write('\t\t'+'<image>'+'flickr'+'</image>'+'\n')
        fout.write('\t'+'</source>'+'\n')

        fout.write('\t'+'<size>'+'\n')
        fout.write('\t\t'+'<width>'+str(img.size[0])+'</width>'+'\n')
        fout.write('\t\t'+'<height>'+str(img.size[1])+'</height>'+'\n')
        fout.write('\t\t'+'<depth>'+'3'+'</depth>'+'\n')
        fout.write('\t'+'</size>'+'\n')

        fout.write('\t'+'<segmented>'+'0'+'</segmented>'+'\n')

        for line in fin.readlines():
            line = line.split(',')
            fout.write('\t'+'<object>'+'\n')
            fout.write('\t\t'+'<name>'+class_name[int(line[5])+1]+'</name>'+'\n')
            fout.write('\t\t'+'<pose>'+'Unspecified'+'</pose>'+'\n')
            fout.write('\t\t'+'<truncated>'+line[6]+'</truncated>'+'\n')
            fout.write('\t\t'+'<occluded>'+str(int(line[7]))+'</occluded>'+'\n')
            fout.write('\t\t'+'<bndbox>'+'\n')
            fout.write('\t\t\t'+'<xmin>'+line[0]+'</xmin>'+'\n')
            fout.write('\t\t\t'+'<ymin>'+line[1]+'</ymin>'+'\n')
            fout.write('\t\t\t'+'<xmax>'+str(int(line[0])+int(line[2]))+'</xmax>'+'\n')
            fout.write('\t\t\t'+'<ymax>'+str(int(line[1])+int(line[3]))+'</ymax>'+'\n')
            fout.write('\t\t'+'</bndbox>'+'\n')
            fout.write('\t'+'<difficult>'+'0'+'</difficult>'+'\n')
            fout.write('\t'+'</object>'+'\n')
        fin.close()
        fout.write('</annotation>')