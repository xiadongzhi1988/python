#__author: root
#data: 2018/10/1

_user = "wuxing"
_passwd = "abc123"
count = 0
while count < 3:
    username = input("username:")
    password = input("password:")
    if username == _user and password == _passwd :
        print("Welcome %s login ...." % _user)
        break
    else:
        print("Invalid username or password")
    count += 1
    if count == 3:
        keep_going_choise = input("是否继续[y/n]")
        if keep_going_choise == "y":
            count = 0
else:
    print("尝试很多次了")


