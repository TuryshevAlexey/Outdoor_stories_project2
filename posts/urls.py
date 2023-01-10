from django.urls import path
from django.views.generic import CreateView, DetailView, ListView

from . import views
from users.views import ProfileView, UpdateProfile

from .views import *

app_name = 'posts'

urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('draft/', Draft.as_view(), name='post_draft'),
    path('about/', about, name='about'),
    path('addpost/', AddPost.as_view(), name='post_create'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('profile/<str:username>', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/edit/', UpdateProfile.as_view(), name='profile_update'),
    path('profile/<str:username>/posts/', ProfilePostView.as_view(), name='profile_posts'),
    path('posts/<int:pk>/', ShowPost.as_view(), name='post_detail'),
    path('posts/<int:pk>/public/', public_post, name='post_public'),
    path('posts/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('category/<slug:cat_slug>/', PostCategory.as_view(), name='category'),
]
