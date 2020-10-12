from django.shortcuts import render
from .models import gallery, Location, Category

# Create your views here.
def index(request): 
    return render(request, 'index.html')

def galleri(request):
    my_image = gallery.all_images()

    return render(request, 'gallery.html', {"my_image":my_image})

def search_results(request):
    
    if 'img' in request.GET and request.GET["img"]:
        search_term = request.GET.get("img")
        searched_images = gallery.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"imgs": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})