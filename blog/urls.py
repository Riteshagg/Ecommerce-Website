from django.urls import path
from . import views
urlpatterns = [
    path('index', views.index,name='index' ),
    path('product',views.product,name='product'),
    path('update', views.update,name='update'),
    path('signup', views.signup,name='signup'),

    

]