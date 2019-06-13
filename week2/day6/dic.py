#__author: root
#data: 2018/10/2
#



# dic={'name':'alex','age':35,'hobby':'girl'}
# print(dic)
# print(dic['hobby'])

# dic2=dict((('name','alex'),('age',18)))
#
# print(dic2)


dic1={'name':'alex','age':18,'hobby':'girl'}
# print(list(dic1.keys()))
# print(list(dic1.values()))
# print(list(dic1.items()))
# print(dic1['name'])

# dic1['age']=55
# print(dic1)

dic5={'name':'alex','age':18,'class':1}
# del dic5['name']
# print(dic5)
#
# dic5.clear()
# print(dic5)

# ret=dic5.pop('age')
# print(ret)
# print(dic5)

# a= dic5.popitem()
# print(a,dic5)

# del dic5
# print(dic5)

# dic6=dict.fromkeys(['host1','host2','host3'],'test')
# print(dic6)


# av_catalog = {
#     "欧美":{
#         "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
#         "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
#         "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
#         "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
#     },
#     "日韩":{
#         "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
#     },
#     "大陆":{
#         "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
#     }
# }
#
# print(av_catalog['大陆']['1024'][1])
# av_catalog["大陆"]["1024"][1] += ",可以用爬虫爬下来"
# print(av_catalog["大陆"]["1024"])



# dic={5:'555',2:'666',4:'444'}
# print(sorted(dic))

dic5={'name':'alex','age':18,'class':1}

#默认遍历key
# for i in dic5:
#     print(i,dic5[i])

# 遍历key
# for i in dic5.keys():
#     print(i)

# 遍历value
# for i in dic5.values():
#     print(i)


# 遍历key-value
# for k,v in dic5.items():
#     print(k,v)



# dic={
#     'zhangsan':{
#         'age':23,
#         'sex':'male'
#     },
#     'lisi':{
#         'age':34,
#         'sex':'male'
#     },
#     'wangwu':{
#         'age':25,
#         'sex':'women'
#     }
# }
#
# print(dic['zhangsan'])
# print(dic['wangwu']['sex'])


#
# a="Let's go"
# print(a*2)
#
# print(a[1::2])
#
# print('et' in a)
# print('en' in a)




a='123'
b='abc'
d='44'
# c=a+b
# print(c)


# c='*****'.join([a,b,d])
# print(c)


# st='hello kitty'
# print(st.count('l'))  # 统计元素个数
# print(st.capitalize())  #字符串首字母大写
# print(st.center(50,'-')) #居中显示字符串，两边用-补齐，总长度为50
#
# print(st.endswith('y'))  #以y结尾，返回真
# print(st.startswith('he')) #以he开头，返回真
# print(st.expandtabs(tabsize=10))
# print(st.find('t'))   #查找到第一个元素，并将索引值返回
#
# st='hello kitty {name} is {age}'
# print(st.format(name='alex',age=37))  #格式化输出另一种方式
# print(st.format_map({'name':'alex','age':22}))
# #print(st.index('q'))
#
# # is系列
# print('abc456'.isalnum())
# print('0b010'.isdecimal())  # 是否为十进制数
# print('123342345'.isdigit()) #是否为整数
# print('124234'.isnumeric())  # 是否为整数
# print('34abc'.isidentifier())  # 是否非法变量
# print('abc'.islower())  #是否全为小写字母
# print('ABC'.isupper())  #是否全为大写字母
# print('  '.isspace())  #是否全为空格
# print('My Title'.istitle()) #是否每个单词开头为大写
#
# print('My Title'.lower())  #所有大写字母转换为小写字母
# print('My Title'.upper())  #所有小写字母转换为大写字母
# print('My Title'.swapcase())  #所有大写字母转换为小写字母，所有小写字母转换为大写字母
# print('My Title'.ljust(50,'*')) #字符串在左侧，右边用*补齐
# print('My Title'.rjust(50,'*')) #字符串在右侧，左边用*补齐
#
# print('   \tMy Title\n'.strip()) #去掉字符串前后的空格、tab、回车
# print('   \tMy Title\n'.lstrip()) #去掉字符串左边的空格、tab、回车
# print('   \tMy Title\n'.rstrip()) #去掉字符串右边的空格、tab、回车
# print('ok')
#
# print('My title title'.replace('title','lesson',1))  #替换一处字符串
# print('My title title'.rfind('t'))  #从右边找t，返回索引
#
# print('My title title'.split(' '))  #空格为分隔符，切割字符串，并转换为列表
# print('My title title'.split('i'))  #i为分隔符，切割字符串，并转换为列表
# print('My title title'.split('i',1))  #i为分隔符，切割字符串,切割一次，并转换为列表
# print('My title title'.rsplit('i',1))  # 从右边切割，i为分隔符，切割一次
#
# print('My title title'.title()) #每个单词开头大写
#

# menu = {
#     '北京':{
#         '朝阳':{
#             '国贸':{
#                 'CICC':{},
#                 'HP':{},
#                 '渣打银行':{},
#                 'CCTV':{},
#             },
#             '望京':{
#                 '陌陌':{},
#                 '奔驰':{},
#                 '360':{},
#             },
#             '三里屯':{
#                 '优衣库':{},
#                 'apple':{},
#             },
#         },
#         '昌平':{
#             '沙河':{
#                 '老男孩':{},
#                 '阿泰包子':{},
#             },
#             '天通苑':{
#                 '链家':{},
#                 '我爱我家':{},
#             },
#             '回龙观':{},
#         },
#         '海淀':{
#             "五道口":{
#                 "谷歌":{},
#                 "网易":{},
#                 "sohu":{},
#                 "sogo":{},
#                 "快手":{},
#             },
#             "中关村":{
#                 'youku':{},
#                 'iqiyi':{},
#                 '汽车之家':{},
#                 '新东方':{},
#                 'QQ':{},
#             },
#         },
#     },
#     '上海':{
#         "浦东":{
#             "陆家嘴":{
#                 "CICC":{},
#                 "高盛":{},
#                 "摩根":{},
#             },
#             "外滩":{},
#         },
#         "闵行":{},
#         "静安":{},
#     },
#     '山东':{
#         "济南":{
#         },
#         "德州":{
#             "乐陵":{
#                 "丁务镇":{},
#                 "城区":{},
#             },
#             "平原县":{},
#         },
#         "青岛":{},
#     },
# }
# for i in menu['北京']:
#     print(i)



s='中国'
s_to_unicode = s.de













