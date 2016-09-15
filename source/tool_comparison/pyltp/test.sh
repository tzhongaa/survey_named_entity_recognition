START=`date +%s%N`;
python ltpout.py
END=`date +%s%N`;
time=$((END-START))
time=`expr $time / 1000000`
echo $time
