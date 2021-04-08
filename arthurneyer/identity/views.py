from django.shortcuts import render

from .models import Portfolio


# Create your views here.
def home(request):

    portfolio = Portfolio.get_all_portfolios()
    portfolio.sort()

    context = {
        'portfolio': portfolio,
    }

    return render(request, 'identity/home/index.html', context)
