from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index,name='index' ),
    path('order', views.order,name='order' ),
    path('cancel/<int:itemsid>', views.cancel, name='cancel'),
    path('canceltotal', views.canceltotal, name='canceltotal'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('cart', views.cart, name='cart'),
    path('cart/<int:itemsid>', views.cartparam, name='cartparam'),
    path('product',views.product,name='product'),
    path('viewitems/<int:itemid>',views.viewitems,name='viewitems'),
    path('buycate',views.buycate,name='buycate'),
    path('buy/<int:itemid>',views.viewitems,name='buy'),
    path('addtowishlist/<int:itemid>',views.viewitems,name='addtowishlist'),
    path('signup', views.signup,name='signup'),
    path('login', views.handlelogin,name='login'),
    path('logout', views.handlelogout,name='logout'),

    

]
