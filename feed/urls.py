from django.urls import path
from .views import HomePage, PostDetail, CreateNewPost

app_name = 'feed'

urlpatterns = [
    path('', HomePage.as_view(), name="index"),
    path('<int:pk>/', PostDetail.as_view(), name="detail"),
    path('new', CreateNewPost.as_view(), name="new_post"),
]