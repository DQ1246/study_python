a_list=[1,2,3,4,5,6,7,8,9,10]
def a_list_while():
    count=0
    b_list=[]
    while count<len(a_list):
        if a_list[count]%2==0:
            b_list.append(a_list[count])
        count+=1
    a_list.extend(b_list)
    print(f"偶数列表：{b_list},while循环的新列表：{a_list}")
def a_list_for():
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    c_list=[]
    for x in a_list:
        if x%2==0:
            c_list.append(x)
    a_list.extend(c_list)
    print(f"偶数列表：{c_list},for循环的新列表：{a_list}")
a_list_while()
print(a_list)
a_list_for()

