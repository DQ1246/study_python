from data import record
import json
class filereader:
    def reader(self)->list[record]:#顶层封装
        pass
class textfilereader(filereader):#子类1，文件类型：文本
    def __init__(self,path):#文件路径
        self.path=path
    def reader(self):
        with open(self.path,'r',encoding="UTF-8") as f:
            record_list=[]
            for line in f.readlines():
                line=line.strip()#消除文件的/
                data=line.split(",")#分割数据
                Record=record(data[0],data[1],int(data[2]),data[3])
                record_list.append(Record)
            return record_list
class jsonfilereader(filereader):#子类2，文件类型：JSON
    def __init__(self,path):#文件路径
        self.path=path
    def reader(self):
        with open(self.path,'r',encoding="UTF-8") as f:
            record_list = []
            for line in f.readlines():
                line=json.loads(line)
                Record=record(line["date"],line["order_id"],line["money"],line["province"])
                record_list.append(Record)
            return record_list
if __name__ == '__main__':
    a=textfilereader("2011年1月销售数据.txt")
    b=jsonfilereader("2011年2月销售数据JSON.txt")
    print(a.reader())
    for x in a.reader():
        print(x)