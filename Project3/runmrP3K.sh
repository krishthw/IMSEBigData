#!/bin/bash

cp v_initial.csv vector.csv
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.13.0.jar \
        -input /user/krishwera/Group/M.csv \
        -output /user/krishwera/Group/outputP3K_iter1 \
        -file mapperP3K.py \
        -file reducerP3K.py \
        -mapper "python mapperP3K.py" \
        -reducer "python reducerP3K.py" \
        -file vector.csv
        
hdfs dfs -mv Group/outputP3K_iter1/part-00000 Group/outputP3K_iter1/vector1.csv 
hdfs dfs -get /user/krishwera/Group/outputP3K_iter1/vector1.csv /home/krishwera/
cp vector1.csv vector.csv

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.13.0.jar \
        -input /user/krishwera/Group/M.csv \
        -output /user/krishwera/Group/outputP3K_iter2 \
        -file mapperP3K.py \
        -file reducerP3K.py \
        -mapper "python mapperP3K.py" \
        -reducer "python reducerP3K.py" \
        -file vector.csv
