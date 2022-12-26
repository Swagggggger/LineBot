import os
import requests
import re
import pandas as pd
import json

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackAction,URIAction, MessageAction, TemplateSendMessage, MessageTemplateAction, ButtonsTemplate, ImageSendMessage, ImageCarouselTemplate
from bs4 import BeautifulSoup


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_movie_info(reply_token, userid):
    # 搜尋目前上映那些電影，擷取出其資訊
    url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    movie_html = soup.find_all("div", "release_info_text")

    #先宣告兩個list放電影名稱跟電影英文
    name_list = []
    english_name_list = []
    result = ""
    counter = 0
    #因為movie_html 是一個bs4的元素集合，我們要用遍歷去探索它:
    for item in movie_html:
        name = item.find("div","release_movie_name").a.text.strip()
        name_list.append(name)
        english_name = item.find("div","en").a.text.strip()
        english_name_list.append(english_name)

    result +=('本週電影\n')
    for i in name_list:
        result += ("{}:{}\n" .format(counter, name_list[counter]))
        counter = counter+1
    result += ('\nFilms this week\n')
    counter=0
    for i in english_name_list:
        result += ("{}:{}\n" .format(counter, english_name_list[counter]))
        counter = counter+1
    
    send_text_message(reply_token, result)
    
    return "OK"
    
def send_movie_detail(reply_token, userid, movie_num):
    # 搜尋目前上映那些電影，擷取出其資訊
    url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    movie_html = soup.find_all("div", "release_info_text")

    #先宣告兩個list放電影名稱跟電影英文
    name_list = []
    english_name_list = []
    intro_list = []
    rate_list = []
    result = ""
    counter = 0
    #因為movie_html 是一個bs4的元素集合，我們要用遍歷去探索它:
    for item in movie_html:
        name = item.find("div","release_movie_name").a.text.strip()
        name_list.append(name)
        english_name = item.find("div","en").a.text.strip()
        english_name_list.append(english_name)
        intro = item.find("div","release_text").span.text.strip()
        intro_list.append(intro)
        try:  
            rate = item.find('div', 'leveltext').span.text.strip()
            rate_list.append(rate)
        except: 
            rate_list.append("None")
        
    result=""
    result += ("{}({}):\n{}\n" .format(name_list[movie_num], english_name_list[movie_num], intro_list[movie_num]))
    result += ("\n\n期待度(Expectation):{}" .format(rate_list[movie_num]))
    send_text_message(reply_token, result)
    
    return "OK"

def send_movie_rank(reply_token, userid):    
    # 搜尋目前上映那些電影，擷取出其資訊
    url = 'https://movies.yahoo.com.tw/chart.html'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    movie_html = soup.find_all("div", "tr")

    #先宣告兩個list放電影名稱跟連結
    name_list = []
    url_list = []
    result = ""
    counter = 1
    #因為movie_html 是一個bs4的元素集合，我們要用遍歷去探索它:
    for item in movie_html:
        if counter==1:
            counter = counter + 1
            continue
        elif counter==2:
            name = item.find("dl","rank_list_box").dd.h2.text.strip()
            name_list.append(name)
            url = item.select_one("a").get("href")
            url_list.append(url)
            counter = counter + 1
        else:
            item1 = item.find_all("div","td")
            for item2 in item1:
                item3 = item2.find("a")
                if item3 != None:
                    name = item3.find("div").text.strip()
                    name_list.append(name)
                    break
                    
            try:
                url = item.select_one("a").get("href")
                url_list.append(url)
            except:
                url = None
                url_list.append(url)
    #make result
    counter = 1
    for i in name_list:
        result += ("{}.{}\n{}\n" .format(counter, name_list[counter-1], url_list[counter-1])) 
        counter = counter + 1
    send_text_message(reply_token, result)
    
    return "OK"

def send_movie_theaterarea(reply_token, userid):
    # 搜尋目前上映那些電影，擷取出其資訊
    url = 'https://movies.yahoo.com.tw/theater_list.html'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    movie_html = soup.find_all("div", "theater_content")

    #先宣告兩個list放地區名稱跟區域ID
    area_list = []
    areaID_list = []
    result = ""
    counter = 0
    #因為movie_html 是一個bs4的元素集合，我們要用遍歷去探索它:
    for item in movie_html:
        area = item.find("div","theater_top").text.strip()
        area_list.append(area)
        areaID = item.get("data-area")
        areaID_list.append(areaID)

    for i in area_list:
        try:
            result += ("放映地區：{}  areaID:{}\n" .format(area_list[counter], areaID_list[counter]))
            counter+=1
        except:
            break

    send_text_message(reply_token, result)
    
    return "OK"

def send_movie_theater(reply_token, userid, area_num):
    # 搜尋目前上映那些電影，擷取出其資訊
    url = 'https://movies.yahoo.com.tw/theater_list.html'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    movie_html = soup.find_all("div", "theater_content")
    
    #先宣告兩個list影廳名稱和連結
    theater_list = []
    url_list = []
    result = ""
    counter=0
    #因為movie_html 是一個bs4的元素集合，我們要用遍歷去探索它:
    for item in movie_html:
        if item.get("data-area") == area_num:
            item1 = item.find_all("div", "name")
            for item2 in item1:
                theater = item2.a.text.strip()
                theater_list.append(theater)
                url = item2.select_one("a").get("href")
                url_list.append(url)
            break
        else:
            continue

    for i in theater_list:
        result += ("{}\n{}\n" .format(theater_list[counter], url_list[counter]))
        counter+=1
        
    send_text_message(reply_token, result)
    
    return "OK"

def send_button_message(id, img, title, uptext, labels, texts):
    acts = []
    for i, lab in enumerate(labels):
        acts.append(
            MessageTemplateAction(
                label=lab,
                text=texts[i]
            )
        )

    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url=img,
            title=title,
            text=uptext,
            actions=acts
        )
    )
    line_bot_api.push_message(id, message)
    
    return "OK"

def send_image_carousel(id, imglinks, labels, texts):
    cols = []
    for i, url in enumerate(imglinks):
        cols.append(
            ImageCarouselColumn(
                image_url=url,
                action=MessageTemplateAction(
                    label=labels[i],
                    text=texts[i]
                )
            )
        )
    message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(columns=cols)
    )
    line_bot_api.push_message(id, message)
    return "OK"

def push_message(userid, msg):
    line_bot_api.push_message(userid, TextSendMessage(text=msg))
    return "OK"

def send_image_url(reply_token, img_url):
    message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

