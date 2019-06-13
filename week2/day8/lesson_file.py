#__author: root
#data: 2018/10/5


#能调用方法的一定是对象

# import time
# # li=[1,2,3]
# # li.append('2')
#
#
# f=open('小重山2','a',encoding='utf8')
# print(f.fileno())
#
# f.write('\nhello world\n')
# f.write('alex')
# time.sleep(50)
# f.close()

f=open('小重山','r',encoding='utf8')

# print(f.read(5)) #读5个字符
# print(f.read(5))
#
# print(f.readline()) #读取文件一行
# print(f.readline())

#print(f.readlines())  #读所有行，放入列表中

# data=f.readlines()
# f.close()
# data[5]='欲将心事付瑶琴。******'

# number=0
# for i in f:  #for内部将f对象做成迭代器，用一行取一行
#     number += 1
#     if number == 6:
#         i = ''.join([i.strip(),'******'])
#     print(i.strip())
#
# f.close()

# print(f.tell()) #记录光标位置
# print(f.read(2))
# print(f.tell()) # tell 把读到的每个中文字符看作3个字符
#
# f.seek(0)  #调整光标位置
# print(f.read(4))

# import sys,time
#
# for i in range(30):
#     sys.stdout.write("*")
#     sys.stdout.flush()
#     time.sleep(0.2)

# f=open('小重山','a',encoding='utf8')

#f.truncate(5) #保留5个字符，之后的全部删除

# print(f.isatty())
# f.close()


# f=open('小重山','r+',encoding='utf8')
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.write('岳飞')
#
# f.close()

# f=open('小重山','r+',encoding='utf8')
#
# number=0
# for line in f:
#     number += 1
#     if number == 6:
#         f.write('alex')
#
# f.close()

# f_read=open('小重山','r',encoding='utf8')
# f_write=open('小重山2','w',encoding='utf8')
#
# number=0
# for line in f_read:
#     number+=1
#     if number==5:
#         line=''.join([line.strip(),'hello 岳飞\n'])  # 第5行添加内容
#     f_write.write(line)
#
# f_write.close()
# f_read.close()

# a=str({'beijing':{'1':111}})  #转换成字符串
# print(type(a))
# print(a)
# a=eval(a) #转换成字典
# print(type(a))
# print(a['beijing'])



with open('小重山','r',encoding='utf8') as f_read, open('小重山2','w',encoding='utf8') as f_write:
    for line in f_read:
        f_write.write(line)


num = 1
if type(num) is int:
    print('right')


