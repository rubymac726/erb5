from django.shortcuts import render, get_object_or_404
from . models import Listing   # add "." to find the model under the same apps
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F   # to import the Q and F objects from django
from listings.choices import price_choices, bedroom_choices, district_choices

# Create your views here.

def listings(request):
    # listings = Listing.objects.filter(Q(district='tst') | ~Q(district='mk'))   # Q object 
    # listings = Listing.objects.filter(district=F('address'))   # F object  
    # listings = Listing.objects.all()    # Listing is the databse, use "listings" to hold all the variable from database
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)  # lastest listing is on top, only show the listing with "is_published"
    paginator = Paginator(listings, 3)  # Allocate 3 listings as a group
    page = request.GET.get('page')      # GET is method and get is function, page holds the variables of the number of page
    paged_listings = paginator.get_page(page) # paged_listings holds the variables of the page with 3 listings
    context = {'listings' : paged_listings}   # context holds the variables of paged_listings in a dictionary 
    return render(request, 'listings/listings.html', context)  # pass the dictionary to template engine, render is used to combine the data and the template

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing' : listing}
    return render(request, 'listings/listing.html',context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__icontains=title)
    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            queryset_list = queryset_list.filter(district__iexact=district) 
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)                      
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
  
    paginator = Paginator(queryset_list, 3)  # Allocate 3 listings as a group
    page = request.GET.get('page')      # GET is method and get is function, page holds the variables of the number of page
    paged_listings = paginator.get_page(page) # paged_listings holds the variables of the page with 3 listings
    values = request.GET.copy()
    if 'page' in values:
        del values["page"]

    context = {'price_choices' : price_choices,
               'bedroom_choices' : bedroom_choices,
               'district_choices' : district_choices,
               'listings' : paged_listings,
               'values' : request.GET,
    }
    return render(request, 'listings/search.html',context)