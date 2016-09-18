# coding: utf-8
class AddressParser(object):
    """
    """


    def __init__(self, csw_model='ltp_models/cws.model', csw_dictionary='segmentor.txt', pos_model='ltp_models/pos.model', pos_dictionary='postagger.txt',parse_model='ltp_models/parser.model', token_address='token_address.txt', token_address_weak='token_address_weak.txt', token_address_remove='token_address_remove.txt'):

        from pyltp import Segmentor
        segmentor = Segmentor()  # 初始化实例
        segmentor.load_with_lexicon('ltp_models/cws.model','segmentor.txt')  # 加载模型
        from pyltp import Postagger
        postagger = Postagger() # 初始化实例
        postagger.load_with_lexicon('ltp_models/pos.model','postagger.txt')  # 加载模型
        from pyltp import Parser
        parser = Parser() # 初始化实例
        parser.load('ltp_models/parser.model')  # 加载模型

        import re
        regex = re.compile('\s*,\s*')
        with open('token_address.txt','r') as fp:
            token1_address = regex.split(fp.readline().strip('\n'))   
            token2_address = regex.split(fp.readline().strip('\n'))
        with open('token_address_weak.txt', 'r') as fp:
            token1_address_weak = regex.split(fp.readline().strip('\n'))   
            token2_address_weak = regex.split(fp.readline().strip('\n'))
        with open('token_address_remove.txt', 'r') as fp:
            token_address_remove = regex.split(fp.readline().strip('\n'))   

        self.segmentor = segmentor
        self.postagger = postagger
        self.parser = parser
        self.token1_address = token1_address
        self.token2_address = token2_address
        self.token1_address_weak = token1_address_weak
        self.token2_address_weak = token2_address_weak
        self.token_address_remove = token_address_remove

    def __call__(self, sentence):
        words, postags, arcs = self.parse_sentence(self.segmentor, self.postagger, self.parser, sentence)
        return self.address_extract(words, postags, arcs)


    def parse_sentence(self, segmentor, postagger, parser, sentence='北京市望京soho'):
        words = segmentor.segment(sentence)  # 分词
        #print '\t'.join(words)
        #segmentor.release()  # 释放模型
        postags = postagger.postag(words)  # 词性标注
        #print '\t'.join(postags)
        #postagger.release()  # 释放模型
        arcs = parser.parse(words, postags)  # 句法分析
        #print "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)
        #parser.release()  # 释放模型
        #print [x.relation for x in arcs]

        return words, postags, arcs


    def word_in(self, word, address):
        word_new = word.decode('utf-8')
        w = word_new[len(word_new)-1]
        for w_ in address:
            if w == w_.decode('utf-8'):
                return True
        return False


    def word_in_first(self, word):
        word_new = word.decode('utf-8')
        if word in ['道路', '原路'] or len(word_new) <= 1:
            return False
        w = word_new[len(word_new)-1]
        for w_ in ['路', '街']:
            if w == w_.decode('utf-8'):
                return True
        return False


    def address_extract(self, words, postags, arcs):
        """
        """
        address2 = self.token1_address
        word2_address = self.token2_address
        address = self.token1_address_weak
        word_address = self.token2_address_weak
        token_address_remove = self.token_address_remove
           
        
        temp = []
        solution = []
        for i in range(len(arcs)):
            if (temp != [] and i == len(arcs)-1 and arcs[i].relation not in ['WP'] and (postags[i] not in ['v', 'r'] or words[i] in ['弄'])) or (i == len(arcs)-1 and postags[i] in ['ni', 'ns', 'nl']) or (i == len(arcs)-1 and self.word_in_first(words[i])):
                temp.append(i)
                #print temp
                while len(temp) >=1 and not (words[temp[-1]] in address or self.word_in(words[temp[-1]], word_address)) and postags[temp[-1]] not in ['j', 'm', 'nd', 'ni', 'nl', 'ns', 'nz', 'ws', 'i', 'q'] and not (postags[temp[-1]] in ['n'] and temp[0] >=2 and words[temp[0]-2] in ['送'] and words[temp[0]-1] in ['到', '至']) and not (postags[temp[-1]] in ['n'] and temp[0] >=2 and words[temp[0]-2] in ['地址', '住']) and not (postags[temp[-1]] in ['n'] and temp[0] >=1 and words[temp[0]-1] in ['住']):
                    temp.pop()
                if len(temp) >= 1:
                    solution.append(temp)

          #      print solution
            elif (arcs[i].relation == 'ATT' and postags[i] not in ['p', 'r', 'q'] and words[i] not in ['大杯','超大杯','小杯']) or postags[i] in ['ns', 'ni', 'nl']:
                temp.append(i)
                #print temp
            elif temp != [] and (words[i] in address or self.word_in(words[i],word_address)):
                temp.append(i)
            elif self.word_in_first(words[i]):
                temp.append(i)
            elif temp != [] and postags[i] in ['m', 'ws']:
                temp.append(i)
            elif temp != []:   
                #print temp
                while len(temp) >=1 and not (words[temp[-1]] in address or self.word_in(words[temp[-1]], word_address)) and postags[temp[-1]] not in ['j', 'm', 'nd', 'ni', 'nl', 'ns', 'nz', 'ws', 'i', 'q'] and not (postags[temp[-1]] in ['n'] and temp[0] >=2 and words[temp[0]-2] in ['送'] and words[temp[0]-1] in ['到', '至']) and not (postags[temp[-1]] in ['n'] and temp[0] >=2 and words[temp[0]-2] in ['地址', '住']) and not (postags[temp[-1]] in ['n'] and temp[0] >=1 and words[temp[0]-1] in ['住']):
                    temp.pop()
                if len(temp) >= 1:
                    solution.append(temp)
                temp = []
            else:
                temp = []

        temp_solution = []
        for temp in solution:
            #print temp
            for idx in temp:
                if postags[idx] in ['ns', 'ni', 'nl'] or words[idx] in address or self.word_in(words[idx], word_address):
                    if len(temp_solution) >= 1 and (temp[0] - temp_solution[-1][-1] == 2) and words[temp[0]-1] in ['的', '与', '和']:
                        last_temp = temp_solution.pop()
                            
                        last_temp.append(temp[0]-1)
                        last_temp.extend(temp)
                        temp = last_temp
                    if arcs[temp[-1]].relation == 'VOB' and arcs[temp[-1]].head == temp[0] + 1:
                        del temp[0]
                        #print temp
                    for idx1 in temp:
                        if postags[idx1] in ['ns', 'ni', 'nl'] or words[idx1] in address2 or self.word_in(words[idx1], word2_address):
                            temp_solution.append(temp)
                            break
                    break
        #print temp_solution           
        final_solution = []
        for temp in temp_solution:
            final_solution.append(''.join(words[i] for i in temp))

        return final_solution



if __name__ == '__main__':
    from time import time
    start = time()
    import chardet
    address_parser = AddressParser()

    end = time()

    sentence = '我的地址是深南大道100002号32楼b707'
    solution = address_parser(sentence)

    end1 = time()
    for temp in solution:
        print(temp)
      
    print(end-start)
    print(end1-end)

