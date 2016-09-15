START=`date +%s%N`;
./ltp-3.3.2/bin/examples/cws_cmdline --input input --threads 4 | ./ltp-3.3.2/bin/examples/pos_cmdline --threads 4  | ./ltp-3.3.2/bin/examples/par_cmdline --threads 4 
END=`date +%s%N`;
time=$((END-START))
time=`expr $time / 1000000`
echo $time
