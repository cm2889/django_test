from pyexpat import model
from django.shortcuts import render,redirect
import hashlib
from . import models
import datetime

# Create your views here.
def login(request):
    return render(request,'login.html')
    
#Registration Page
def registration(request):
    if request.method=="POST":    
        email = request.POST.get('email')
        print("email: ", email)
        username=request.POST['username'] #ki error dibe eita diye bujbo
        password=request.POST['password']
        new_md5_obj= hashlib.md5(password.encode())
        new_enc_pass= new_md5_obj.hexdigest()

        models.SalesPerson.objects.create(
            email=email, username=username, password=new_enc_pass
        )
        return render(request,'registration.html') 
    else:
        return render(request,'registration.html') 
#Login 
def login(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        new_md5_obj= hashlib.md5(password.encode())
        new_enc_pass= new_md5_obj.hexdigest()
        
        result = models.SalesPerson.objects.filter(username=username,password=new_enc_pass)
        if(result):
            request.session['username']=result[0].username
           
            return redirect('/user-list')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

#userList
def userList(request):
    if(request.method=="GET"):
            #student_list=models.Students.objects.all() #dor all information
            #student_list=models.Students.objects.filter()
            user_list=models.SalesPerson.objects.all()
            context = {'user_list': user_list}
    return render(request,'userList.html',context)
#categoryList
def categoryList(request):
    category_list=models.Category.objects.all()
    context = {'category_list': category_list}
    if request.method=="POST":
        category_name=request.POST['category_name']
        models.Category.objects.create(category_name=category_name)
    return render(request,'category/index.html',context)
#category delete
def category_delete(request,pk):
    models.Category.objects.filter(id=pk).delete()
    return redirect('/category-list')
#Category Edit
def category_edit(request,pk):
    Category=models.Category.objects.get(id=pk)

    if(request.method=="POST"):
        category_name = request.POST.get('category_name')
        status = True if request.POST.get('status') else False
        current_time=datetime.datetime.now()
        models.Category.objects.filter(id=pk).update(category_name=category_name,status=status,updated_at=current_time)
        return redirect('/category-list')

    return render(request,'category/edit.html',{'Category':Category})
 #productList
def productList(request):
    category_list=models.Category.objects.all()
    product_List=models.Product.objects.all()
    context = {'product_List': product_List,'category_list':category_list}
    if request.method=="POST":
         category_id=request.POST['category_id']
         product_web_name=request.POST['product_web_name']
         product_code=request.POST['product_code']
         models.Product.objects.create(category_id=category_id,product_web_name=product_web_name,product_code=product_code)
    return render(request,'product/index.html',context)
#product Edit
def product_edit(request,pk):
    Product=models.Product.objects.get(id=pk)
    category_list=models.Category.objects.all()

    if(request.method=="POST"):
        category_id = request.POST.get('category_id')
        product_web_name = request.POST.get('product_web_name')
        product_code = request.POST.get('product_code')
        status = True if request.POST.get('status') else False
        current_time=datetime.datetime.now()
        models.Product.objects.filter(id=pk).update(category_id=category_id,
        product_web_name=product_web_name,product_code=product_code,
        status=status,updated_at=current_time)
        return redirect('/product-list')

    return render(request,'product/edit.html',{'Product':Product,'category_list':category_list})
#product delete
def product_delete(request,pk):
    models.Category.Product.filter(id=pk).delete()
    return redirect('/product-list')
#Complain List
def complainList(request):

    complain_List=models.Complain.objects.all()
    complain_type=models.ComplainType.objects.all()
    context = {'complain_List': complain_List,'complain_type':complain_type}
    return render(request,'complain/index.html',context)

#Complain Create
def complainCreate(request):
    complain_type=models.ComplainType.objects.all()
    context = {'complain_type':complain_type}
    if(request.method=="POST"):
        details=request.POST['details']
        complainType_id=request.POST['complainType_id']
        models.Complain.objects.create(details=details,complainType_id=complainType_id)
        return redirect('/dashboard/complain-list')
    else:
        return render(request,'complain/create.html',context)
#complain Edit
def complain_edit(request,pk):
    Complain=models.Complain.objects.get(id=pk)
    complain_type=models.ComplainType.objects.all()

    if(request.method=="POST"):
        details = request.POST.get('details')
        complainType_id = request.POST.get('complainType_id')
        status = True if request.POST.get('status') else False
        current_time=datetime.datetime.now()
        models.Complain.objects.filter(id=pk).update(details=details,complainType_id=complainType_id,
        status=status,updated_at=current_time)
        return redirect('/dashboard/complain-list')

    return render(request,'complain/edit.html',{'Complain':Complain,'complain_type':complain_type})
#complain delete
def complain_delete(request,pk):
    models.Complain.objects.filter(id=pk).delete()
    return redirect('/dashboard/complain-list')

def complainTypeList(request):

    complain_type_List=models.ComplainType.objects.all()
    context = {'complain_type_List': complain_type_List}
    return render(request,'complain_type/index.html',context)
#complainTypeCreate
def complainTypeCreate(request):
    if(request.method=="POST"):
        name=request.POST['name']
        models.ComplainType.objects.create(name=name)
    return render(request,'complain_type/create.html')
#complainType_edit
def complainType_edit(request,pk):
    complain_type=models.ComplainType.objects.get(id=pk)

    if(request.method=="POST"):
        name = request.POST.get('name')
        status = True if request.POST.get('status') else False
        current_time=datetime.datetime.now()
        models.ComplainType.objects.filter(id=pk).update(name=name,
        status=status,updated_at=current_time)
        return redirect('/dashboard/complainType-list')
    return render(request,'complain_type/edit.html',{'complain_type':complain_type})
#complainType_delete
def complainType_delete(request,pk):
    models.ComplainType.objects.filter(id=pk).delete()
    return redirect('/dashboard/complainType-list')