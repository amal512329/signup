from django.urls import path,re_path
from . import views


urlpatterns = [
    
    path('',views.signupview,name='signup'),
    path('login/',views.login,name='login'),
    path('next',views.next,name='next'),
    
]