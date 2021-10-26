from django.views.generic import ListView, DetailView
from .models import Post

class HomePage(ListView):
    queryset = Post.objects.all().order_by('-id')[0:30]
    http_method_names = ["get"]
    model = Post
    template_name = "feed/homepage.html"
    context_object_name = "posts"
                        
class PostDetail(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "feed/detail.html"
    http_method_names = ["get"]