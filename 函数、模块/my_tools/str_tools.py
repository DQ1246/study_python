def str_reverse(s):
    # s1= list(s)
    # s2=s1.copy()#不能简单的用变量赋值而是通过copy或则list（）
    # count=-1
    # for x in s1:
    #     s2[count]=x
    #     count-=1
    # s3=''.join(s2)#".join服务于列表字符串，连接符，单引号内可放入符号
    # return s3
    return s[::-1]#序列的反转
if __name__ == '__main__':
    s="汉语"
    print(str_reverse(s))

def substr(s,x,y):
    return s[x:y:1]#都用序列
if __name__ == '__main__':
    s="abdcefg"
    print(substr(s,2,4))