./NiuParser-v1.3.0-mt-linux --WS -c niuparser.config -in try.utf8 -out ws.out
./NiuParser-v1.3.0-mt-linux --POS -c niuparser.config -in ws.out -out pos.out
./NiuParser-v1.3.0-mt-linux --NER -c niuparser.config -in pos.out -out ner.out
#./NiuParser-v1.3.0-mt-linux --CHK -c niuparser.config -in pos.out -out chk.out
#./NiuParser-v1.3.0-mt-linux --CP -c niuparser.config -in pos.out -out cp.out
#./NiuParser-v1.3.0-mt-linux --DP -c niuparser.config -in pos.out -out dp.out
#./NiuParser-v1.3.0-mt-linux --SRL -c niuparser.config -in cp.out -out srl.out
