#!/bin/sh

log_file=/home/ec2-user/bm.log

echo "bench m5 echo" >> $log_file
wrk -c 256 -t 8 -d10m --latency http://172.31.46.126:8000/echo >> $log_file
sleep 5m
echo "bench m6g echo" >> $log_file
wrk -c 256 -t 8 -d10m --latency http://172.31.32.42:8000/echo >> $log_file


sleep 5m
echo "bench m5 uuid" >> $log_file
wrk -c 256 -t 8 -d10m --latency http://172.31.46.126:8000/uuid >> $log_file
sleep 5m
echo "bench m6g uuid" >> $log_file
wrk -c 256 -t 8 -d10m --latency http://172.31.32.42:8000/uuid >> $log_file


sleep 5m
echo "bench m5 pi" >> $log_file
wrk -c 256 -t 8 -d10m --latency http://172.31.46.126:8000/pi?steps=1000 >> $log_file
sleep 5m
echo "bench m6g pi" >> $log_file
wrk -c 256 -t 8 -d10m --latency http://172.31.32.42:8000/pi?steps=1000 >> $log_file