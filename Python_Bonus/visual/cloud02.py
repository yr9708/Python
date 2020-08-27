# -*- coding:utf-8 -*-

from wordcloud import WordCloud
from PIL import Image
import numpy as np
# import matplotlib.pyplot as plt
import json


kakao_mask = np.array(Image.open("kakao.png"))

wordcloud = WordCloud(
    font_path ='Goyang.ttf',
    width = 800,
    height = 800,
    background_color="black",
    mask = kakao_mask
)


with open('webtoons.json', encoding='utf-8') as file:
    webtoon = json.load(file)
    
res = dict()
for webtoon in webtoon['webtoons']:
    res[webtoon['title']] = int(float(webtoon['star'])*100)
    
visual = wordcloud.fit_words(res)
visual.to_image()
visual.to_file('kakaocloud.png')

print('완료')
