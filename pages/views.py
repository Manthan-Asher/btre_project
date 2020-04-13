from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtors
from listings.choices import state_choices,bedroom_choices,price_choices
# Create your views here.
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices
    }
    return render(request,'pages/index.html',context)

def about(request):
    realtors=Realtors.objects.order_by('-hire_date')
    #get MVP
    mvp_realtors=Realtors.objects.all().filter(is_mvp=True)
    context1={
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request,'pages/about.html',context1)