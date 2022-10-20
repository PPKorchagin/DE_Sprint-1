# ➜  1 git:(main) ✗ docker exec -it broker kafka-console-consumer --bootstrap-server 127.0.0.1:9092 --topic testt  --from-beginning
#
# test string1
# tetest str2
# test str3
# test str4
# test str5
#
# ^CProcessed a total of 5 messages


# ➜  1 git:(main) ✗ kcat -C -t testt -b localhost:9092 -e
# test string1
# tetest str2
# test str3
# test str4
# test str5
# % Reached end of topic testt [0] at offset 5: exiting


import kafka
from kafka import TopicPartition, OffsetAndMetadata
from kafka.consumer.fetcher import ConsumerRecord

SRV = "127.0.0.1:9092"
TPC = "testt"

#, group_id="testgr"
kc = kafka.KafkaConsumer(TPC, bootstrap_servers=SRV, auto_offset_reset='earliest')


tp=TopicPartition(TPC,0)
# print(kc.topics())

# kc.seek_to_end(tp)

end_off=list(kc.end_offsets([tp]).values())[0]
print(end_off)

for msg in kc:
    print(msg.offset,":",msg.value)
    msg: ConsumerRecord = msg

    # om = OffsetAndMetadata(msg.offset + 1, 0)
    # kc.commit({tp: om})
    if msg.offset == end_off-1:
        break