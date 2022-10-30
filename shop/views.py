from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from django.views import View

from shop.forms import SignUpForm
from shop.models import Product


# Create your views here.
class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')
        laptops = Product.objects.filter(category='L')
        return render(request, 'app/home.html', {'topwears':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles, 'laptops':laptops})

class ProductDetail(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product})
def home(request):
    return render(request, 'app/home.html')

def product_detail(request):
    return render(request, 'app/productdetail.html')

def add_to_cart(request):
    return render(request, 'app/addtocart.html')

def buy_now(request):
    return render(request, 'app/buynow.html')

def profile(request):
    return render(request, 'app/profile.html')

def address(request):
    return render(request, 'app/address.html')

def orders(request):
    return render(request, 'app/orders.html')

def change_password(request):
    return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'samsung1' or data == 'samsung2' or data == 'samsung3':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=25000)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gte=25000)

    return render(request, 'app/mobile.html',{'mobiles':mobiles})

# def login(request):
#     return render(request, 'app/login.html')

# def customerregistration(request):
#     return render(request, 'app/customerregistration.html')
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'app/customerregistration.html',{'form':form})
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! Registered Successfully')
            user={}
            user['Username'] = form.cleaned_data['username']
            user['Email'] = form.cleaned_data['email']
            user['Password'] = form.cleaned_data['password1']
            user['is_staff'] = True
            user = User.objects.create_user(user['Username'], user['Email'], user['Password'], is_staff=user['is_staff'])
            group = Group.objects.get(name='Tour Guide')
            user.groups.add(group)
            user.save()
            return redirect('home')

        return render(request, 'app/customerregistration.html',{'form':form})

# class SignIn(View):
#     def get(self, request):
#         return render(request, 'app/login.html')
#     def post(self, request):
#         return render(request, 'app/login.html')
def checkout(request):
    return render(request, 'app/checkout.html')