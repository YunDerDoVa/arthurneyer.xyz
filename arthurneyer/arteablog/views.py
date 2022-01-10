from django.shortcuts import render

from .models import Article


# Create your views here.
def blog(request):

    articles = Article.objects.filter(online=True).order_by('last_update_date')
    categories = Article.get_categories_from(articles)

    context = {
        'articles': articles,
        'categories': categories,
    }

    return render(request, 'arteablog/blog/index.html', context)


def article(request, id):

    article = Article.objects.filter(id=id).first()

    context = {
        'article': article,
    }

    return render(request, 'arteablog/article/index.html', context)
