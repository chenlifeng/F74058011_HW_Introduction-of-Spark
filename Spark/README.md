
##基本思路：(跟sourcecode里面的代码对应)

      ①	首先将每条数据按照时间递增排序，使用asc()方法排序
      ②	根据窃盗序列的要求【竊盜事件兩兩距離不大於R公里，整個竊盜序列從第一個竊盜事件到最後一個竊盜事件所經歷的時間不大於T秒】
              求出最长的那个序列：先loop每一条element，然后第二个loop从该条element后开始查找时间条件符合的element，然后检查该条element是否与
              序列中原本已经有的element两两距离都不大于R公里，如果符合条件就将这个element的相关信息加入序列
      ③	根据求出的最长序列找出比较短的所有序列
      ④	将找到的所有序列根据序列类型进行排序，并计算出他們各自的个数

##Requirement：

     ①	需要将TaipeiBurglary2015-01_10.csv放进Spark文件下的data中
             （这是我的代码里面设置的路径，如果要放在不同的文件夹，需要去代码里面修改一下路径）
     ②	输入要求：HW_F74058011_Spark.py 2 3600，会输出在output.txt里面
     ③	需要把附带的pyspark_csv.py放在指定路径中（同时要修改代码中的路径）:
              比如我的代码里面对应的路径就是把pyspark_csv.py和HW_F74058011_Spark.py一起放在spark-1.6.3文件夹下面
              注意：pyspark_csv这个repo的othercode文件夹下面可以下载或者需要自己去网上下载

##执行方式：

    ①Spark启动：
        cd ~/Downloads/spark-1.6.3/
        sbin/start-all.sh
    ②sourcecode代码编译运行：
        bin/spark-submit HW_F74058011_Spark.py 2 3600（这是针对本题，因为输入输出已经在代码里面写死）
        根据代码里面写死的输出，会自动在spark-1.6.3文件夹下面新建一個output.txt并且写入输出的结果

##执行结果：(output.txt里面的内容)
     Residential burglary > Bicycle burglary, 51
     Residential burglary > Car burglary, 13
     Car burglary > Bicycle burglary, 1
     Car theft > Bicycle burglary, 1
     Residential burglary > Car burglary > Bicycle burglary, 1

##可能会遇到的问题：
    ①IndentationError: unindent does not match any outer indentation level
      原因：这个问题的原因是因为没有对齐或者tab键和空格键混用导致的，最终发现我的notepad中代码中混有两个tab箭头
      解决方法：原因和解决方法都是由这个Link启发：http://www.crifan.com/python_syntax_error_indentationerror/comment-page-1/
                             可以根据link里面设置避免以后出错
    ②No module named dateutil.parser
      解决方法：
      sudo apt-get install python-pip 
      sudo pip install python-dateutil
     (以上为我遇到的比较大众化的问题，一些基础的语法问题可以根据在terminal的提示在对应的Line修改)

##代码不足之处：
     因为这个Homework比较要求大部分根据Spark的function进行操作，尽量不要用python语法，比如for loop，但是由于我是第一次使用spark和python,
     比较不熟悉， 最后尝试了foreach这个方法没有成功，所以最后代码中用了比较多的for loop进行关于距离条件要求的检查。

##个人感想：
      这是第一次接触数据挖掘以及使用相关技术，对function的理解中间也出现了很多误解，以及遇到很多Python语法的一些错误提示，不过
      terminal都会具体提示错误的位置，所以比较好修改，做完这个作业，看到新的学习领域，值得深入了解。
       
      
