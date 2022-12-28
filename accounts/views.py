from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/')       
    else:
        form = UserCreationForm()
        return render(request,'signup.html',{'form':form})
def loginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/')
    form = AuthenticationForm()
    return render(request,'loginn.html',{'form':form})
    
def Logoutview(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')