from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from django.contrib.auth.models import User

from .models import *

# Create your views here.

# @login_required(login_url='/')
def logins(request):

    username = request.POST.get('username')
    password = request.POST.get('pass')

    next = request.GET.get('next', False)
    user = authenticate(username=username, password=password)

    if user is not None and user.is_active:
    
        # print("user is login")
        
        login(request, user)

        if next: 
            return redirect(next)
        else:
            return redirect('homepage') # page si connect
      
    else:
        return render(request, 'pages/index.html')




def register(request):

    name = request.POST.get('name')
    prenom = request.POST.get('prenom')
    email = request.POST.get('email')
    username = request.POST.get('username')
    contact = request.POST.get('contact')
    date = request.POST.get('date')
    image = request.FILES.get('image')
    password = request.POST.get('pass')
    # Confirmpass = request.POST.get('repeat-pass')

    # User
    
    try:
        user = User(username =username, first_name = name, last_name = prenom, email = email)
        user.save()

        user.profile.contacts = contact
        user.profile.image = image
        user.profile.birth_date = date
        user.save()

        user.password = password
        user.set_password(user.password)
        user.save()

    except:
        pass



    return render(request, 'pages/regis.html')



def deconnexion(request):
    logout(request)
    return redirect('conect') 


@login_required(login_url='/')
def dashbord(request):

    search = request.POST.get('recherch')
    

    videoAdmin = Videodash.objects.all().order_by('-date_Add')

    if search:
        videoAdmin = videoAdmin.filter(titre__icontains=search)
    paginator = Paginator(videoAdmin, 6)

    page = request.GET.get('page')

    videoadminist = paginator.get_page(page)

    context = {
        'videoadmin': videoadminist
    }

    return render(request, 'pages/dashbord.html', context)