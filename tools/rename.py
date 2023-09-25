import os
import shutil

import pofile
name="竹业"

def folder_rename():

    # 获取该目录下所有文件，存入列表中
    fileList = os.listdir(f"C:/Users/打工人/Downloads/{name}")
    print(fileList)
    n = 0
    for i in fileList:
        # 设置新文件名
        newname = 'a' + str(n + 1)
        n += 1
        # del_content:要替换的文件名，replace_content:替换后的文件名
        pofile.replace4filename(path=f'C:/Users/打工人/Downloads/{name}',
                                 del_content=i,
                                 replace_content=newname)

def file_rename():
    # 多层目录下修改文件名
    fileList = os.listdir(f"C:/Users/打工人/Downloads/{name}")
    print(fileList)
    n = 0
    for i in fileList:
        print(i)
        path=f"C:/Users/打工人/Downloads/{name}/{i}"
        newfileList = os.listdir(path)

        for j in newfileList:
            # 设置新文件名
            newname = 'pic' + str(n + 1)+'.png'
            n += 1
            # del_content:要替换的文件名，replace_content:替换后的文件名
            pofile.replace4filename(path=path,
                                    del_content=j,
                                    replace_content=newname)

def copy_file_to_taget():
    fileList = os.listdir(f"C:/Users/打工人/Downloads/{name}")
    print(f"fileList:{fileList}")
    filePath = 0
    for filePath in fileList:
        path = f"C:/Users/打工人/Downloads/{name}/{filePath}"
        print(f"path:{path}")
        newfileList = os.listdir(path)
        print(newfileList)
        dst_file=os.path.join(f"C:/Users/打工人/Downloads/{name}")
        for j in newfileList:
            src_file=path+"/"+j
            print(src_file)
            shutil.move(src_file,dst_file)

            # shutil.copyfile(src_file,dst_file)  # 循环将每个文件拷贝到target的文件夹下



if __name__ == '__main__':
    folder_rename()
    file_rename()
    copy_file_to_taget()
