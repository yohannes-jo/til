from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
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

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()

        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        post = Post.objects.create(
            text=request.POST.get("text"),
            author=request.user,
        )
        return render(
            request,
            "includes/post.html",
            {
                "post": post,
                "show_detail_link": True,
            },
            content_type="application/html"
        )