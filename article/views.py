from django.shortcuts import render,redirect
from . import models
from .forms import CreateArticle
from django.contrib.auth.decorators import login_required
from comments import forms
from comments.models import Comments
def articles(request):
    article = models.Articles.objects.all()
    return render(request,'article.html',{'articles':article})
def articleview(request,slug):
    articl = models.Articles.objects.get(slug=slug)
    comment = forms.UserCumment()
    ucomment = Comments.objects.all()
    if request.method == "POST":
        commen = forms.UserCumment(request.POST)
        if comment.is_valid:
            commen.save()
    return render(request,"articleview.html",{"article":articl,"comments":comment,"usersc":ucomment})
@login_required(login_url="/accounts/login")
def art(request):
    form = CreateArticle()
    if request.method == "POST":
        form = CreateArticle(request.POST,request.FILES)
        if form.is_valid:
            formval = form.save(commit=False)
            formval.author = request.user
            formval.save()
            return redirect("/articles")
        else:
            form = CreateArticle()
    return render(request,"crtt.html",{"form":form})