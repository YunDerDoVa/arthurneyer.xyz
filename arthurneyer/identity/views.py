from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import Portfolio

from greentea.artyp import ArtYp



# Create your views here.
@xframe_options_exempt
def home(request):

    ArtYp.save_ip(ArtYp.get_ip_with_django(request=request))

    portfolio = Portfolio.get_all_portfolios()
    portfolio.sort()

    context = {
        'portfolio': portfolio,
    }

    return render(request, 'identity/home/index.html', context)
