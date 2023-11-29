from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.

posts = list(range(30))

def index(request):
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/pages/index.html', {'page_obj': page_obj, })

def page(request):
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/pages/page.html')

def post(request):
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/pages/post.html')