from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('', lambda request: HttpResponseRedirect('/home/'))
]

urlpatterns += static('favicon.ico', document_root=settings.STATIC_ROOT)
