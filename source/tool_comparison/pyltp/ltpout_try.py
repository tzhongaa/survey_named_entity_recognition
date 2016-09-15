# coding: utf-8


from time import time
start = time()
def load_model():
    from pyltp import Segmentor
    segmentor = Segmentor()  # 初始化实例
    segmentor.load_with_lexicon('ltp_models/cws.model','segmentor.txt')  # 加载模型
    from pyltp import Postagger
    postagger = Postagger() # 初始化实例
    postagger.load_with_lexicon('ltp_models/pos.model','postagger.txt')  # 加载模型
    from pyltp import Parser
    parser = Parser() # 初始化实例
    parser.load('ltp_models/parser.model')  # 加载模型
end = time()

def sentence_parse():
    words = segmentor.segment('我家的地址是福田区老佛街108号，记住了哈！')  # 分词
    print '\t'.join(words)
    #segmentor.release()  # 释放模型
    postags = postagger.postag(words)  # 词性标注
    end2 = time()
    print '\t'.join(postags)
    #postagger.release()  # 释放模型
    arcs = parser.parse(words, postags)  # 句法分析
    #print [x.relation for x in arcs]
    #parser.release()  # 释放模型
    return words, postags, arcs



import chardet
def word_in(word, address):
    word_new = word.decode('utf-8')
    w = word_new[len(word_new)-1]
    for w_ in address:
        if w == w_.decode('utf-8'):
            return True
    return False


def process(words, postags, arcs)
    address = ['大厦', '大学','中学','小学','科技园','广场', '公园', '酒店', '花园', '中心', '单元', '公司', '研究院', '公寓', '店铺']
    word_address = ['省','市','县','乡','区', '镇','街','路', '栋','座','层','楼','室', '弄', '店']
# In[61]:
    word_remove = ['时']
    temp = []
    solution = []
    final_solution = []
    
    for i in range(len(arcs)):
        if temp != [] and i == len(arcs)-1 and arcs[i].relation not in ['WP'] and postags[i] not in ['v', 'r']:
            temp.append(i)
            if words[len(temp)-1] in word_remove:
                del temp[len(temp)-1]
                if len(temp) !=0 and postags[temp[0]] not in ['nz', 'n', 'ns', 'nd', 'nh', 'ni', 'nl']:
                    del temp[0]
            solution.append(temp)
            print solution
        elif (arcs[i].relation == 'ATT' and postags[i] not in ['p', 'r']) or postags[i] in ['ns', 'ni']:
            temp.append(i)
        elif temp != [] and (words[i] in address or word_in(words[i],word_address)):
            temp.append(i)
        elif temp != [] and postags[i] in ['m', 'ws']:
            temp.append(i)
        elif temp != []:   
            if postags[i] in ['nz', 'n', 'ns', 'nd', 'nh', 'ni', 'nl'] or words[i] in ['号']:
                temp.append(i)
            if words[temp[len(temp)-1]] in word_remove:
                del temp[len(temp)-1]
                if len(temp) !=0 and postags[temp[0]] not in ['nz', 'n', 'ns', 'nd', 'nh', 'ni', 'nl']:
                    del temp[0]
            solution.append(temp)
            temp = []
        else:
            temp = []

    for temp in solution:
        #print temp
        for idx in temp:
            if postags[idx] == 'ns' or words[idx] in address or word_in(words[idx], word_address):
                final_solution.append(temp)
                break

# In[64]:
end4 = time()
for temp in final_solution:
    print ''.join(words[i] for i in temp)

print(end-start)
print(end1-end)
print(end2-end1)
print(end3-end2)
print(end4-end3)
## In[ ]:
#
#
#
