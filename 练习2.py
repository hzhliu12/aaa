##冒泡排序
def bubble_sort(lists):  #定义一个函数 bubble_sort
 # 选择排序
    count = len(lists)
    for i in range(0,count):
        for j in range(i+1,count):
            if lists[i]>lists[j]:
                lists[i],lists[j] = lists[j],lists[i]
             #定义一个函数
    return lists
if __name__ == "__main__": #直接执行 __name__等于文件名（包含了后缀.py）而“__main__”等于当前执行文件的名称（包含了后缀.py）
    lists = [1,2,6,0.3,2,0.5,-1,2.4]
    print("排序前序列为："),
    for i in lists:
        print(i)
    print("\n排序后结果为："),
    for i in bubble_sort(lists):
        print(i)