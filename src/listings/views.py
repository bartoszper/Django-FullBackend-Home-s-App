from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import price_choices, bedroom_choices, state_choices


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
    queryset_list = Listing.objects.order_by('-list_date')

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains =keywords)
            
    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list
    }
    return render(request, 'listings/search.html', context)