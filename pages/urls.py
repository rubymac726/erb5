from django.urls import path  # from module import function
from . import views   # from current folder import file
urlpatterns = [
    path('', views.index, name='index'),    # run index in views.py
    path('about', views.about, name='about'),   # run about in views.py
]
