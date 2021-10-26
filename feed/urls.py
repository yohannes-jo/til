from django.urls import path
from .views import HomePage, PostDetail

app_name = 'feed'

urlpatterns = [
    path('', HomePage.as_view(), name="index"),
    path('<int:pk>/', PostDetail.as_view(), name="detail"),
]