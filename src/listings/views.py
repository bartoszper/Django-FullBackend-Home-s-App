from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    #Order by newset and filter by is published
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    #Pagination
    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'listings': page_obj
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):

    #if page doesnt exist show 404 error
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }

    return render(request, 'listings/listing.html', context)



def search(request):
    return render(request, 'listings/search.html')