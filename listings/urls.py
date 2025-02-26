from django.urls import path  
from . import views  

urlpatterns = [
    path('', views.listings, name='listings'),   # using listings for empty string
    path('<int:listing_id>', views.listing, name='listing'),    # using listing for numbers
    path('search', views.search, name='search'),  
]