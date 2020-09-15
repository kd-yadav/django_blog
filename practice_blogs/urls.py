from django.urls import path
from . import views

app_name = 'practice_blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('titles/', views.titles, name='titles'),
    path('titles/<int:title_id>/', views.title, name='title'),
    path('new_title/', views.new_title, name='new_title'),
    path('new_text/<int:title_id>/', views.new_text, name='new_text'),
    path('edit_text/<int:tx_id>/', views.edit_text, name='edit_text'),
]