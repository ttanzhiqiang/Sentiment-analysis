# Sentiment-analysis



# 中文单句的情感极性判断

使用python开发，第三方库有：spa，pypinyin，jieba

有下列功能，可以在demon中测试：
> 分类器
  * 朴素贝叶斯(NB)
  * K最近邻(KNN)
  * 支持向量机(SVM)
  * 最大熵(MaxEnt)
  * 情感词典
>  评估
  * 准确率
  * 召回率
  * F值
  * 训练、测试时间
  * 结果输出
>  统计检验
  * 卡方检验(Chi-square test)

代码说明：

* 在demon中修改文件测试各项功能，例如执行demon\_dict是使用情感词典来分析文本，而demon\_waimai则是读取语料库当中的数据，然后调取KNN，bayes或者svm等方法来进行评估，在控制台下查看结果
* data文件夹下，dict是整理的情感词典，corpus下是语料库，out是程序输出数据记录
* classifier文件夹下是各个分类器的实现方式
* 

简单的情感分析


![](https://github.com/ttanzhiqiang/Sentiment-analysis/blob/master/1.png)

可以看出高兴的和不高兴得到的评分是不一样的

在0.80之上可以判断为高兴

0.70以下可以判断为不高兴
