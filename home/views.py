from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import Contact, ContactForm
from product.models import Category, Product


def index(request):
    category = Category.objects.all()
    products = Product.objects.all()

    context = { 'page': 'home',
                'category': category,
                'products': products,
    }
    return render(request, 'index.html',context)

def login_form(request):
    if request.method=="POST":

        next_url = request.POST.get("next")
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if next_url:
                return redirect(next_url)
            else:
                return  redirect('/')
        else:
            context = {'hata': 'Kullanıcı adı yada şifre hatalı!!',

                       }
            return render(request, "login.html",context)
    else:
        return render(request, "login.html")


def login_out(request):
    logout(request)
    return redirect('/home')


def join_form():
    return None

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            contactdata=Contact()
            contactdata.name    = form.cleaned_data['name']
            contactdata.email   =form.cleaned_data['email']
            contactdata.subject =form.cleaned_data['subject']
            contactdata.message =form.cleaned_data['message']
            contactdata.save()

            messages.success(request,"Your message has sent.Thank you for your interest")
            return HttpResponseRedirect('/contact')


    else:
        form=ContactForm()

    return render(request,'contact.html',{'form': form })