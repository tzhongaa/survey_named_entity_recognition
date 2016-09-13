
# coding: utf-8

# In[1]:

from __future__ import print_function, unicode_literals
from time import time
start = time()
from bosonnlp import BosonNLP
import os
nlp = BosonNLP('ZoNGiZCV.9409.1Cz-WJBQHKEi')
s=['我想预订一杯咖啡，请把它送到腾讯大厦A栋101室']
result = nlp.ner(s)[0]
words = result['word']
entities = result['entity']
for entity in entities:
    print(''.join(words[entity[0]:entity[1]]), entity[2])
end = time()
print(end-start)


# In[ ]:




# In[ ]:



