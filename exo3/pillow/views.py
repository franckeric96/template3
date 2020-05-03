from django.shortcuts import render

from contact.models import NewsLetter, Contact

from formulaire import ContactForm, CommentForm

from configuration.models import Temoignage, SocialAccount, Presentation

# Create your views here.


def index(request):

    if request.method == 'POST':
        email = request.POST['newsletter']
        if email:
            news_letter = NewsLetter.objects.create(email=email)
            news_letter.save()

    temoignages = Temoignage.objects.filter(status=True)[:2]
    sociaux = SocialAccount.objects.filter(status=True)



    datas = {
        'temoignages' : temoignages,
        'sociaux' : sociaux,
        }
    return render(request, "index.html", datas)


def about(request):
    if request.method == 'POST':
        email = request.POST['newsletter']
        if email:
            news_letter = NewsLetter.objects.create(email=email)
            news_letter.save()
    
    temoignages = Temoignage.objects.filter(status=True)[:2]
    sociaux = SocialAccount.objects.filter(status=True)
    presentations = Presentation.objects.filter(status=True)

  
    datas = {

        'temoignages' : temoignages,
        'sociaux' : sociaux,
        'presentations' : presentations


    }
    return render(request, "about.html", datas)


def blog(request):
    if request.method == 'POST':
        email = request.POST['newsletter']
        if email:
            news_letter = NewsLetter.objects.create(email=email)
            news_letter.save()

    sociaux = SocialAccount.objects.filter(status=True)
  
    datas = {
        'sociaux' : sociaux

    }

    return render(request, "blog.html", datas)


def cart(request):

    sociaux = SocialAccount.objects.filter(status=True)
  
    datas = {
        'sociaux' : sociaux

    }
    return render(request, "cart.html", datas)


def checkout(request):



    sociaux = SocialAccount.objects.filter(status=True)
  
    datas = {
        'sociaux' : sociaux

    }
    return render(request, "checkout.html", datas)


def confirmation(request):
    
    sociaux = SocialAccount.objects.filter(status=True)
  
    datas = {
        'sociaux' : sociaux

    }
    return render(request, "confirmation.html", datas)


def contact(request):
    formulaire = ContactForm(request.POST or None)
    if formulaire.is_valid():
        formulaire.save()
        formulaire = ContactForm()



    sociaux = SocialAccount.objects.filter(status=True)
        
    datas = {

        'form': formulaire,
        'sociaux' : sociaux

    }
    return render(request, "contact.html", datas)


def elements(request):

    sociaux = SocialAccount.objects.filter(status=True)
  
    datas = {
        'sociaux' : sociaux

    }
    return render(request, "elements.html", datas)


def login(request):

    sociaux = SocialAccount.objects.filter(status=True)
  
    datas = {
        'sociaux' : sociaux

    }
    return render(request, "login.html", datas)


def main(request):
    
    sociaux = SocialAccount.objects.filter(status=True)
  
    datas = {
        'sociaux' : sociaux

    }
    return render(request, "main.html", datas)


def product_list(request):
    
    sociaux = SocialAccount.objects.filter(status=True)
  
    datas = {
        'sociaux' : sociaux

    }
    return render(request, "product_list.html", datas)


def single_blog(request):

    sociaux = SocialAccount.objects.filter(status=True)
  
    datas = {
        'sociaux' : sociaux

    }
    return render(request, "single-blog.html", datas)


def single_product(request):

    sociaux = SocialAccount.objects.filter(status=True)
  
    datas = {
        'sociaux' : sociaux

    }
    return render(request, "single-product.html", datas)
