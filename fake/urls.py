from django.urls import path
from . import views

app_name="blog"
urlpatterns = [
    path('zzzzz/zzzzz/', views.DataPage.as_view(), name='data'),
    path('home/', views.DataPage.as_view(), name='home'),
    path('xyz/user/', views.NewUser, name='newuser'),
    path('login/', views.Login.as_view(), name='login'),
    
]