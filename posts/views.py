from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import AddPostForm
from .models import Category, Post, User
from users.forms import UserUpdateForm


class Home(ListView):
    paginate_by = 5
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Путевой журнал'
        return context

    def get_queryset(self):
        return Post.objects.all()


class ShowPost(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['count'] = Post.objects.filter(author__id=self.kwargs['pk']).count()
        return context


class ProfilePostView(ListView):
    model = Post
    template_name: str = 'posts/profile_posts.html'
    context_object_name = 'page_obj'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['username']
        context['count'] = Post.objects.filter(author__username=self.kwargs['username']).count()
        context['fio'] = context['title']
        return context


class PostCategory(ListView):
    paginate_by = 5
    model = Post
    template_name = 'posts/category_list.html'
    context_object_name = 'page_obj'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['page_obj'][0].category)
        return context


class AddPost(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('posts:index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = AddPostForm
    template_name = 'posts/create_post.html'
    id_url_kwarg = 'id'
    context_object_name = 'post'
    # success_url = reverse_lazy('profile:index')
    extra_context = {'is_edit': True}


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def about(request):
    return HttpResponse("О авторе")
