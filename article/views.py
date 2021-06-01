from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib import messages
from .models import Article, Comment
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

def articles (request):
    keyword = request.GET.get("keyword") 
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html", {"articles": articles})

    articles = Article.objects.all()
    return render(request, "articles.html",{"articles":articles})


# Create your views here.
def index(request):
    return render (request, "index.html")
def about(request):
    return render(request,"about.html")
def detail (request,id):
    article = article.object.filter(id = id).first()
    return render(request,"detail.html",{"article":article})
    #return HttpResponse("Detail:"+str(id))

@login_required(login_url="user:login")
def dashboard (request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles" : articles
}
    return render(request, "dashboard.html",context)

@login_required(login_url="user:login")
def addarticle (request):
    form = ArticleForm(request.POST or None, request.FILES or None,)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makaleniz Başarıyla Kaydedilmiştir.")
        return redirect("article:dashboard")
    return render(request, "addarticle.html",{"form":form})

def detail (request,id):
    article = Article.objects.filter(id=id).first()
    comments = article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})

@login_required(login_url="user:login")
def updatearticle (request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale Başarılı Bir Şekilde Güncellenmiştir")
        return redirect("article:dashboard")
    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deletearticle(request,id):
    article = get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request, "Makale Başarılı Bir Şekilde Silinmiştir")
    return redirect("article:dashboard")

def addcomment(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method =="POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author=comment_author, comment_content=comment_content)
        newComment.article = article
        newComment.save()
    return redirect("/articles/article/"+str(id))