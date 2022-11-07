from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    articles_object = Article.objects.order_by(ordering)
    # print(Article.scopes.all)
    context = {
        'object_list': articles_object
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)