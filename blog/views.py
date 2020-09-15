# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Post

class PostView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'