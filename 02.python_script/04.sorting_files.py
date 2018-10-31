import os
import shutil

path = './problem2_files'
os.makedirs(path + './image')
os.makedirs(path + './document')

image_suffix = ['jpg', 'png', 'gif']
doc_suffix = ['doc', 'docx', 'ppt', md]

for i in image_suffix:
    cur_path = path +'/'+i
    files = os.listdir(cur_path)
    for f in files:
        shutil.move(cur_path + '.' + f, path + '/image')

    os.removedirs(cur_path)

for d in doc_suffix:
    cur_path = path + '/' + d
    files = os.listdir(cur_path)
    for f in files:
        shutil.move(cur_path + '/' + f, path + '/document')
    os.removedirs(cur_path)

    

