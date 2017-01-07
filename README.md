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
         
         
         
##关于台北市窃盗Pattern的查找
 
 
 
我想从下面这个题目分享一下我关于spark使用的过程和心得：

根据Dataset:[Taipei Burglary2015-01_10.csv](https://drive.google.com/open?id=0ByW2ffFcRkFgOVc1RHFEa0dLTUk)(台北市自行車、汽車、住宅竊盜點資訊)
寻找台北市的窃盗PATTERN

   –給定一個距離R(公里)以及一個時間T(秒)   
   
   –使用Spark來找出各種符合條件之竊盜類型序列及其個數  
   
   –輸出結果內容為竊盜類型序列及其個數，並且根據個數多寡由多到少來進行排序
    




                  
 
     
 
 
     
