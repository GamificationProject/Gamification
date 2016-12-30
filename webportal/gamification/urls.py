from django.conf.urls import url

from . import views

app_name = "gamification"
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = "index"),
    url(r'^$', views.IndexView.as_view(), name = "register"),
    url(r'^$', views.IndexView.as_view(), name = "login"),
]