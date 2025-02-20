
# Create your views here.

from django.shortcuts import render
from .models import Provider

def provider_list(request):
    providers = Provider.objects.all()
    # Hardcoded data for testing
    # providers = [
    #     {
    #         'name': 'Test Provider 1',
    #         'standard_crayon_price': 10.00,
    #         'premium_crayon_price': 15.00,
    #         'eco_friendly_crayon_price': 20.00,
    #         'offers_bulk_discount': True,
    #     },
    #     {
    #         'name': 'Test Provider 2',
    #         'standard_crayon_price': 5.00,
    #         'premium_crayon_price': 8.00,
    #         'eco_friendly_crayon_price': None,
    #         'offers_bulk_discount': False,
    #     },
    # ]

    print(providers) 
    
    return render(request, 'providers/provider_list.html', {'providers': providers})