from pyexpat import model
from django.shortcuts import render
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