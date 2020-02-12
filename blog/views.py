from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product
from .forms import List
# Create your views here.

def index(request):
    if request.method=="POST":
            model= List(request.POST,request.FILES)  
            if model.is_valid():
                    model.save()
            return redirect(product)
    else:
           model = List()  
    return render(request,'blog/index.html',{'form':model})
  

    


def product(request):
     pro = Product.objects.all()
     params  = {'products':pro}
     return render(request,'blog/product.html',params)




def signup(request):
        if request.method == "POST":
                username = request.POST['username']
                email = request.POST['email']
                password = request.POST['password']
                fname = request.POST['fname']
                lname = request.POST['lname']
                user = User.objects.create_user(username,email,password)
                user.first_name = fname
                user.last_name = lname
                user.save()
                messages.success(request,"Your account has been successfully created")
                return redirect(index)
        else:
                print("not Posted")      
        return render(request,"blog/signup.html")



def handlelogin(request):
        if request.method == "POST":
                loginusername = request.POST['username']
                loginpassword = request.POST['pass']
                user = authenticate(username=loginusername, password=loginpassword)
                if user is not None:
                        login(request,user)
                        messages.success(request,"Login successfully")  
                        return redirect(product)
                else:
                        messages.error(request,"invalid login username and password")    
                        return redirect(index)    
        return render(request,"blog/login.html")

def handlelogout(request):
        logout(request)
        messages.success(request,"Logout successfully") 
        return redirect(index)       