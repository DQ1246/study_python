def print_file_info(file_name):
    try:
        # 不用TRUE，因为他是值，不能看作一个对象，none为空，相当于占位
        # 防止open没创立，导致f.close异常，当然用with open更好
        f=None
        f=open(file_name,'r',encoding="UTF-8")
        print(f.read())
    except Exception as e:
        print(f"文件不存在，捕获异常:{e}")
    finally:
        if f is not None:
            f.close()
if __name__ == '__main__':
    print_file_info("test.txt")

def append_to_file(file_name,date):
    with open(file_name,'a',encoding="UTF_8") as f:
        f.write(date)
        f.flush()#可用可不用，with open有flush的功能
if __name__ == '__main__':
    append_to_file("test.txt", "测试")