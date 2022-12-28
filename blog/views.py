from django.shortcuts import render,redirect
from comments import forms
from article import models
from comments.models import Comments
def home(request):
    form = forms.UserCumment()
    if request.method == "POST":
        message = forms.UserCumment(request.POST)
        if form.is_valid:
            message.save()
        else:
            return redirect("")
    comments = Comments.objects.all()
    article = models.Articles.objects.all().order_by("-date")
    return render(request,"home.html",{"article":article,"form":form,"usercomments":comments})
    