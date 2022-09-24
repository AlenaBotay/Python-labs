#!/bin/bash
touch info.txt
echo "Hello, $USER" > info.txt

echo $'\n' >> info.txt

suffix=`date -u`
echo "time: $suffix" >> info.txt

echo "os: $OSTYPE" >> info.txt


eval echo "home directory: ~$different_user" >> info.txt


memfree=`awk '/MemFree/ { printf "%.3f \n", $2/1024/1024 }' /proc/meminfo`
memtotal=`awk '/MemTotal/ { printf "%.3f \n", $2/1024/1024 }' /proc/meminfo`

echo "memory: $memtotal G (used), $memfree G (free)  " >> info.txt

#num= `ls -l .vim | grep -c ^d`

num=`find . -mindepth 1 -maxdepth 1 -type d | wc -l`
echo "num folders: $num" >> info.txt

num1=`find /etc -type f 2> /dev/null | wc -l`
echo "num files: $num1" >> info.txt