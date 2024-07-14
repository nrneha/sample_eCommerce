from django.shortcuts import render, redirect
from Backend.models import Category_DB,Product_DB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import ContactDB
from django.contrib import messages


# Create your views here.
def view_indexPage(request):
    return render(request, "index.html")


def Category_Page(request):
    return render(request, "Category.html")


def Save_Categories_Data(request):
    if request.method == "POST":
        cnm = request.POST.get('category')
        cds = request.POST.get('description')
        cim = request.FILES['image']
        C_data = Category_DB(Category_Name=cnm, Category_Description=cds, Category_Image=cim)
        C_data.save()

        messages.success(request,"Category Saved Successfully.!")

        return redirect(Category_Page)


def Display_CategoryTable(request):
    item = Category_DB.objects.all()
    return render(request, "ShowCategoryTable.html", {'item': item})


def Edit_Category(request, c_id):
    c_data = Category_DB.objects.get(id=c_id)
    return render(request, "Edit_Category.html",{'c_data':c_data})

def Save_Updations(request,c_id):
    if request.method=="POST":
        cnm = request.POST.get('category')
        cds = request.POST.get('description')
        try:
            img = request.FILES['image']
            x = FileSystemStorage()
            file = x.save(img.name,img)
        except MultiValueDictKeyError:
            file = Category_DB.objects.get(id=c_id).Category_Image
        Category_DB.objects.filter(id=c_id).update(Category_Name=cnm, Category_Description=cds, Category_Image=file)
        return redirect(Display_CategoryTable)

def Delete_Data(request,c_id):
    data = Category_DB.objects.get(id=c_id)
    data.delete()
    messages.info(request,"You have Deleted A Category.!!!")
    return redirect(Display_CategoryTable)


def view_loginPage(request):
    return render(request,"Admin_login.html")

def Do_AdminLogin(request):
    if request.method=="POST":
        un = request.POST.get('username')
        ps = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un,password=ps)
            if x is not None:
                login(request,x)
                request.session['username'] = un
                request.session['password'] = ps
                messages.success(request,"Welcome!!")
                return redirect(view_indexPage)
            else:
                messages.error(request,"Incorrect Password!!")
                return redirect(view_loginPage)
        else:
            messages.error(request,"User not found")
            return redirect(view_loginPage)

def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(view_loginPage)


def Add_Products(request):
    catg = Category_DB.objects.all()
    return render(request,"Add_Products.html",{'catg':catg})

def Save_ProductData(request):
    if request.method=="POST":
        pnm = request.POST.get('product')
        pctg = request.POST.get('category')
        pdsc = request.POST.get('description')
        pcst = request.POST.get('price')
        pimg = request.FILES['image']

        Data = Product_DB( Product =pnm,Category =pctg,Description =pdsc, Price  =pcst,Image =pimg)
        Data.save()
        messages.success(request,"Product Added Successfully.!")

        return redirect(Add_Products)


def Show_Products(request):

    data = Product_DB.objects.all()
    return render(request,"Show_ProductTable.html",{'data':data})

def EditPage_Products(request,p_id):
    p_data = Product_DB.objects.get(id=p_id)
    c_data = Category_DB.objects.all()
    return render(request,"Edit_product.html",{'p_data':p_data,'c_data':c_data})

def Save_ProductUpdations(request,p_id):
    if request.method =="POST":
        pnm = request.POST.get('product')
        pctg = request.POST.get('category')
        pdsc = request.POST.get('description')
        pcst = request.POST.get('price')
        try:
            im = request.FILES['image']
            x = FileSystemStorage()
            file = x.save(im.name, im)
        except MultiValueDictKeyError:
            file = Product_DB.objects.get(id=p_id).Image
        Product_DB.objects.filter(id=p_id).update(Product =pnm,Category =pctg,Description =pdsc, Price  =pcst,Image =file)
        messages.success(request,"Product updated Successfully.!")
        return redirect(Show_Products)

def Delete_Product(request,p_id):
    x = Product_DB.objects.get(id=p_id)
    x.delete()
    messages.info(request,"Product Deleted!!!")
    return redirect(Show_Products)

def Customer_support(request):
    data = ContactDB.objects.all()
    return render(request,"CustomerQuery.html",{'data':data})

def delete_queries(request,c_id):
    data = ContactDB.objects.get(id=c_id)
    data.delete()
    return redirect(Customer_support)

