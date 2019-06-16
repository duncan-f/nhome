from blog.models import Post
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

def home(request):

    context = {
        'posts': Post.objects.order_by('-created')[:5],
    }
    return render(request, "blog/home.html", context)

class PostListView(generic.ListView):
    context_object_name = 'posts'

    ordering = [
        '-created',
    ]

    paginate_by = 5

    model = Post


class PostDetailView(generic.DetailView):
    context_object_name = 'post'
    model = Post

class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    fields = [
        'title',
        'content',
        'draft',
        #'published'
    ]

    success_message = f'Your post has been created successfully.'
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    fields = [
        'title',
        'content',
        'draft',
        #'published'
    ]

    success_message = f'Your post has been updated successfully.'
    model = Post
