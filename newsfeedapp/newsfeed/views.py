from django.shortcuts import render
from .models import News
from .forms import NewsForm
from django.shortcuts import get_object_or_404, redirect

def index(request):
    return render(request, 'index.html')

def news_list(request):
    newsList = News.objects.all().order_by('-created_at')
    return render(request, 'news_list.html', {'news':news_list})

def news_create(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = request.user
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news_form.html', {'form':form})

def  news_edit(request, news_id):
    news = get_object_or_404(News, pk=news_id, user = request.user)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            news = form.save(commit=False)
            news.user = request.user
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news_form.html', {'form':form})
    
def news_delete(request, news_id):
    news = get_object_or_404(News, pk=news_id, user = request.user)
    if request.method == "POST":
        news.delete()
        return redirect('news_list')
    return render(request, 'news_confirm_delete.html', {'news':news})