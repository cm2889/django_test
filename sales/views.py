from pyexpat import model
from django.shortcuts import render,redirect
import hashlib
from . import models

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
        models.Category.objects.filter(id=pk).update(category_name=category_name,status=status)
        return redirect('/category-list')

    return render(request,'category/edit.html',{'Category':Category})



