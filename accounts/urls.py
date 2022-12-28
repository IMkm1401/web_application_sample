from django.urls import path
from accounts.views import loginView, signup,Logoutview
app_name = 'accounts'
urlpatterns = [
    path('signup/',signup),
    path('login/',loginView),
    path('logout/',Logoutview,name="logout"),
]