from django.shortcuts import render

# Create your views here.
def blog(request):

    articles = Article.objects.filter(online=True)
    categories = Article.get_categories_from(articles)

    context = {
        'articles': articles,
        'categories': categories,
    }

    return render(request, 'arteablog/blog/index.html', context)


def article(request, slug):

    article = Article.objects.filter(slug=slug).first()

    context = {
        'article': article,
    }

    return render(request, 'arteablog/blog/index.html', context)
