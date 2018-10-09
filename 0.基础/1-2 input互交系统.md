# 1-3 input互交系统

* 字符串拼接
```python
  `name = input("name;")
  age = input("age:")
  job = input("jon:")
  salary = input("salary:")
  info = ''' -----------------info of ''' + name +'''--------------
  Name:'''+ name + '''
  Age:'''+ age + '''
  Job:'''+ job + '''
  Salary:'''+ salary + '''
  '''
  print(info)`
  字符串拼接没有什么好说
---------------------------------------------------------------------------------------------------------------
# 变量
`name = input("name;")
age = input("age:")
job = input("job:")
salary = input("salary:")
info = ''' -----------------info of %s--------------
Name:%s
Age:%s
Job:%s
Salary:%s
''' % (name,name,age,job,salary )
print(info)`
*这里特别注意%s 代表字符串变量,如果age换成%d,就只能输入数字了*
如果我们把把age的 变量换成 %d 了 ,我们输出任何数字都会报错
第三个函数 print(type(age)) -------->打印age是什么字符类型.
第四个函数 int() ------->整形  
python默认输出输入都是字符串,除非强制转
age 的变量改成%d 必须强制把字符串转成整形数字int(input(age));
`name = input("name;")
age = int(input("age:"))
print(type(age))
job = input("job:")
salary = input("salary:")
info = ''' -----------------info of %s--------------
Name:%s
Age:%d
Job:%s
Salary:%s
''' % (name,name,age,job,salary )
print(info)
`
------------------------------------------------------------------------------------------------------------
第五个函数 .format()--------------------->格式化输出用法见上面
`name = input("name;")
age = int(input("age:"))
print(type(age))
job = input("jon:")
salary = input("salary:")
info = ''' -----------------info of {_name}--------------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name=name,
            _age=age,
           _job=job,
           _salary=salary
           )
print(info)`
另外一种输出方法
`name = input("name;")
age = int(input("age:"))
print(type(age))
job = input("jon:")
salary = input("salary:")
info = ''' -----------------info of {0}--------------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)
print(info)`

--------------------------------------------------------------------------------------------------------