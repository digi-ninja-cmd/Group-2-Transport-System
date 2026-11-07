from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def servicedetails(request):
    return render(request, 'servicedetails.html')

def pricing(request):
    return render(request, 'pricing.html')

def quote(request):
    return render(request, 'quote.html')

def contact(request):
    return render(request, 'contact.html')

def starterpage(request):
    return render(request, 'starterpage.html')
