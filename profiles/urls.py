from django.urls import path

from . import views

app_name = 'profiles'

urlpattterns = [
    path("<str:username>/", views.ProfileDetail.as_view(), name="detail"),
]