# Introduction of Spark


环境：Linux的Ubuntu系统


Spark 版本：spark-1.6.3

环境变量设置：

    export SPARK_HOME=$WORK_SPACE/spark-1.6.3
    export PATH=$PATH:$SPARK_HOME/bin
   
关于Spark的Function的理解，我的参考资料主要是这篇博客：[Spark Function](https://www.iteblog.com/archives/1396)

我想从下面这个题目分享一下我关于spark使用的过程和心得：

Requirements:

    –給定一個距離R(公里)以及一個時間T(秒)    
    –使用Spark來找出各種符合條件之竊盜類型序列及其個數    
    –輸出結果內容為竊盜類型序列及其個數，並且根據個數多寡由多到少來進行排序
    
Dataset:[Taipei Burglary2015-01_10.csv](https://drive.google.com/open?id=0ByW2ffFcRkFgOVc1RHFEa0dLTUk)(台北市自行車、汽車、住宅竊盜點資訊)


竊盜類型序列:

     –竊盜事件兩兩距離不大於R公里    
     –整個竊盜序列從第一個竊盜事件到最後一個竊盜事件所經歷的時間不大於T秒
     –序列的先後順序根據發生的時間而定
                  竊盜事件一>竊盜事件二，竊盜事件一的發生時間比竊盜事件二的發生時間早
                  
 輸出要求:
 
     –竊盜類型>竊盜類型>竊盜類型,個數 
     此格式中除了竊盜類型的字有空格外，其餘部分皆不需要以空格隔開   
     –依個數多寡來進行排序
     
 執行模式:
 
     –./bin/spark-submit hw_spark.py2 3600
     –第一個參數讓使用者設定兩兩事件相距的距離
     –第二個參數讓使用者設定竊盜序列的時間長度
     
