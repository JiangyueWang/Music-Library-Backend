from django.urls import path
from songs import views

urlpatterns = [
    path('', views.songs_list),
    # <int: pk> force the pk can only accept integer value
    path('<int:pk>/', views.song_detail),
]
