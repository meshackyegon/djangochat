from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('user_id/<user_id>/', views.room, name='room'),
    path('messages/',views.messages,name='messages'),
]