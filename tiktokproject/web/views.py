from django.shortcuts import render
from tiktokproject import settings



# Create your views here.
def index(request):
    print(settings.COMPRESS_URL)
    context = {"base_dir":settings.BASE_DIR,"home_dir": settings.HOME_DIR, "rel_media": settings.rel_home('media'), "rel_static":settings.rel_home('media', 'static') }
    return render(request, 'index.html', context=context)

    
    