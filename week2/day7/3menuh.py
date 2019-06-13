#__author: root
#data: 2018/10/4



menu = {
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'HP':{},
                '渣打银行':{},
                'CCTV':{},
            },
            '望京':{
                '陌陌':{},
                '奔驰':{},
                '360':{},
            },
            '三里屯':{
                '优衣库':{},
                'apple':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '阿泰包子':{},
            },
            '天通苑':{
                '链家':{},
                '我爱我家':{},
            },
            '回龙观':{},
        },
        '海淀':{
            "五道口":{
                "谷歌":{},
                "网易":{},
                "sohu":{},
                "sogo":{},
                "快手":{},
            },
            "中关村":{
                'youku':{},
                'iqiyi':{},
                '汽车之家':{},
                '新东方':{},
                'QQ':{},
            },
        },
    },
    '上海':{
        "浦东":{
            "陆家嘴":{
                "CICC":{},
                "高盛":{},
                "摩根":{},
            },
            "外滩":{},
        },
        "闵行":{},
        "静安":{},
    },
    '山东':{
        "济南":{
        },
        "德州":{
            "乐陵":{
                "丁务镇":{},
                "城区":{},
            },
            "平原县":{},
        },
        "青岛":{},
    },
}


current_layer = menu # 保存当前状态
parent_layers = []  #状态列表

while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:continue
    if choice in current_layer:
        parent_layers.append(current_layer)  #修改状态时，把当前状态追加到列表中
        current_layer = current_layer[choice] #修改当前状态
    elif choice == "b":
        if parent_layers: #列表不空
            current_layer = parent_layers.pop() #返回时，弹出列表最后一项，赋给当前状态
    elif choice == 'q':
        break
    else:
        print("无此项")







