
from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

def post_list(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()

    form = ArticleForm()
    articles = Article.objects.all().order_by('-id')  # We get all articles, ordered by descending ID (latest first)
    return render(request, 'blog/post_list.html', {'form': form, 'articles': articles})

def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = ArticleForm()
    return render(request, 'blog/new_article.html', {'form': form})