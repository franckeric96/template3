from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('element', views.element, name='element'),
    path('singleblog', views.singleblog, name='singleblog'),
    path('singleproduct', views.singleproduct, name='singleproduct'),
    path('productlist', views.productlist, name='productlist'),
    path('login', views.login, name='login'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('confirmation', views.confirmation, name='confirmation'),


    

    
    
]