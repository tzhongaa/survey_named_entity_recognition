TART=`date +%s%N`;
python test.py
END=`date +%s%N`;
time=$((END-START))
time=`expr $time / 1000000`
echo $time
