#!/usr/bin/python
# coding: utf-8

import vkontakte

import json
import requests
import os
import random
import dircache


# Картинки в папке img, скрипт рандомно выбирает картинку из папки, постит ее на стену группы с текстом TTEXT и удаляет

IMGDIR = 'img/'

# Меняем VKAPPID VKKEY VKTOKEN GROUPID TTEXT на свои
VKAPPID = '*'
VKKEY = '*'
"""
get token by open url http://oauth.vk.com/authorize?client_id=VKAPPID&scope=wall,photos,groups,offline&redirect_uri=http://oauth.vk.com/blank.html&response_type=token
"""
VKTOKEN = '*'

GROUPID = *

TTEXT = u"""TEXT TO POST """



def getnewimg():
    dir= IMGDIR
    try:
        filename = random.choice(dircache.listdir(dir))
        path = os.path.join(dir, filename)
    except IndexError:
        raise IndexError("Something wrong with images")
    return path



def vkgrouppost(filename, text):
    vk = vkontakte.API(token=VKTOKEN)
    upurl = vk.get('photos.getWallUploadServer',gid=GROUPID)['upload_url']
    r = requests.post(upurl, files={'photo': open(filename, 'rb')}).json()
    ph = vk.get('photos.saveWallPhoto',server=r['server'],photo=r['photo'],hash=r['hash'],gid=GROUPID)
    attach = ph[0]['id']
    vk.get('wall.post',owner_id=0-GROUPID,message=text,attachments=attach,from_group=1)
    # пост запрос с полем photo содержащим файл с изображением
    # С помощью метода photos.saveWallPhoto приложение передает серверу
    # полученные данные (server, photo, hash и опциональные uid и gid) и
    # получает данные о загруженной фотографии.
    # метод wall.post и указав идентификатор фотографии в параметре attachment.
    # Обратите внимание, что при размещении фотографии на стене другого
    # пользователя или группы необходимо указывать параметры uid и gid,
    # соответствующие используемым в п.1.


def main():
    filename = getnewimg()
    text = TTEXT
    vkgrouppost(filename, text)
    os.remove(filename)

    
if __name__ == "__main__":
    main()
