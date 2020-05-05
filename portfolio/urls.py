
from django.contrib import admin
from django.urls import path

from django.conf import settings # importing the settings.py file
from django.conf.urls.static import static

import jobs.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home ,name = 'home'),
    path('/blog',blog.views.main, name = 'main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
