from django.shortcuts import render, redirect
from adminapp.models import Category, Products
from electroapp.models import Customerdetails
from django.contrib.auth import  authenticate,logout


# Create your views here.
def home_pg(req):
    data = Category.objects.all()
    return render(req, "home.html", {'data': data})


def about_pg(req):
    data = Category.objects.all()
    return render(req, "about.html", {'data': data})


def about_d(req, dataid):
    da = Category.objects.all()
    data = Products.objects.get(id=dataid)
    return render(req, "about1.html", {'data': data, 'da': da})


def contact_pg(req):
    data = Category.objects.all()
    return render(req, "contact.html", {'data': data})


def products_pg(req):
    data = Products.objects.all()
    return render(req, "products.html", {'data': data})


def dispCateg(req, itemCateg):
    print("===itemCateg===", itemCateg)
    catg = itemCateg.upper()
    products = Products.objects.filter(Categry=itemCateg)
    da=Category.objects.all()
    context = {
        'products': products,
        'catg': catg,
        'da':da
    }
    return render(req, "displayCategory.html", context)


def displayProd(req, dataid):
    data = Products.objects.get(id=dataid)
    return render(req, "productDetails.html", {'data': data})


def login(request):
    return render(request, "login_or_register.html")


def loginsave(request):
    if request.method == "POST":
        u = request.POST.get('user')
        e = request.POST.get('email')
        p = request.POST.get('pass')
        c = request.POST.get('cpass')
        if p == c:
            obj = Customerdetails(username=u, email=e, password=p, confirmpassword=c)
            obj.save()
            return redirect(login)
        else:
            return render(request, 'login_or_register.html', {'msg': "Sorry......password not matched "})


def Customer_login(request):
    if request.method == 'POST':
        u = request.POST.get("user")
        p = request.POST.get("pass")

        if Customerdetails.objects.filter(username=u, password=p).exists():
            request.session['user'] = u
            request.session['pass'] = p
            return redirect(home_pg)
        else:
            return render(request, "login_or_register.html", {'msg': "Sorry......password not matched "})
def llogout(request):
    logout(request)
    return redirect(home_pg)