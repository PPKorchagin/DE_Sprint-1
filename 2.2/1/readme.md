➜  1 git:(main) ✗ docker exec -it broker kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic testt  --from-beginning

test string1
tetest str2
test str3
test str4
test str5

^CProcessed a total of 5 messages

----


➜  1 git:(main) ✗ kcat -C -t testt -b localhost:9092 -e
test string1
tetest str2
test str3
test str4
test str5
% Reached end of topic testt [0] at offset 5: exiting


----