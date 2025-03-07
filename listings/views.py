from django.shortcuts import render, get_object_or_404
from . models import Listing   # add "." to find the model under the same apps
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def listings(request):
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
    return render(request, 'listings/search.html')