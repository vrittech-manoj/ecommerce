
from django.urls import path
from . import views
# from account import views 

urlpatterns = [
    path('login',views.Login,name="login"),
    path('signup',views.Signup,name="user_register"),
]