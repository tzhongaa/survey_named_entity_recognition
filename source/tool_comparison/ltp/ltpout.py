
# coding: utf-8

# In[57]:

from time import time
start = time()
from pyltp import Segmentor
segmentor = Segmentor()  # 初始化实例
segmentor.load('ltp_models/cws.model')  # 加载模型
words = segmentor.segment('我家的地址是福田区老佛街108号，记住了哈！')  # 分词
#print '\t'.join(words)
#segmentor.release()  # 释放模型


# In[58]:


from pyltp import Postagger
postagger = Postagger() # 初始化实例
postagger.load('ltp_models/pos.model')  # 加载模型
postags = postagger.postag(words)  # 词性标注
end = time()
print(end-start)
##print '\t'.join(postags)
##postagger.release()  # 释放模型
#
#
## In[59]:
#
#
from pyltp import Parser
parser = Parser() # 初始化实例
parser.load('ltp_models/parser.model')  # 加载模型
arcs = parser.parse(words, postags)  # 句法分析
#print "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)
#parser.release()  # 释放模型
#print arcs


# In[60]:

#[x.relation for x in arcs]


# In[61]:

temp = []
solution = []
for i in range(len(arcs)):
    if arcs[i].relation == 'ATT':
        temp.append(i)
    elif temp != []:
        solution.append(temp)
        temp = []
    else:
        temp = []

        


# In[62]:

address = ['大厦']


# In[63]:

final_solution = []
for temp in solution:
    #print temp
    for idx in temp:
        if postags[idx] == 'ns' or words[idx] in address:
            #print 'yes'
            final_solution.append(temp)
            break


# In[64]:
end2 = time()
for temp in final_solution:
    print ''.join(words[i] for i in temp)

print(end2-start)
# In[ ]:



