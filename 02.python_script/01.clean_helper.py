import os
import sys
import time


def main(input_day):
    path_list = os.listdir('./')

    get_present_time = time.time()

    for i in path_list:
        file_path = './' + i
        get_file_time = os.stat(file_path).st_mtime

        time_gap = time.ctime(get_present_time - get_file_time).split()

        day = time_gap[2]
        month = time_gap[1]
        year = time_gap[-1]
        if (day > input_day) or (month != 'Jan') or (year != '1970') and (i != sys.argv[0].split('\\')[-1]):
            try:
                print('正在删除文件：', i)
                os.remove(file_path)
            except PermissionError:
                continue
        else:
            continue

if __name__ == '__main__':
    background = '''This is a clean script for Maccor data files, but it can also clean your own files.
                                --wrote at 03/24/2018,made with love for EE lab'''
    print(background)
    # 获取当前运行脚本本身路径
    a = sys.argv[0]
    #print(a.split('\\')[-1])
    while True:
        input_info = input('你需要清理几天前的文件?回车后确定: ')
        if input_info.isdigit():
            main(input_info)
            print('清理完成')
            break
        else:
            print('输入有误,重新输入，或Ctrl+C直接退出')
            input_day = input('你需要清理几天前的文件?回车后确定: ')


