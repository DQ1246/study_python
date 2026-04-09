import os
def get_file(path):
    file_list=[]#新的空列表
    if os.path.exists(path):#文件存在
        for x in os.listdir(path):#文件列表
            new_path=path+"/"+x
            if os.path.isdir(new_path):
                file_list+=get_file(new_path)#递归，不是文件，调用自己，成为新的path，同时file_list持续记录文件
            else:
                file_list.append(new_path)
    else:
        print(f"指定目录{path},不存在")
        return []
    return file_list
if __name__ == '__main__':
    print(get_file("a"))
