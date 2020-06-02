
from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('<int:blog_id>/',views.detail,name='detail'),
]
