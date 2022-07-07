from django.urls import path
from . import views

app_name = 'instagramm'

urlpatterns = [
    path('<user_name>', views.user, name='user'),
    path('<user_name>/edit', views.user_edit, name='user'),
    path('index/', views.index, name='index'),
    path('', views.main, name='main'),
]
