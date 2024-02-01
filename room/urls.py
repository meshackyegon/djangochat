from django.urls import path

from . import views

urlpatterns = [
    # path('', views.rooms, name='rooms'),
    # path('user_id/<user_id>/', views.room, name='room'),
    # path('messages/',views.messages,name='messages'),
]

# messaging/urls.py
from django.urls import path
from .views import receive_message, agent_portal, view_message, respond_to_message

urlpatterns = [
    path('receive_message/', receive_message, name='receive_message'),
    path('', agent_portal, name='agent_portal'),
    path('view_message/<int:user_id>/', view_message, name='view_message'),
    path('respond_to_message/<int:user_id>/', respond_to_message, name='respond_to_message'),
]
