from django.shortcuts import render
from .models import Seller


def seller_info(request):
    seller = Seller.objects.first()

    # Pasa el nombre del vendedor al template
    return render(request, 'seller.html', {'seller': seller})