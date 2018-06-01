# -*- coding: utf-8 -*-
# Data: 17/10/9
# Brief:
from snownlp import SnowNLP
s = SnowNLP("我喜欢这油画")
print(s.words)
print(s.pinyin)
print(s.sentiments)

s = SnowNLP("我看了这油画半天，没看出什么有意思的内容")
print(s.words)
print(s.pinyin)
print(s.sentiments)

s = SnowNLP("我看了这油画半天，真是讨厌的背景")
print(s.words)
print(s.pinyin)
print(s.sentiments)

s = SnowNLP("我看了这油画半天，真是大爱的名作")
print(s.words)
print(s.pinyin)
print(s.sentiments)

print("*"*36)
s = SnowNLP("啊啊啊，要难吃死了。这土豆丝非常烂！")
print(s.words)
print(s.pinyin)
print(s.sentiments)

print("*"*36)
s = SnowNLP("这土豆丝非常美味！")
print(s.words)
print(s.pinyin)
print(s.sentiments)