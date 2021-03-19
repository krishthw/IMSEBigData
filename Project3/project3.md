**Project 3**

**Mappper: mapperP3K.py**  
Input:  
key = url of website  
value = PageRank and outgoing links from that website 
 
Output for each outgoing link:  
key = outgoing link url   
value = original website, number of outgoing links(M) and PageRank 
 
Each Reducer gets outgoing link url as key and iterable of all outgoing links as values. The output of mapper is the newly computed PageRank using the formula v =M.v. 
 
**Reduce:reducerP3K.py**  
Input:  
key = outgoing link url  
values = Iterable of all links to outgoing link url  

Output:  
key = outgoing link url (which is the same as the source in this case)   
value = Newly computed PageRank (using the formula) 

**Steps**  

1. execute mapper and runner

        chmod +x mapperP3K.py 
        chmod +x reducerP3K.py 
2. copy v_initial.csv to mapper input vector.csv

        cp v_initial.csv vector.csv  
        
3. unix pipe command to get the answer to 1st iteration

        cat M.csv | python mapperP3K.py | python reducerP3K.py  
        
4. Run iteration twice in HDFS. mapper, reducer, runner and vector should be in home directory and M.csv should be in HDFS. 

        bash runmrP3K.sh  
        
**Description for runmrP3K.sh**  
copy v_initial.csv to mapper input vector.csv  
```cp v_initial.csv vector.csv  ```

The first map reduce job  
output will be saved in hdfs folder: /user/krishwera/Group/outputP3K_iter1/part-00000
```hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.13.0.jar \
        -input /user/krishwera/Group/M.csv \
        -output /user/krishwera/Group/outputP3K_iter1 \
        -file mapperP3K.py \
        -file reducerP3K.py \
        -mapper "python mapperP3K.py" \
        -reducer "python reducerP3K.py" \
        -file vector.csv 
```
change name of part-00000 to vector1.csv
```hdfs dfs -mv Group/outputP3K_iter1/part-00000 Group/outputP3K_iter1/vector1.csv ```
 
get vector1.csv out of HDFS to home directory
```hdfs dfs -get /user/krishwera/Group/outputP3K_iter1/vector1.csv /home/krishwera/ ```

copy vector1.csv to mapper input vector.csv  
```cp vector1.csv vector.csv```

The second map reduce job  
output will be saved in hdfs folder: /user/krishwera/Group/outputP3K_iter2/part-00000
```hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.13.0.jar \
        -input /user/krishwera/Group/M.csv \
        -output /user/krishwera/Group/outputP3K_iter2 \
        -file mapperP3K.py \
        -file reducerP3K.py \
        -mapper "python mapperP3K.py" \
        -reducer "python reducerP3K.py" \
        -file vector.csv
```

