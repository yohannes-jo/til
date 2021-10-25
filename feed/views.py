from django.views.generic import ListView
from .models import Post

class HomePage(ListView):
    queryset = Post.objects.all().order_by('-id')[0:30]
    http_method_names = ["get"]
    model = Post
    template_name = "feed/homepage.html"
    context_object_name = "posts"