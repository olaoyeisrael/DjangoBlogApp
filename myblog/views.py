from unicodedata import category
from xml.etree.ElementTree import Comment
from django.shortcuts import render, get_object_or_404    
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from.models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.
# def home(request):
#     return render(request, 'home.html',{})


def LikeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('blog_id'))
    liked = False

    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    # this is used to stay on the page after being reloaded
    return HttpResponseRedirect(reverse('blog-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    # ordering = ['-id']
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        # stuff = get_object_or_404(Post,id = self.kwargs["pk"])  
        # total_likes = stuff.total_likes()      
        # context["total_likes"]= total_likes
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category= cats.replace('-', '%20')) 
    return render(request, 'categories.html', {'cats': cats.title().replace('-', '%20'), 'category_posts': category_posts})

class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post,id = self.kwargs["pk"])  
        total_likes = stuff.total_likes()   

        liked = False

        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True   
        context["total_likes"]= total_likes
        context["cat_menu"] = cat_menu
        context["liked"] = liked
        return context

class AddBlogView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addBlog.html'
    # fields = '__all__'




class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    # fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'addCategory.html'
    fields = '__all__'


class UpdateBlogView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'
    # fields = ['title', 'author', 'body']
class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')