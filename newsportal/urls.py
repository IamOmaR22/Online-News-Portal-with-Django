from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from django.urls import path

urlpatterns = [
    
    url(r'^admin/' , admin.site.urls),
    url(r'', include('main.urls')),         # here main is an app name
    url(r'', include('news.urls')),         # here news is an app name
    url(r'', include('cat.urls')),          # here cat is an app name
    url(r'', include('subcat.urls')),       # here subcat is an app name
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)