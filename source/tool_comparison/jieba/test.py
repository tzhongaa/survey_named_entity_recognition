#encoding=utf-8
from time import time
start = time()
import jieba.posseg as pseg
#jieba.enable_parallel()
end = time()
words = pseg.cut("老街3899弄105号202室")
end1 = time()
for word, flag in words:
    print('%s %s' % (word, flag))

print(end-start)
print(end1-end)
