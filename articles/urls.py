from django.urls import path
from . import views

urlpatterns = [
    path('',views.article_list, name='article_list'),

    path('<int:id>/', views.article_detail, name='article_detail'),
    path('detail/<int:id>/', views.article_update, name='article_update'),
    path('new/', views.article_new, name='article_new'),
    path('delete/<int:id>/', views.article_delete, name='article_delete'),
    path('article_confirm/<int:id>/',views.article_confirm_delete, name='article_confirm_delete'),
    
]