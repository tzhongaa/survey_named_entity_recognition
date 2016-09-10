bosonnlp:
----------
    The performance is the best among these tools. It provides python API. The problem is that it is not free. We can only process 500 cases for free each day. The performance online can be checked in http://bosonnlp.com/demo

pyltp(python for ltp):
--------
    It is a free product named Language Technology Platform Cloud of Harbin Institute of Technology. It provides python API. The performance online can be checked in http://www.ltp-cloud.com/demo. 
    Although it is not good when using Named Entity Recognition if we want to find the address information, we can make use of part-of-speech tagging, semantic role labeling, dependency parsing to improve our results. 
    For example: We apply sematic role labeling or dependecy parsing to get one phrase or something. After that, we apply part-of-speech tagging or named entity recognition to see if there is a location part in this phrase. If it is, we decide that it is an address. Or we can use some patterns such as whether there are these words, say "大厦，室，号" to decide whether the phrase is an address.
