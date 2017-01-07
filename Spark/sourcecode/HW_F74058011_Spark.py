from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
import math
import datetime
import time
import itertools
import sys
import pyspark_csv as pycsv

def rad(d):
    return d * math.pi/180.0

def getDistance(lat1, lng1, lat2, lng2):
    EARTH_RADIUS = 6378.137
    lat1 = float(lat1)
    lng1 = float(lng1)
    lat2 = float(lat2)
    lng2 = float(lng2)
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    latD = radLat1 - radLat2    
    lngD = rad(lng1) - rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(math.sin(latD/2),2) + math.cos(radLat1)*math.cos(radLat2)*math.pow(math.sin(lngD/2),2)))
    s = s * EARTH_RADIUS;
    s = round(s * 10000) / 10000
    if s<0:
        return -s
    else:
        return s

def checkTime(t1, t2,T):
    if abs((t1-t2).total_seconds())<=T:
        return 1
    else:
        return 0

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def findLargestPattern(tmp,pattern,T,R):
    all=tmp.collect()
    for x in range(0, len(all)):
        initStr = all[x].Type
        gotcha = 0
        flag = 1
        tempLan = [all[x].Latitude]
        tempLng = [all[x].Longitude]
        for y in range(x+1, len(all)):
            xTime = all[x].Time
            yTime = all[y].Time
            if checkTime(yTime,xTime,T)==1:
                yLan = all[y].Latitude
                yLon = all[y].Longitude
                for i in range(0, len(tempLan)):
                    if getDistance(tempLan[i], tempLng[i], yLan, yLon)<=R:
                        flag = 1
                    else:
                        flag = 0
                if flag==1:
                    gotcha = 1
                    initStr += ' > '
                    initStr += all[y].Type
                    tempLan.append(yLan)
                    tempLng.append(yLon)
                else:
                    flag = 1
        if gotcha == 1:
            pattern.append({'strs' : initStr})
    return pattern

def findOtherPattern(pattern): 
    for x in range(0, len(pattern)):
            if pattern[x]["strs"].count(" > ") > 1:
                temp = pattern[x]["strs"].split(" > ")
                for y in range(2, len(temp)):
                    tempList = list(itertools.combinations(temp, y))
                    for z in range (0, nCr(len(temp), y) - nCr(len(temp)-1 , y)):
                        initStr = tempList[z][0]
                        for zz in range(1, len(tempList[z])):
                            initStr += ' > '
                            initStr += tempList[z][zz]
                        pattern.append({'strs' : initStr})
    return pattern

if __name__ == "__main__":
    conf = SparkConf().setAppName("HW_F74058011_Spark").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    sqlContext=SQLContext(sc)
    #sc.addPyFile('/home/chenlf/Downloads/pyspark_csv.py')
    T = int(sys.argv[1])
    R = float(sys.argv[2])
    f = open('output.txt', 'w')
    pattern = []
    data = sc.textFile("TaipeiBurglary2015-01_10.csv")
    df=pycsv.csvToDataFrame(sqlContext,data)
    df=df.sort(df.Time.asc())
    pattern=findLargestPattern(df,pattern,T,R)
    pattern=findOtherPattern(pattern)
    df2 = sqlContext.createDataFrame(pattern)
    all2 = df2.groupBy("strs").count().sort("count", ascending=False).collect()
    for x in range(0, len(all2)):
        f.write(str(all2[x][0])+', '+str(all2[x][1])+'\n')

    f.close()
  
  








