from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path("About", views.about, name="About"),
    # path("login", views.login, name="login"),
    # path("livechat", views.livechat, name="livechat"),
]
