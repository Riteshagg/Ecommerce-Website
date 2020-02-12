from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index,name='index' ),
    path('product',views.product,name='product'),
    path('signup', views.signup,name='signup'),
    path('login', views.handlelogin,name='login'),
    path('logout', views.handlelogout,name='logout'),

    

]