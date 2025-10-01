**python preprocessing.py**



**start-all.cmd**



**hdfs dfs -mkdir -p /user/hadoop/wordcount**

**hdfs dfs -put C:/hadoop/bin/wordcount/pageviews-20250901-000000-clean.txt /user/hadoop/wordcount/**



**hadoop jar C:\\hadoop\\share\\hadoop\\mapreduce\\hadoop-mapreduce-examples-3.2.4.jar wordcount /user/hadoop/wordcount/pageviews-20250901-000000-clean.txt /user/hadoop/wordcount/output**



**hdfs dfs -get /user/hadoop/wordcount/output/part-r-00000 C:/hadoop/bin/wordcount/part-r-00000.txt**



**cd C:\\hadoop\\bin\\wordcount**

**type part-r-00000.txt | python topn.py**

**type part-r-00000.txt | python descriptive.py**



hdfs dfs -rm -r -f /user/hadoop/wordcount



hdfs dfsadmin -safemode leave



