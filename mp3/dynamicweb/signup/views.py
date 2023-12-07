from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password1']
        c_password = request.POST['password2']
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'This email already exists')
            else:
                user = User.objects.create_user(username=username,first_name= firstname,last_name= lastname,email=email,password=password )
                user.save()
                return redirect ('login')
        else:
            messages.info(request,"Password Do Not Match")
            return redirect('register')
        return redirect ('/')
    return render(request,'signup.html')