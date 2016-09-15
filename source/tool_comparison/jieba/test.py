#encoding=utf-8
from time import time
start = time()
import jieba
#jieba.enable_parallel()
end = time()
seg_list = jieba.cut("我家的地址是福田区老佛街108号，记住了哈！")
end1 = time()
print(" ".join(seg_list))
print(end-start)
print(end1-end)
