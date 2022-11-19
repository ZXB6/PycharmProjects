import jieba
from os import path  #用来获取文档的路径
from PIL import Image
import numpy as np,matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator #词云生成工具
import matplotlib.font_manager as fm #需要对中文进行处理

bg=np.array(Image.open("1.jpg")) # 背景图
d=path.dirname(__file__)
stopwords_path='stop_words.txt'  # 读取停用词表
# 添加需要自定以的分词
# jieba.add_word("xx")

text_path="红楼梦.txt"#读取要分析的文本
text=open(path.join(d,text_path),encoding="utf8").read()  #读取要分析的文本，读取格式
# 分词函数
def jiebaclearText(text):

    mywordList=[] #定义一个空的列表，将去除的停用词的分词保存
    seg_list=jieba.cut(text,cut_all=False)   #进行分词
    listStr='/'.join(seg_list)  #将一个generator的内容用/连接
    f_stop=open(stopwords_path,encoding="utf8")   #打开停用词表
    #读取
    try:
        f_stop_text=f_stop.read()
    finally:
        f_stop.close()#关闭资源
    #将停用词格式化，用\n分开，返回一个列表
    f_stop_seg_list=f_stop_text.split("\n")
    #对默认模式分词的进行遍历，去除停用词
    for myword in listStr.split('/'):
        #去除停用词
        if not(myword.split()) in f_stop_seg_list and len(myword.strip())>1:
            mywordList.append(myword)
    return ' '.join(mywordList)
text1=jiebaclearText(text)
#生成
wc=WordCloud( background_color="white",max_words=200,mask=bg,random_state=42,font_path='C:/Windows/Fonts/simkai.ttf'   #中文处理，用系统自带的字体
).generate(text1)
my_font=fm.FontProperties(fname='C:/Windows/Fonts/simkai.ttf') #为图片设置字体
#产生背景图片，基于彩色图像的颜色生成器
image_colors=ImageColorGenerator(bg)
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.figure()
plt.axis("off")
plt.imshow(bg,cmap=plt.cm.gray)

#保存云图
wc.to_file("finish.png")
