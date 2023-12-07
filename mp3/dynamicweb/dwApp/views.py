from django.shortcuts import render
from .models import massage,blog

# Create your views here.
def home(request):
    obj1 = massage.objects.all()
    obj2 = blog.objects.all()
    return render(request,'index.html',{'result1':obj1,'result2':obj2})
