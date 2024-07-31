from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('articles/',articles,name='articles'),
    path('test_detail/<int:id>/',test_detail,name='test_detail'),  
    path('article_detail/<int:id>/',article_detail,name='article_detail'),

    path('djangoprojects/',djangoprojects,name='djangoprojects'),
    path('portfolio/',portfolio,name='portfolio'),
    path('contact/',contact,name='contact'),


    path('register/',register_page,name='register_page'),
    path('login/',login_page,name='login_page'),
    path("verify-email/<slug:username>/",verify_email,name="verify-email"),
    path("resend-otp/",resend_otp,name="resend-otp"),
    path('logout_user/',logout_user,name="logout_user"), 
    path('update_password/',update_password,name="update_password"),
    path('profile_update/',profile_update,name="profile_update"),
  


]

