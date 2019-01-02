# Python基础  变量与基本数据类型

## 保留字与标识符

1. 保留字

   保留字是Python语言中已经赋予特定意义的一些单词，开发时，不可以把这些保留字作为变量，函数，类，模块和其他对象的名称来使用。那么，Python中有哪些保留字呢?

   ```python
   import keyword #引入关键字模块
   
   print(keyword.kwlist) #获取关键字列表
   ```

   ![1546002489433](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1546002489433.png)

   在Python中是区分大小写的，所以False是关键字，而false则不是，但是也不推荐这么用。避免发生不可预期的错误。

   如果在开发中使用了保留字，会发生什么？

   ```python
   if = "我看看会发生什么"
   print(if)
   ```

   ![1546002679033](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1546002679033.png)

   这里可以看到会发生错误。

2. 标识符

   表示符可以简单的理解为一个名字，比如每个人都有自己的名字，它主要用来标识变量，函数，类，模块和其他对象的名称。

   Python中的表示符命名规则：

   - 由字母，下划线（_）和数字组成，并且第一个字符不能是数字。目前Python中只允许使用ISO-Latin字符集中的字符A~Z和a~z。

   - 不能使用Python中的保留字

     一下都是合法的标识符

     > USERID
     >
     > book
     >
     > user_id
     >
     > myname \#保留字和其他字符组合是合法标识符
     >
     > book001 \# 数字在标识符后面是可以的。

     下面的是非法标识符：

     > 4word \# 以数字开头
     >
     > class # 使用保留字
     >
     > @you #  不能使用特殊字符@
     >
     > book list  \# book和list中间有空格

   - 区分大小写

## 变量

1. 理解Python中的变量

   在Python中，变量严格意义上应该成为“名字”，也可以理解为标签。如：name = '路飞',这里的name就称为变量。

2. 变量的定义与使用

   在Python中，不需要先声明变量的类型，直接赋值即可创建各种类型的变量，但是变量的命名并不是任意的，应该遵循以下几条原则：

   - 变量名必须是一个有效的标识符
   - 变量名不能使用Python的保留字
   - 慎用小字母i和大写字母O(因为和1和0很像)
   - 应该选择有意义的单词作为变量名。

   为变量赋值可以通过等号(=)来实现，语法格式：

   > 变量名 = value
   >
   > 例如：num = 1024

   在python中可以同时为多个变量同时赋值。例如：

   ```python
   myname, age = '路飞', 18
   print(myname, age )
   ```

   ![1546003946519](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1546003946519.png)

## 基本数据类型

1. 数字类型

   - 整数

     和数学中的整数一样，指的是没有小数部分

     - 十进制整数 （不能以0开头）如：1， 2， 555， -299等
     - 八进制 ：由0~7组成，逢8进1，并以0o开头的数，如0o123
     - 十六进制：由0~9，A~F组成，逢16进1，并且以0x或0X开头的数，如0x25

   - 浮点数

     浮点数是由整数部分和小数部分组成如：0.2

     ```python
     print(0.1 == 0.1 )
     print(0.2 == 0.2)
     a = 0.1 + 0.2
     print(a == 0.3) #这将是一个神奇的结果
     ```

     用浮点数来进行比较时要小心！

     **作业练习**

     根据身高，体重计算BMI指数。BMI = 体重 / (身高 X 身高)

   - 复数，和数学中的复数一样，由实部和虚部组成。例如：3.14 + 12.5j

2. 字符串类型

   字符串就是连续的字符序列，用两个单引号('')或连个双引号("")或三个引号(''' 或""")来包含起来。

   ```python
   title = "这是一个字符串" #使用双引号创建字符串
   name = '路飞' #使用单引号创建字符串
   #使用三个引号来创建字符串
   word = """我是成为海贼王的男人！
   海賊王に俺はなる！
   """
   print(title)
   print(name)
   print(word)
   ```

   ![1546005324532](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1546005324532.png)

3. 布尔类型

   布尔类型就是表示真假的值，True，False两个值。另外1也可以表示真，0也可以表示假

   ```python
   print(True == 1)
   print(True == 0)
   print(False == 1)
   print(False == 0)
   ```

   ![1546005523499](C:\Users\Think\AppData\Roaming\Typora\typora-user-images\1546005523499.png)

4. 数据类型转换

   int(x):将x转换成整数

   float(x):将x转换成浮点类型

   complex(real,[,imag]): 创建一个复数

   str(x):将x转换成字符串

   repr(x):将x转换成表达式字符串

   eval(str):计算在字符串中有效的Python表达式，并返回一个对象

   chr(x):将x转换成一个字符

   ord(x):将x转换成它对应的数值

   hex(x):将整数x转换成一个16进制的字符串

   oct(x):将整数x转换成一个8进制的字符串

   ```python
   # 模拟超市抹零结账
   money_all = 56.7 + 32.9 + 87.52 #累加金额
   money_all_str = str(money_all) #转换成字符串
   print("总金额为："+ money_all_str)
   money_real = int(money_all) #取整
   money_real_str = str(money_real)
   print("实收："+ money_real_str)
   ```

