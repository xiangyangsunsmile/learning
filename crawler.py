# -*- coding: utf-8 -*-
'''
author: yang
date:   2015/8/13
description:   爬虫
params:
    url_queue:       存放尚未爬取的url的队列
    url_set ：       存放已爬取的url的集合
    url_name ：      网站根目录
    short_html：     html正则表达式
    short_css：      css正则表达式
    short_js：       js正则表达式
    short_jpg：      jpg正则表达式
    short_png:       png正则表达式
    NameList = []:   存放可爬取的url的列表
    WrongNameList = []：存放产生异常的url的列表
'''
import Queue
import urllib2
import re
import threading
import time
import string
import os
import pdb
url_queue = Queue.Queue(0)
url_set = set()
url_name = "http://www.xxxx.edu.cn/"
short_html = ".*xxxx.*"
short_css = ".*xxxx.*.css"
short_js = ".*xxxx.*.js"
short_jpg = ".*xxxx.*.jpg"
short_png = ".*xxxx.*.png"
url_short = re.compile(short_html)
css_short = re.compile(short_css)
js_short = re.compile(short_js)
jpg_short = re.compile(short_jpg)
png_short = re.compile(short_png)
NameList = []
WrongNameList = []
class url_get:
    def __init__(self):
        url_queue.put("http://www.xxxx.edu.cn",0.5);
        i = 0
    def run(self):
        cas = 0
        j=0
        while(url_queue.empty() == False):
            j=j+1
            print "j=="+str(j), "len of queue:",url_queue.qsize()
            if url_queue.empty() == True :
                print u"finish"
            else :
                self.recent_url = url_queue.get(0.5)    #操作的url
                if self.recent_url not in url_set :     #该url还未被爬取过
                    url_set.add(self.recent_url)        #在爬取之前先添加到以集合url_set里
                    try :
                        url_need = urllib2.urlopen(self.recent_url).read()  #爬取网页
                    except :
                        WrongNameList.append(self.recent_url)   #打不开的时候进行处理，防止程序不正常结束
                    url_list = re.findall('"((http|ftp)s?://.*?)"', url_need)   #正则表达式，找出网页里面的所有链接
                    #url_list_second = re.findall('<a.*?href="([^"]*)".*?>([\S\s]*?)</a>', url_need) 
                    if re.match(css_short,self.recent_url) :
                        sName = string.zfill(cas,4)+'.css'
                    elif re.match(js_short,self.recent_url) :
                        sName = string.zfill(cas,4)+'.js'
                    elif re.match(jpg_short,self.recent_url) :
                        continue
                    elif re.match(png_short,self.recent_url) :
                        continue 
                    else :
                        sName = string.zfill(cas,4)+'.html'
                    url_text = open(sName,"w+")
                    url_text.write(url_need)    #爬取recent_url网页的内容写到文件里面
                    url_text.close()
                    NameList.append(sName + self.recent_url)
                    n=0
                    for url_pos in url_list:#该网页的所有url
                        n=n+1
                        print"n="+str(n)+url_pos[0]
                        if re.match(url_short,url_pos[0]) != None :
                            url_queue.put(url_pos[0])
                            print"   n="+str(n)+url_pos[0]
                        #print url_pos[0]
                    cas = cas + 1
                    #print cas
                    #print "--------------------"

if __name__ == '__main__':
    quest = url_get()
    quest.run()
    RightName = open("RightName.txt","w+")
    for item in NameList :
         RightName.write(item)
         RightName.write("\n")
    RightName.close()

    WrongName = open("WrongName.txt","w+")
    for item in WrongNameList :
         WrongName.write(item)
         WrongName.write("\n")
    WrongName.close()
