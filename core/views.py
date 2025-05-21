from django.shortcuts import render

def home(request):
    return render(request,'core/home.html')

def product(request):
    return render(request ,'core/product.html')

def contact(request):
    return render(request,'core/contact.html')

def about(request):
    return render(request,'core/about.html')
