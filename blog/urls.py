from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('accounts/',include('accounts.urls')),
    path("articles/",include('article.urls')),
    path("contactus",include('contact.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)