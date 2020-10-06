from selenium import webdriver
import time
import requests as req
from bs4 import BeautifulSoup
import re
import os
import cv2
import numpy as np


def img_process(img_path, tags):
    w_font, h_font = 22, 15
    alpha = 0.3
    img = cv2.imread(img_path)
    w_img, h_img = (img.shape[1]*7, img.shape[0]*7)
    img = cv2.resize(
        img, (w_img, h_img), interpolation=cv2.INTER_CUBIC)
    len_tags = len(tags)
    font_pos = (int(w_img/2)-int(len_tags/2*w_font/2),
                int(h_img/2)+int(h_font/2))

    cv2.rectangle(img, (font_pos[0], font_pos[1]-h_font-5),
                  (int(font_pos[0]+len_tags*w_font/2)+30, font_pos[1]+5), (255, 255, 255), -1)
    # for correction
    # cv2.circle(img, (int(w_img/2), int(h_img/2)), 2, (0, 255, 0), -1)
    cv2.putText(img, tags, font_pos,
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1, cv2.LINE_AA)


    cv2.imwrite(img_path, img)


def get_img(html):
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find(attrs={'id': 'ConcurrentUsersRows'})
    games = table.find_all('a')

    for g in games:
        img_url = g.find('img').get('src')
        name = g.find(attrs={'class': 'tab_item_name'}).text
        non_chinese = re.sub('[\u4E00-\u9FFF]+','?', name)

        file_name = re.sub('^_|_$', '', re.sub('\W+', '_', non_chinese))
        path_name = os.path.join('./img/steam', f'{file_name}.png')
        print('--------------------------------')
        print(file_name)

        r_img = req.get(img_url, stream=True)
        if r_img.status_code == 200:
            with open(path_name, 'wb') as f:
                for chunk in r_img:
                    f.write(chunk)

        tags = g.find(attrs={'class': 'tab_item_top_tags'}).text
        img_process(path_name, tags)


def main():
    browser = webdriver.Firefox()
    browser.get('https://store.steampowered.com/')
    # browser.maximize_window()


    browser.find_element_by_id('language_pulldown').click()
    time.sleep(1)
    browser.find_element_by_link_text('English（英文）').click()
    time.sleep(2)
    browser.find_element_by_link_text('Free to Play').click()
    browser.find_element_by_id('tab_select_ConcurrentUsers').click()


    for _ in range(4):
        html = browser.page_source
        get_img(html)

        browser.find_element_by_id('ConcurrentUsers_btn_next').click()
        time.sleep(3)
    html = browser.page_source
    get_img(html)

    time.sleep(1)
    browser.quit()


if __name__ == "__main__":
    if not os.path.exists('.\img\steam'):
        os.mkdir('.\img\steam')
    main()
