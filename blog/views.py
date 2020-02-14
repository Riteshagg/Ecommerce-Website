from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product,ProQuantity,Transaction
from .forms import List,Quentity
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
  

    

@login_required(login_url='login')
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



@login_required(login_url='login')
def handlelogout(request):
        logout(request)
        messages.success(request,"Logout successfully") 
        return redirect(index)    


@login_required(login_url='login')
def order(request):
        items = Transaction.objects.filter(userId=request.user.id,status="buy")
        products = []
        for item in items:    
            products += Product.objects.filter(id=item.productid)
        param  = {'model':products}
        return render(request,'blog/order.html',param)






@login_required(login_url='login')
def viewitems(request,itemid):
        items = Product.objects.get(id=itemid)
        model = ProQuantity.objects.all()  
        params  = {'item':items,'model':model}
        return render(request,'blog/product_items.html',params)



@login_required(login_url='login')
def buycate(request):
        
        if request.method=="POST":
                product_id = request.POST['id']
                quantity = request.POST['quantityID']
                if 'buynow' in request.POST:                      
                        cart_item = Transaction.objects.create(userId=request.user.id, productid=product_id,quantityid=quantity,status="Buy")
                        messages.success(request,"Transaction has been done successfully") 
                        return redirect(viewitems,request.user.id)

                elif 'addtocart' in  request.POST:
                        cart_item = Transaction.objects.create(userId=request.user.id, productid=product_id,quantityid=quantity,status="AddToCart")
                        messages.success(request,"Your item  has been add to cart successfully") 
                        return redirect(cart)
                else:
                        cart_item = Transaction.objects.create(userId=request.user.id, productid=product_id,quantityid=quantity,status="AddToWishList")
                        messages.success(request,"Your item  has been add to wish list successfully") 
                        return redirect(wishlist)
        else:
                 model = ProQuantity.objects.all()  
        return render(request,'blog/index.html',{'model':model,})


def wishlist(request):
        items = Transaction.objects.filter(userId=request.user.id,status="AddToWishList")
        products = []
        for item in items:
            products += Product.objects.filter(id=item.productid)
        param = {'model': products}
        return render(request, 'blog/whishlist.html', param)




def cart(request):
        items = Transaction.objects.filter(userId=request.user.id,status="AddToCart")
        itemsCount = Transaction.objects.filter(userId=request.user.id, status="AddToCart").count()
        totalPrice = 0
        products = []
        for item in items:
            query = Product.objects.filter(id=item.productid)
            products += query
            for total in query:
                    totalPrice += total.price

        param = {'model': products, 'itemCount': itemsCount,'totalPrice':totalPrice}
        return render(request, 'blog/cart.html', param)


def buyagain(request,itemsid):
        cart_update = Transaction.objects.filter(pk=some_value).update(field1='some value')
        cart_item = Transaction.objects.create(userId=request.user.id, productid=itemsid,quantityid=quantity,status="Buy")
        messages.success(request,"Transaction has been done successfully") 
        return redirect(viewitems,request.user.id)        
                


                  
