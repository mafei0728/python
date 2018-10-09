# 2-1 while循环,break,continue

whlie,for循环,break,continue 

- 一个简单的while脚本 while +else
   if  guess_age == age_of_mass:
- 一个简答的for循环 range(3) 指的是取值0,1,2不包含3 
 ```python
        age_of_mass = 2
        for i in range(3):
          guess_age = int(input("guess age:"))
          if guess_age == age_of_mass:
              print("yes,you got it")
              break
          elif guess_age > age_of_mass:
              print("think smaller")
          else:
              print("think bigger")
        else:
         print("you guess so many times, fuck off")


- 追加的考虑是否三次失败后继续,并输出,你竞猜的次数
 ```python
age_of_mass = 2
      count = 0
      while count < 3:
         guess_age = int(input("guess age:"))
         if  guess_age == age_of_mass:
             print("yes,you got it")
             break
         elif guess_age > age_of_mass:
                 print("think smaller")
         else:
                 print("think bigger")
         count += 1
         if count == 3:   
             chioce = input("you have guess three times,are you want to go on :")
             if  chioce != "n":
                 count = 0
             else:
                 print("ok  maybe you want to chioce give up")


- 不管有没有猜对,结束的时候打印所猜的次数
    ```python
      age_of_mass = 2
      count = 0
      _times = 0
      while count < 3:
         _times +=1
         guess_age = int(input("guess age:"))
         if  guess_age == age_of_mass:
             print("yes,you got it")
             print("congratulation!!!,You only guessed {times} times altogether".format(times=_times))
             break
         elif guess_age > age_of_mass:
                 print("think smaller")
         else:
                 print("think bigger")
         count += 1
         if count == 3:
             chioce = input("you have guess three times,are you want to go on :")
             if  chioce != "n":
                 count = 0
             else:
                 print("ok  maybe you want to chioce give up,and you guessed {times} times altogether".format(times=_times))

- 最后说下 range()函数步长
​```python
      for i in range(0,6,2):
          {0,2,3,6}
          print("mass",i)
          指的是间隔一个打印一个,默认是1,
- continue 和break的区别
  - continue是跳出本次循环,进入下一个循环;break是结束循环
        for i in range(0,20):
            if i < 10:
                print("mass",i)
            else:
                print("hhe")
                print(i)
                continue
            print("test")


猜年龄全版本
​```python
age_of_mass = 2
count = 0
count1 = 0
while count < 3:
    count += 1
    count1 += 1
    guess_age = input("guess age:")
    if guess_age.isdigit():
        guess_age=int(guess_age)
    else:
        print("\033[31;1m您输入的有误,请重新输入\033[0m")
        continue
    if guess_age == age_of_mass:
        print("yes,you got it")
        print("您一共猜了\033[31;1m%d\033[0m次" %count1)
        break
    elif guess_age > age_of_mass:
        print("think smaller")
    else:
        print("think bigger")
    if count == 3:
        chioce = input("you have guess three times,are you want to go on :")
        if chioce != "n":
            count = 0
        else:
            print("ok  maybe you want to chioce give up")
            print("您一共猜了\033[31;1m%d\033[0m次" % count1)
    else:continue
 ```
```shell
#while也有else
# mafei0728
#正常打印ok
#!/usr/bin/env python
# encoding: utf-8
a = 1
b = False
while not b:
    if a>3:
        print(a)
        b = True
    a += 1

else:
    print("ok")
#不能正常打印
# mafei0728
#!/usr/bin/env python
# encoding: utf-8
a = 1
b = False
while not b:
    if a>3:
        print(a)
        break
    a += 1

else:
    print("ok")
```

