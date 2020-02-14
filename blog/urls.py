from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index,name='index' ),
    path('order', views.order,name='order' ),
    path('buyagain/<int:itemsid>', views.buyagain, name='buyagain'),
    path('cancel/<int:itemsid>', views.index, name='cancel'),
    path('canceltotal', views.index, name='canceltotal'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('chart', views.cart,name='chart' ),
    path('product',views.product,name='product'),
    path('viewitems/<int:itemid>',views.viewitems,name='viewitems'),
    path('buycate',views.buycate,name='buycate'),
    path('buy/<int:itemid>',views.viewitems,name='buy'),
    path('addtowishlist/<int:itemid>',views.viewitems,name='addtowishlist'),
    path('signup', views.signup,name='signup'),
    path('login', views.handlelogin,name='login'),
    path('logout', views.handlelogout,name='logout'),

    

]
