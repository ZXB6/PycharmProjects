import jieba
def wordFreq(text_path,text,topn):
    words=jieba.lcut(text.strip())
    counts={}
    for word in words:
        if len(word) == 1:
            continue
        counts[word]=counts.get(word,0)+1
    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
    f=open(text_path[:-4]+'_词频.txt',"w")
    for i in range(topn):
        word,count=items[i]
        f.write("{}\t\{}\n".format(word,count))
    f.close()

def stowordslist(text_path):
    stopwords = [line.strip() for line in open(text_path,'r',encoding='utf-8').readlines()]
    return stopwords

text_path = "红楼梦.txt"
text = open(text_path,"r",encoding='utf-8').read()
t = wordFreq(text_path,text,10)
