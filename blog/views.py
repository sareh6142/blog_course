from django.shortcuts import render, redirect
from .models import Post
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from .forms import NewPostForm
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.


# def post_list_view(request):
#     posts_lists = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/home.html', {'posts_list_last': posts_lists})

class PostListView(generic.ListView):

    template_name = 'blog/home.html'
    context_object_name = 'posts_list_last'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')

# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except ObjectDoesNotExist:
#     #     post = None
#
#     return render(request, 'blog/detail.html', {'post': post})


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'


# def post_add_view(request):
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("post_page")
#             # form = NewPostForm()
#
#
#     else:
#         form = NewPostForm()
#     return render(request, 'blog/new.html', {'form': form})


class PostCreateView(generic.CreateView):
    form_class = NewPostForm
    template_name = 'blog/new.html'


# def update_view(request,pk):
#     # post = Post.objects.get(pk=pk)
#     post = get_object_or_404(Post, pk=pk)
#     form = NewPostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect("post_page")
#
#     return render(request, 'blog/new.html', {'form': form})
class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = NewPostForm
    template_name = 'blog/new.html'


# def delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect("post_page")
#
#     return render(request, 'blog/delete.html', {'post': post})
class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('post_page')


    # post = get_object_or_404(Post, pk=pk)
    # if request.method == 'POST':
    #     post.delete()
    #     return redirect('post_page')



