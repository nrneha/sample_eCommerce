from django.shortcuts import render,redirect
from Backend.models import Product_DB,Category_DB
from WebApp.models import ContactDB,User_Account,CartDB
from django.contrib import messages

# Create your views here.

def Homepage(request):
    c_data = Category_DB.objects.all()
    return render(request,"Home.html",{'c_data':c_data})

def AboutPage(request):
    return render(request,"About.html")

def ContactPage(request):
    return render(request,"Contact.html")

def Show_Products(request):
    cdata = Category_DB.objects.all()
    data = Product_DB.objects.all()
    return render(request,"Show_Products.html",{'data':data,'cdata':cdata})

def Save_CustomerMessages(request):
    if request.method == "POST":
        cnm = request.POST.get('name')
        cem = request.POST.get('email')
        csb = request.POST.get('subject')
        cms = request.POST.get('message')

        obj = ContactDB(Name =cnm,Email =cem, Subject =csb,Message =cms )
        obj.save()
        return redirect(ContactPage)


def Show_FilterdProucts(request,ctg):
    data = Product_DB.objects.filter(Category=ctg)
    ctg_data = Category_DB.objects.all()
    return render(request,"Filterd_Products.html",{'data':data,'ctg_data':ctg_data})

def Single_Products(request,p_id):
    data = Product_DB.objects.get(id=p_id)
    return render(request,"Single_product.html",{'data':data})

def user_registration(request):
    return render(request,"user_registration.html")

def Save_UserAccount(request):
    if request.method=="POST":
        nm = request.POST.get('name')
        em = request.POST.get('email')
        ps = request.POST.get('password1')

        ob = User_Account(Name=nm,Email=em,Password=  ps)
        if User_Account.objects.filter(Name=nm).exists():
            messages.warning(request,"Username not available !!")
            return redirect(user_registration)
        elif User_Account.objects.filter(Email=em).exists():
            messages.info(request,"Email id not available !!")
        else:
            ob.save()
            messages.success(request,"Registered Successfully")
        return redirect(user_registration)

def UserLogin(request):
    if request.method=="POST":
        un = request.POST.get('username')
        psw = request.POST.get('password')
        request.session['Name']=un
        request.session[' Password']=psw
        if User_Account.objects.filter(Name =un,Password = psw).exists():
            messages.success(request,"WELCOME")
            return redirect(Homepage)
        else:
            messages.error(request, "User not found..!!")
            return redirect(user_registration)
    else:
        return redirect(user_registration)

def UserLogout(request):
    del request.session['Name']
    del request.session[' Password']
    messages.success(request,"Logout Successfully.")
    return redirect(Homepage)

def Save_Cart(request):
    if request.method=="POST":
        un = request.POST.get('user')
        pn = request.POST.get('productname')
        qt = request.POST.get('quantity')
        tp = request.POST.get('total')

        obj = CartDB( UserName =un,Product =pn,Quantity =qt,TotalPrice =tp)
        obj.save()
        messages.success(request,"Yeah...An Item added to cart..")
        return redirect(Show_Products)

def View_Cart(request):
    data = CartDB.objects.filter(UserName=request.session['Name'])
    total = 0
    for d in data:
        total = total+d.TotalPrice
    return render(request,"Cart.html",{'data':data,'total':total})

def Remove_CartedItem(request,p_id):
    x = CartDB.objects.get(id = p_id)
    x.delete()
    messages.success(request,"Item removed from cart")
    return redirect(View_Cart)

def user_loginpage(request):
    return render(request,"UserLogIn.html")