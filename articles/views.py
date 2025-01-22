from django.shortcuts import render
from . models import Article
def article_list(request):
    articles=Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/article_list.html', context)
def article_detail(request,id):
    pass

def article_update(request,id):
    pass

def article_delete(request,id):
    pass