[TOC]

# 密文传输,if else,for 流程判断语句

## if else

* 什么叫做python的标准库 

  只能能够import调用,而不用安装的,叫做标准库

* 调入getpass模块,进行密文

  ```
  import getpass #调用 getpass
  username = input("username:")
  password = getpass.getpass("password:") #调用函数 getpass.getpass 
  print(username,password)
  ```

* pyrhon中单等号表示赋值,双等号表示比较中的等于

* 简单的判断

  ```
  _username = 'mafei0728'
  _password = 'mafei0728'
  username = input("username:")
  password = input("massword:")
  print(username,password)
  if username == _username and password == _password:
      print("welcome user {user} login....".format(user=username) )
  else:
      print("invalid username or password")
  ```

  其实要注意的是函数./format(xxxx)格式化输出

  python强制缩进

* if elif else 语句

  ```
  age_of_mass = 2
  guess_age = int(input("guess age:"))
  if guess_age == age_of_mass:
      print("yes,you got it")
  elif guess_age > age_of_mass:
      print("think smaller")
  else:
      print("think bigger")
  ```

  python默认输入时字符串,是整形数字一定要指定

  ## for循环

  for循环没什么好说的,只要知道for循环也有else就够了

  ```shell
  #常用的跳出多层循环的手法
  # mafei0728
  #!/usr/bin/env python
  # encoding: utf-8
  a = True
  for i in range(10):
      if a:
          print(i)
          for k in range(10):
              if a:
                  print(k)
                  for v in range(10):
                      print(v)
                      a = False
                      break
  #关于for循环的else
  #如果没有正常执行完.是不会打印出执行else的
  # mafei0728
  #!/usr/bin/env python
  # encoding: utf-8
  for i in range(10):
      if i<5:
          print(i)
      else:
          if i == 7:
              break
  
  else:
      print("lose")
  #跟下面这种的区别,都会执行,这个例子作为判断循环是否正常执行的一种方法
  # mafei0728
  #!/usr/bin/env python
  # encoding: utf-8
  for i in range(10):
      if i<5:
          print(i)
      else:
          if i == 9:
              break
  print("lose")
  ```

  

  ​