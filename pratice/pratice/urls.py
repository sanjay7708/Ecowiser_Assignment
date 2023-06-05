from django.urls import path
from new import views

urlpatterns = [
    path('upload/', views.upload_video, name='upload_video'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('search/', views.search, name='search'),
]
