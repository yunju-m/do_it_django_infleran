from . import views
from django.urls import path


urlpatterns = [
    path('', views.landing),
    path('about_me/', views.about_me),
]
