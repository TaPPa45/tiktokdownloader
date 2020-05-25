from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, Http404
import requests
import re

class GetVideoUrl(View):
    headers_content_url = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    headers_video_url = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'text/html; charset=utf-8',
        'Range': 'bytes=0-200000',
    }
    TIKTOK_URL_PATTERN = re.compile(r'^((https|http)://.+\.tiktok\.com\/@[a-zA-Z0-9]+/video/[\d]+)$')
    
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST' and self.TIKTOK_URL_PATTERN.match(request.body.decode('utf-8')):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponse("Видео не найдено проверьте ссылку", content_type="text/plain", status=400)
            
    
    def _get_content_url(self, url):
        response = requests.get(url, headers=self.headers_content_url)
        if re.search(r'"contentUrl":"', str(response.content)):
            return str(response.content).split('"contentUrl":"')[1].split('"')[0]
        else:
            return None

    def _get_video_id(self, content_url):
        response = requests.get(content_url, headers=self.headers_video_url)
        is_vid = re.search('\x76\x69\x64\x3a', str(response.content))
        if is_vid:
            vid_index = is_vid.span()[1] # поиск "vid:" в байтовом представлении, начальный индекс vid 
            vid_index_fin = vid_index + int(re.search(r'\\', str(response.content)[int(vid_index):]).span()[0]) # поиск конечного индекса vid
            return str(response.content)[int(vid_index):int(vid_index_fin)]
        return None

    def post(self, request, *args, **kwargs):
        content_url = self._get_content_url(request.body.decode('utf-8'))
        if content_url:
            video_id = self._get_video_id(content_url)
            if video_id:
                video_url = "https://api2.musical.ly/aweme/v1/playwm/?video_id=%s" %(video_id)
                return HttpResponse(video_url, content_type="text/plain", status=200)
        return HttpResponse("Видео не найдено проверьте ссылку", content_type="text/plain", status=400)







    

# Create your views here.
