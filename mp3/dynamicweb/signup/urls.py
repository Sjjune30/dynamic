from django.urls import path
from signup import views

urlpatterns = [
    path('register',views.register, name = 'register'),

]