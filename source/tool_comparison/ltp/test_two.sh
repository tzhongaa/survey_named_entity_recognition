START=`date +%s%N`;
./ltp-3.3.2/bin/ltp_test --last-stage dp --input input --threads 4
END=`date +%s%N`;
time=$((END-START))
time=`expr $time / 1000000`
echo $time
