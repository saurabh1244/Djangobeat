from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
from django.conf import settings
import secrets
import datetime





class OtpToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE,related_name="otps")
    otp_code = models.CharField(max_length=6 , default=secrets.token_hex(3))
    tp_created_At = models.DateTimeField(auto_now_add=True)
    otp_expires_at  = models.DateTimeField(blank=True , null=True)
    print("--------------------------")
    print(f"tp_created_At === {tp_created_At}")
    print(f"otp_expires_at === {otp_expires_at}")

    def __str__(self):
        return self.user.username
    


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = ("email")
    REQUIRED_FIELDS = ["username"]

    # def __str__(self):
    #     return self.email
 

class Project_Root(models.Model):

    project_name = models.CharField(max_length=200)

    asgi = models.TextField(blank=True,null=True)
    asgi_context = models.TextField(blank=True,null=True)

    settings = models.TextField(blank=True,null=True)
    settings_context = models.TextField(blank=True,null=True)

    urls = models.TextField(blank=True,null=True)
    urls_context = models.TextField(blank=True,null=True)

    wsgi = models.TextField(blank=True,null=True)
    wsgi_context = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.project_name


class Startapp(models.Model):
    project_name = models.ForeignKey(Project_Root,on_delete=models.CASCADE)

    app_name = models.CharField(max_length=200)

    admin = models.TextField(blank=True,null=True)
    admin_context = models.TextField(blank=True,null=True)

    apps = models.TextField(blank=True,null=True)
    apps_context = models.TextField(blank=True,null=True)

    model = models.TextField(blank=True,null=True)
    model_context = models.TextField(blank=True,null=True)

    test = models.TextField(blank=True,null=True)
    test_context = models.TextField(blank=True,null=True)

    urls = models.TextField(blank=True,null=True)
    urls_context = models.TextField(blank=True,null=True)

    views = models.TextField(blank=True,null=True)
    views_context = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.app_name



class Templates(models.Model):
    project_name = models.ForeignKey(Project_Root,on_delete=models.CASCADE)

    html_name = models.CharField(max_length=200,blank=True,null=True)
    html_data = models.TextField(max_length=40000,blank=True,null=True)
    html_context = models.TextField(max_length=4000,blank=True,null=True)

    def __str__(self):
        return self.html_name



class Static(models.Model):
    project_name = models.ForeignKey(Project_Root,on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name.project_name
   

class Css(models.Model):
    static_name = models.ForeignKey(Static,on_delete=models.CASCADE)
    css_name = models.CharField(max_length=200,null=True,blank=True)
    css_data = models.TextField(max_length=40000,blank=True,null=True)
    css_context = models.TextField(max_length=4000,blank=True,null=True)


class Js(models.Model):
    static_name = models.ForeignKey(Static,on_delete=models.CASCADE)
    js_name = models.CharField(max_length=200,null=True,blank=True)
    js_data = models.TextField(max_length=40000,blank=True,null=True)
    js_context = models.TextField(max_length=4000,blank=True,null=True)


class Images(models.Model):
    static_name = models.ForeignKey(Static,on_delete=models.CASCADE)
    images_name = models.CharField(max_length=200,null=True,blank=True)
    images_data = models.ImageField(upload_to='Images')



class Media(models.Model):
    project_name = models.ForeignKey(Project_Root,on_delete=models.CASCADE)
    data = models.CharField(max_length=200,null=True,blank=True)




class Article(models.Model):
    title = models.CharField(max_length=255)
    author  = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    project = models.ForeignKey(Project_Root,on_delete=models.CASCADE)
    project_description = models.TextField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return self.title



class TableOfContent(models.Model):
    project_name = models.ForeignKey(Project_Root,on_delete=models.CASCADE)
    model_structure_graph = models.TextField(max_length=1000,blank=True,null=True)
    screenshot1 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot2 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot3 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot4 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot5 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot6 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot7 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot8 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot9 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot10 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot11 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot12 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot13 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot14 = models.ImageField(upload_to='Images',blank=True,null=True)
    screenshot15 = models.ImageField(upload_to='Images',blank=True,null=True)
    
   

