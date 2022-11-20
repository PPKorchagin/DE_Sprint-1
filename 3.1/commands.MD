hadoop dfs -put vim1.txt hdfs://localhost:9000/vim1.txt

hadoop dfs -put vim2.txt hdfs://localhost:9000/vim2.txt

hadoop dfs -put vim3.txt hdfs://localhost:9000/vim3.txt

hadoop dfs -put vim4.txt hdfs://localhost:9000/vim4.txt

hadoop dfs -ls /

```
-rw-r--r--   1 lybavsky supergroup     736519 2022-11-20 20:39 /vim1.txt
-rw-r--r--   1 lybavsky supergroup     770324 2022-11-20 20:39 /vim2.txt
-rw-r--r--   1 lybavsky supergroup     843205 2022-11-20 20:39 /vim3.txt
-rw-r--r--   1 lybavsky supergroup     697960 2022-11-20 20:39 /vim4.txt
````

hadoop fs -appendToFile vim1.txt vim2.txt vim3.txt vim4.txt hdfs://localhost:9000/vim_full.txt

hadoop fs -ls /
```
-rw-r--r--   1 lybavsky supergroup     736519 2022-11-20 20:39 /vim1.txt
-rw-r--r--   1 lybavsky supergroup     770324 2022-11-20 20:39 /vim2.txt
-rw-r--r--   1 lybavsky supergroup     843205 2022-11-20 20:39 /vim3.txt
-rw-r--r--   1 lybavsky supergroup     697960 2022-11-20 20:39 /vim4.txt
-rw-r--r--   1 lybavsky supergroup    3048008 2022-11-20 20:44 /vim_full.txt
```

hadoop fs -chmod 755 "/vim*.txt"


hadoop fs -ls -h /

```
-rwxr-xr-x   1 lybavsky supergroup     736519 2022-11-20 20:39 /vim1.txt
-rwxr-xr-x   1 lybavsky supergroup     770324 2022-11-20 20:39 /vim2.txt
-rwxr-xr-x   1 lybavsky supergroup     843205 2022-11-20 20:39 /vim3.txt
-rwxr-xr-x   1 lybavsky supergroup     697960 2022-11-20 20:39 /vim4.txt
-rwxr-xr-x   1 lybavsky supergroup    3048008 2022-11-20 20:44 /vim_full.txt
```


hadoop fs -du -h /

```
719.3 K  719.3 K  /vim1.txt
752.3 K  752.3 K  /vim2.txt
823.4 K  823.4 K  /vim3.txt
681.6 K  681.6 K  /vim4.txt
2.9 M    2.9 M    /vim_full.txt
```


hadoop fs -setrep 2 "/vim*.txt"

hadoop fs -du -h /

```
719.3 K  1.4 M  /vim1.txt
752.3 K  1.5 M  /vim2.txt
823.4 K  1.6 M  /vim3.txt
681.6 K  1.3 M  /vim4.txt
2.9 M    5.8 M  /vim_full.txt
```

hadoop fs -cat /vim_full.txt | wc -l

```
10272
```
