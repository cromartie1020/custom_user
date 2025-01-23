from django.shortcuts import render,redirect
from . models import Article
from .forms import ArticleForm 
from django.contrib.auth.decorators import login_required

def article_list(request):
    articles=Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/article_list.html', context)
@login_required
def article_detail(request,id):
    article=Article.objects.get(id=id)
    context ={
        'article':article
    }
    return render(request, 'articles/article_detail.html',context)
@login_required
def article_new(request):
    if request.method == ('POST' or  None):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:


        form=ArticleForm()

    context= {
        'form':form
    }

    return render(request,'articles/article_new.html',context)    
@login_required
def article_update(request,id):
    article= Article.objects.get(id = id)
    form = ArticleForm(request.POST or None, instance= article)
    if form.is_valid():
        article=form.save(commit=False)
        article.save()
        return redirect('article_list') 
    context = {
        'form':form
    }
    return render(request, 'articles/article_update.html', context)

@login_required
def article_delete(request,id):
    article=Article.objects.get(id =id )
    article.delete()
    return render(request, 'articles/article_delete.html')
@login_required
def article_confirm_delete(request,id):
    article=Article.objects.get(id =id )
    
    context ={
        'article':article
    }
    return render(request, 'articles/article_delete_confirm.html', context)