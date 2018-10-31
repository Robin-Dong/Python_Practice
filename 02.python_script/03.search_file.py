import os,re

def fuzzy_search(path):
    word = input('please input what you want to search?')
    #print(os.listdir(path))
    for filename in os.listdir(path):
        re_filename = re.findall('.\w+',str(filename))
        if word in re_filename[0]:
            print(re_filename)

fuzzy_search('./')