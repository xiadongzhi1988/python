#__author: root
#data: 2018/10/1

name = input("Name:")
age = int(input("Age:"))
job = input("Job:")
salary = input("Salary:")

if salary.isdigit(): #是否为数字
    salary = int(salary)
# else:
#     exit("must input digit") #退出程序


msg = '''
------------info of %s --------
Name: %s
Age : %s
Job : %s
Salary: %f
You will be retired in %s years
------------ end ------------
''' %(name,name,age,job,salary,65-age)

print(msg)

