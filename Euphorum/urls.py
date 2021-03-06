from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from homepage import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^homepage/', include('homepage.urls')),
    url(r'^', include('homepage.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
