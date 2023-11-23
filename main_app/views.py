from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def blog_home(request):
    return render(request, "blog-home.html")

def blog_post(request):
    return render(request, "blog-post.html")

def contact(request):
    return render(request, "contact.html")

def faq(request):
    return render(request, "faq.html")

def portfolio_item(request):
    return render(request, "portfolio-item.html")

def portfolio_overview(request):
    return render(request, "portfolio-overview.html")

def pricing(request):
    return render(request, "pricing.html")