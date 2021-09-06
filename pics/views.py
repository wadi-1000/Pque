from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Category, Location

# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, 'homepage.html',{'images':images})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        
        return render(request, 'all-pics/search.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term"
    return render(request, 'all-pics/search.html',{"message":message})

