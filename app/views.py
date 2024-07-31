from django.shortcuts import render,get_object_or_404
from .models import Project_Root,Startapp,Templates,Article,Static,Css,Js,Images

from django.db.models import Q


from django.shortcuts import render , redirect ,HttpResponse
from django.contrib import messages
from .forms import RegisterForm ,ProfileUpdate
from django.contrib.auth import get_user_model

from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth import authenticate , login , logout 
from .forms import ChangePasswordForm

import datetime
from django.db.models import Q
from .models import OtpToken





def profile_update(request):
    if request.user.is_authenticated:
        user = get_user_model().objects.get(id=request.user.id)
        print(f"user==={user}")
        forms = ProfileUpdate(request.POST or None, instance=user)

        if forms.is_valid():
           forms.save()
           print("Profile updated....")
           login(request, user)
           messages.success(request, 'profile updated succesfully.....')
           return redirect('home')

        
     
        return render(request, 'profile.html',{'forms':forms})
        
    else:
        return HttpResponse("you are not authenticated....")

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        print(f"current_user ====== {current_user}")
        print(f"request.first_name ======={request.user.first_name}")
        print(f"request.last_name ======{request.user.last_name}")
        print(f"request.username ======{request.user.username}")


        forms = ChangePasswordForm(current_user)

        if request.method == 'POST':
            forms = ChangePasswordForm(current_user, request.POST)
            if forms.is_valid():
             forms.save()
             messages.success(request, 'Password updated succesfully.....')
             login(request,current_user)

             return redirect('home')
            
            else:
              print("-------------------------")
              print("form is not valid")
              return render(request, 'uppassword.html', {"forms":forms})
           
            
        else:
            return render(request, 'uppassword.html', {"forms":forms})





def logout_user(request):
    logout(request)
    # messages.success(request , 'you sucessfully logged out')
    messages.success(request, 'You are succesfully logout.......')

    return redirect('home')



def login_page(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        print("--------------------------")
        print(f"username : {username}")
        print(f"password : {password}")
      
        user = authenticate(request, username=username, password=password)
        
        if user is not None:    
            login(request, user)
            messages.success(request, f"Hi {request.user.username}, you are now logged-in")
            return redirect("home")
        
        else:
            messages.warning(request, "Invalid credentials")
            return redirect("login_page")
        
    return render(request, "login_page.html")



def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , ("Accout created succefully,, An OTP was sent to your Email"))
            return redirect("verify-email",username=request.POST['username'])
        
        else:
            messages.error(request, "Please correct the errors below.")
        
    context = {"form":form}
    return render(request, "register_page.html",context)




def verify_email(request, username):
    user  = get_user_model().objects.get(username=username)
    user_otp = OtpToken.objects.filter(user=user).last()

    if request.method == 'POST':

        if user_otp.otp_code == request.POST['otp_code']:
            print("------------------------------")
            print(f"user_otp.otp_expires_at === {user_otp.otp_expires_at}")
            print(f"timezone.now() === {timezone.now()}")


            if user_otp.otp_expires_at > timezone.now():
                user.is_active = True
                user.save()

                messages.success(request , ("Acciut activated successfully..."))
                print("------------------------------")

                login(request,user)
                print("you succesfully logged in..........")

                return redirect("home")
            
            else:
                messages.warning(request , ("The Otp has Expired..."))
                return redirect("verify-email",username=user.username)
            
        else:
            messages.warning(request,("Invalid Otp entered,  enater valid otp"))
            return redirect("verify-email",username=user.username)
        
    context = {}
    return render(request , "verify_token.html",context)






def resend_otp(request):
    if request.method == 'POST':
        user_email = request.POST['otp_email']


        if get_user_model().objects.filter(email=user_email).exists():
            user = get_user_model().objects.get(email=user_email)
            otp  = OtpToken.objects.create(user=user ,otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))

            
            subject = "Email Verification"

            message = f""" 

          Hii {user.username},, here is your OTP {otp.otp_code}  and
          it expire in 5 mintunes
          http://127.0.0.1:8000/verify-email/{user.username}
                       

                           """
            sender = "sstcdurg@gmail.com"
            receiver = [user.email,]

        
            send_mail(
            subject,
            message,
            sender,
            receiver,
            fail_silently=False
               )

            messages.success(request, ("A new otp sent to your email"))
            return redirect("verify-email",username=user.username)
    
        else:
            messages.warning(request, ("this email not have in database..."))
            return redirect("resend-otp")
        
    context = {}

    return render(request,"resend_otp.html",context)






def articles(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')

        articles = Article.objects.filter(
            Q(title__icontains=search_query) |
            Q(date__icontains=search_query) |
            Q(project_description__icontains=search_query)
        )

        return render(request, 'articles.html',{'articles':articles})




    articles = Article.objects.all()
    return render(request, 'articles.html',{'articles':articles})

def djangoprojects(request):
    return render(request, 'djangoprojects.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')




def home(request):
    articles = Article.objects.all()

    return render(request, 'index.html',{'articles':articles})





def test(request):
    articles = Article.objects.all()

    return render(request, 'test.html',{'articles':articles})

def test_detail(request,id):
    article = Article.objects.get(pk=id)
    project = Project_Root.objects.get(pk=id)
    startapp = Startapp.objects.get(pk=id)
    template = Templates.objects.get(pk=id)



    print(article,project,startapp,template)

    print(f"article == {article}")  
    print(f"article.author == {article.author}") 
    print(f"project == {project}")
    print(f"startapp == {startapp}")
    print(f"template == {template}")
    


    return render(request, 'test_detail.html',{'article':article,'project':project,'startapp':startapp,'template':template})




def article_detail(request,id):

    article = get_object_or_404(Article, pk=id)
    project = get_object_or_404(Project_Root, pk=id)
    startapp = get_object_or_404(Startapp, pk=id)
    template = Templates.objects.filter(project_name=project)
    static = Static.objects.get(project_name=project)

    css = Css.objects.filter(static_name=static)

    js = Js.objects.filter(static_name=static)

    images = Images.objects.filter(static_name=static)

    # table_of_content = get_object_or_404(TableOfContent, pk=1)

    print(f"article == {article}")  
    print(f"article.author == {article.author}") 
    print(f"project == {project}")
    print(f"startapp == {startapp}")
    print(f"template == {template}")

    print(f"static == {static}")

    print(f"css == {css}")
    print(f"js == {js}")

    print(f"images == {images}")
    # print(f"table_of_content == {table_of_content}")

    # for temp in template:
    #     print(f"template == {temp}")
    #     print(f"template.html_name == {temp.html_name}")

    for img in images:
        print(f"img == {img}")
        print(f"img.images_name == {img.images_name}")
       
    

    return render(request, 'article_detail.html',{'article':article,'project':project,'startapp':startapp,'templates':template,'csss':css,'jss':js,'images':images})
