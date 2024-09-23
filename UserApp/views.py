from django.shortcuts import render,redirect
from . models import *
from AdminApp .models import *
from django.db.models.aggregates import Sum
# Create your views here.
def userindex(request):
    products = Products.objects.all()
    category = Category.objects.all()
    return render(request,'userindex.html',{'products':products,'category':category})
def register(request):
    return render(request,'register.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def products(request):
    products = Products.objects.all()
    return render(request,'products.html',{'products':products})
def categories(request):
    category = Category.objects.all()
    return render(request,'categories.html',{'category':category})
def userlogin(request):
    return render(request,'login.html')
def userreg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        number = request.POST.get('number')
        place = request.POST.get('place')
        data = Register(name = name, email = email, place = place,password = password,phone = number)
        data.save()
    return redirect('userlogin')
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        if name == 'admin' and password == 'admin':
            return redirect('adminindex')
        elif Register.objects.filter(name = name,password = password).exists():
            data = Register.objects.filter(name = name,password =password).values('id','place','email','phone').first()
            request.session['user_name'] = name
            request.session['user_password'] = password
            request.session['user_place'] = data['place']
            request.session['user_phone'] = data['phone']
            request.session['user_id'] = data['id']
            request.session['user_email'] = data['email']
            return redirect('userindex')
        else:
            return render(request,'login.html',{'msg':'invalid username or password'})
    else:
        return redirect('userlogin')
def logout(request):
    request.session.flush()
    return redirect('userlogin')
def message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        data =  Contact(name = name,email = email,subject = subject,message = message,phone = phone)
        data.save()
    return redirect('userindex')
def singledetails(request,id):
    product = Products.objects.filter(id = id)
    return render(request,'singledetails.html',{'product':product})
def cart(request):
    u_id = request.session.get('user_id')
    data = Cart.objects.filter(usercart = u_id,status = 0)
    a = Cart.objects.filter(usercart = u_id,status = 0).aggregate(Sum('total'))
    return render(request,'cart.html',{'data':data,'a':a})
def checkout(request):
    u_id = request.session.get('user_id')
    data = Cart.objects.filter(usercart = u_id,status = 0)
    a = Cart.objects.filter(usercart = u_id,status = 0).aggregate(Sum('total'))
    return render(request,'checkout.html',{'data':data,'a':a})
def addtocart(request,id):
    if request.method == "POST":
        user_id = request.session.get('user_id')
        quantity = request.POST.get('quantity')
        total = request.POST.get('total')
        print(total)
        print(quantity)
        data = Cart(usercart = Register.objects.get(id=user_id),userpro = Products.objects.get(id=id),quantity = quantity,total = total)
        data.save()
    return redirect('cart')
def removepro(request,id):
    data = Cart.objects.filter(id=id).delete()
    return redirect('cart')
def checkoutdata(request):
    if request.method == "POST":
        checkoutid = request.session.get('user_id')
        adress = request.POST.get('address')
        country = request.POST.get('country')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        data = Cart.objects.filter(usercart = checkoutid,status = 0)

        for i in data:
            data = Checkout(usercheckout = Register.objects.get(id = checkoutid), usercart = Cart.objects.get(id=i.id),adress = adress,city = state, pincode = pincode, country = country)
            data.save()
            Cart.objects.filter(id=i.id).update(status=1)
        return redirect('sucess')
def sucess(request):
    user_id = request.session.get('user_id')
    data = Checkout.objects.filter(usercheckout = user_id)
    return render(request,'sucess.html',{'data':data})

def viewcatpro(request,category):
    category_name = Category.objects.filter(category_name = category)
    data = Products.objects.filter(product_category = category)
    return render(request,'singlecat.html',{'data':data,'category_name':category_name})
def profile(request):
    user_id = request.session.get('user_id')
    data = Register.objects.get(id = user_id)
    return render(request,'profile.html',{'data':data})
def editprofile(request):
    user_id = request.session.get('user_id')
    data = Register.objects.get(id = user_id)
    return render(request,'editprofile.html',{'data':data})
def updateprofile(request):
        if request.method == "POST":
            user_id = request.session.get('user_id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            place = request.POST.get('place')
            Register.objects.filter(id = user_id).update(name = name,email = email,phone = phone,place = place)
            return redirect('profile')
        
def demo(request):
    return render(request,'demo.html')






