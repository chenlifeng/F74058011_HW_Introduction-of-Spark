# Introduction of Spark

环境：Linux的Ubuntu系统

##Spark的安装配置
1.在安装Spark之前需要安装scala环境：

scala环境变量设置（修改.bashrc文件）:

   export SCALA_HOME=$WORK_SPACE/scala-2.11.8
   
   export PATH=$PATH:$SCALA_HOME/bin
   
2.Spark 版本：spark-1.6.3

Spark环境变量设置（修改.bashrc文件）:

   export SPARK_HOME=$WORK_SPACE/spark-1.6.3
   
   export PATH=$PATH:$SPARK_HOME/bin
 
 ##Spark的Function
 
关于Spark的Function的理解，我的参考资料主要是这篇博客：[Spark Function](https://www.iteblog.com/archives/1396)

##Spark的执行模式

Spark的编译运行模式：

①切换到spark-1.6.3文件夹下

②执行bin/spark-submit xxx.py

##Hadoop的安装配置
（因为我在使用使用Spark的过程中有套件提示需要用到Hadoop，所以说一下Hadoop的安装后的配置问题，下面是我的ubuntu系统的配置，这边的配置有求助助教帮忙配置，感谢！）

1.core-site.xml：

       <property>
          <name>fs.defaultFS</name>
          <value>hdfs://chenlf-virtual-machine:9000/</value>  （PS.这里的“chenlf-virtual-machine”是修改为本地的hostname）
       </property>

2.hdfs-site.xml：

       <property>
           <name>dfs.namenode.secondary.http-address</name>
           <value>node1:9001</value>
       </property>
       <property>
           <name>dfs.namenode.name.dir</name>
           <value>file:/home/hdc/workspace/hadoop_tmp/hdfs/namenode</value>
       </property>
       <property>
           <name>dfs.namenode.data.dir</name>
           <value>file:/home/hdc/workspace/hadoop_tmp/hdfs/datanode</value>
       </property>
       <property>
           <name>dfs.replication</name>
           <value>1</value>
       </property>
    


          

3.mapred-site.xml：

       <property>
              <name>mapreduce.framework.name</name>
              <value>yarn</value>
       </property>

4.yarn-site.xml：

（PS.这里的“chenlf-virtual-machine”是修改为本地的hostname）

    <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
       </property>

       <property>
           <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
           <value>org.apache.hadoop.mapred.ShuffleHandler</value>
       </property>

       <property>
           <name>yarn.resourcemanager.address</name>
           <value>chenlf-virtual-machine:8032</value>
       </property>

       <property>
           <name>yarn.resourcemanager.scheduler.address</name>
           <value>chenlf-virtual-machine:8030</value>
       </property>

       <property>
           <name>yarn.resourcemanager.resource-tracker.address</name>
           <value>chenlf-virtual-machine:8035</value>
       </property>

       <property>
           <name>yarn.resourcemanager.admin.address</name>
           <value>chenlf-virtual-machine:8033</value>
       </property>

       <property>
           <name>yarn.resourcemanager.webapp.address</name>
           <value>chenlf-virtual-machine:8088</value>
       </property>
              
 5.设置 .bashrc文件：（PS.下面路径一些需要根据自己主机的路径进行对应的更改）
 
              export HADOOP_PREFIX="/home/chenlf/Downloads/hadoop-2.6.0"
              export HADOOP_HOME="/home/chenlf/Downloads/hadoop-2.6.0"
              export HADOOP_MAPRED_HOME="/home/chenlf/Downloads/hadoop-2.6.0"
              export HADOOP_CONF_DIR="/home/chenlf/Downloads/hadoop-2.6.0/etc/hadoop"
              export HADOOP_HDFS_HOME="/home/chenlf/Downloads/hadoop-2.6.0"
              export HADOOP_YARN_HOME="/home/chenlf/Downloads/hadoop-2.6.0"
              export YARN_CONF_DIR=$HADOOP_CONF_DIR
              export PATH=$PATH:$HADOOP_HOME/bin
              export PATH=$PATH:$HADOOP_HOME/sbin

              export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
              export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib"
         
         
##使用Spark可能会遇到的问题：
 ①IndentationError: unindent does not match any outer indentation level
 
   原因：这个问题的原因是因为没有对齐或者tab键和空格键混用导致的，最终发现我的notepad中代码中混有两个tab箭头
   
   解决方法：原因和解决方法都是由这个Link启发：http://www.crifan.com/python_syntax_error_indentationerror/comment-page-1/
   
   可以根据link里面设置避免以后出错
                          
 ②No module named dateutil.parser
 
   解决方法：
   
   sudo apt-get install python-pip 
   
   sudo pip install python-dateutil
   
  (以上为我遇到的比较大众化的问题，一些基础的语法问题可以根据在terminal的提示在对应的Line修改)
  
 ③java.net.ConnectException: Call From chenlf-virtual-machine/192.168.132.128 to chenlf-virtual-machine:9000 failed on connection exception: java.net.ConnectException: Connection refused; For more details see:  http://wiki.apache.org/hadoop/ConnectionRefused
 
   原因：这个是上面提到的遇到的Hadoop的问题，可能是代码中引入的某些插件需要用到hadoop
   
   解决方法：可以启动hadoop，再将数据上传到hdfs
     
         
##例子：关于台北市窃盗Pattern的查找
 
 
 
我想从下面这个题目分享一下我关于spark使用的过程和心得：

根据Dataset:[Taipei Burglary2015-01_10.csv](https://drive.google.com/open?id=0ByW2ffFcRkFgOVc1RHFEa0dLTUk)(台北市自行車、汽車、住宅竊盜點資訊)
寻找台北市的窃盗PATTERN

   –給定一個距離R(公里)以及一個時間T(秒)   
   
   –使用Spark來找出各種符合條件之竊盜類型序列及其個數  
   
   –輸出結果內容為竊盜類型序列及其個數，並且根據個數多寡由多到少來進行排序
    




                  
 
     
 
 
     
