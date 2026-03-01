from my_tools import file_tools
from my_tools import str_tools
print(str_tools.str_reverse("梦白愿，第一个工具包"))
print(str_tools.substr("梦白愿，第一个工具包",3,7))
file_tools.append_to_file("测试3.txt", "自定义工具包—模块、异常（综合）")
file_tools.print_file_info("测试3.txt")