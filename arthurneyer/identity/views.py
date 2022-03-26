from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import Portfolio
from arteablog.models import Article, Category

from greentea.artyp import ArtYp



# Create your views here.
@xframe_options_exempt
def home(request):

    ArtYp.save_ip(ArtYp.get_ip_with_django(request=request))

    portfolio = Portfolio.get_all_portfolios()
    portfolio.sort(reverse=True)

    articles = Article.objects.filter(online=True).order_by('-last_update_date')[:3]
    categories = Article.get_categories_from(articles)

    context = {
        'portfolio': portfolio,
        'articles': articles,
        'categories': categories if len(categories) > 0 else None,
    }

    return render(request, 'identity/home/index.html', context)


def privacy(request):

    context = {
    }

    return render(request, 'identity/legacy/privacy.html', context)
