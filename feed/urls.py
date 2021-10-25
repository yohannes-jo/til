from django.urls import path
from .views import HomePage

app_name = 'feed'

urlpatterns = [
    path('', HomePage.as_view(), name="index"),
]