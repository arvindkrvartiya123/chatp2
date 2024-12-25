from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'), #AboutPageView
    path("about/", AboutPageView.as_view(), name='about'), #AboutPageView
]
