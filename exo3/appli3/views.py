from django.shortcuts import render

# Create your views here.

def index(request):
    datas = {
        
    }
    return render(request, 'index.html', datas)


def about(request):
    datas = {
        
    }
    return render(request, 'about.html', datas)

def blog(request):
    datas = {
        
    }
    return render(request, 'blog.html', datas)


def contact(request):
    datas = {
        
    }
    return render(request, 'contact.html', datas)



def element(request):
    datas = {
        
    }
    return render(request, 'elements.html', datas)

def singleblog(request):
    datas = {
        
    }
    return render(request, 'single-blog.html', datas)

def singleproduct(request):
    datas = {
        
    }
    return render(request, 'single-product.html', datas)


def productlist(request):
    datas = {
        
    }
    return render(request, 'product_list.html', datas)


def login(request):
    datas = {
        
    }
    return render(request, 'login.html', datas)


def cart(request):
    datas = {
        
    }
    return render(request, 'cart.html', datas)


def checkout(request):
    datas = {
        
    }
    return render(request, 'checkout.html', datas)


def confirmation(request):
    datas = {
        
    }
    return render(request, 'confirmation.html', datas)
