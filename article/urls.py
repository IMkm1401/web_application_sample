from django.urls import path
from .views import articles
from accounts.views import loginView
from accounts.views import signup
from .views import articleview,art
app_name = 'article'
urlpatterns = [
    path("create",art,name="vill"),
    path("",articles,name="list"),
    path("<slug>",articleview,name="detail"),
    path("accounts/login",loginView,name="login"),
    path("accounts/signup",signup,name="signup"),
]
