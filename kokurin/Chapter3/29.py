import re
import requests
import json
Template={}
count=[]

pattern = re.compile(r'^\{\{基礎情報(.*?)\}\}$',re.MULTILINE + re.DOTALL)#元字符“.”在默认模式下，匹配除换行符外的所有字符。在DOTALL模式下，匹配所有字符，包括换行符

wikipedia_api = "http://ja.wikipedia.org/w/api.php?"
prop = {
    'action': "query",
    'prop': "imageinfo",
    'iiprop': "url",
    'format': "json",
    'formatversion': '2',
    'utf8': '',
    'continue': ''
}

with open('uk.txt','r') as f:
    Template_content=pattern.search(f.read())#找到基础情报里面的内容
    target_Template=Template_content.group(1).split('\n')
    for line in target_Template:
        if re.search(r'国旗画像',line):
            key=re.findall(r'.*\=\s?(.*)',line)
            prop['titles'] = "Image:" + key[0]#向wiki发送资料请求
            reqs = requests.get(url=wikipedia_api, params=prop)#请求格式
            reqs_txt = json.loads(reqs.text)#将获取的文件转换为可读模式
            print(reqs_txt['query']['pages'][0]['imageinfo'][0]['url'])#需要学习这部分