from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "feed/create.html"
    fields = ['text']
    success_url = '/'

    # def dispatch(self, request, *args, **kwargs):
    #     self.request = request
    #     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()

        return super().form_valid(form)