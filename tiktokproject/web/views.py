from django.shortcuts import render
from tiktokproject import settings



# Create your views here.
def index(request):
    # context = {"base_dir":settings.BASE_DIR,"home_dir": settings.HOME_DIR, "rel_media": settings.rel_home('media'), "rel_static":settings.rel_home('media', 'static') }
    # -*- coding: utf-8 -*-
    import requests
    import urllib3
    import zlib


    url = 'https://www.tiktok.com/@glistt/video/6824126764885757189'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    r = requests.get(url, headers=headers)

    content = str(r.content).split('"contentUrl":"')
    content_url = content[1].split('"')[0]



    headers2 = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'text/html; charset=utf-8',
        'Range': 'bytes=0-200000',
    }

    rr = requests.get(content_url, headers=headers2)
    rr.encoding = 'utf-8'
    import re

    print(re.search('\x76\x69\x64\x3a', str(rr.content)).span())
    vid_index = re.search('\x76\x69\x64\x3a', str(rr.content)).span()[1]

    vid_index_fin = re.search(r'\\', str(rr.content)[int(vid_index):]).span()[0]
    print(vid_index_fin)
    print(str(rr.content)[int(vid_index):int(vid_index+vid_index_fin)])
    
    
    return render(request, 'index.html', context={})

    
    