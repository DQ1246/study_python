import re
s1="hei bai hei lv heibai"
s2="hei bai hei heibai"
#match：从头匹配
result=re.match("hei",s1)
result1=re.match("bai",s1)
print(result)#返回全部信息
print(result.span())#返回目标位置信息
print(result.group())#返回目标内容
print(result1)#没有返回空
#search:规则匹配
result2=re.search("bai",s1)
print(result2)
#findall:全局匹配所有匹配项
result3=re.findall("lv",s2)
result4=re.findall("bai",s1)
print(result3)
print(result4)