from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import CreationForm, UserLoginForm, UserUpdateForm
from users.models import User


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model and log the user in."""
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f'Аккаунт {user.username} создан')
        return redirect(self.success_url)

    # def form_valid(self, form):
    #     # save the new user first
    #     form.save()
    #     #get the username and password
    #     username = self.request.POST['username']
    #     password = self.request.POST['password1']
    #     #authenticate user then login
    #     user = authenticate(username=username, password=password)
    #     login(self.request, user)
    #     return redirect(self.get_success_url)


class LoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

#    def form_valid(self, form):
#        email = form.cleaned_data['email']
#        password = form.cleaned_data['password']
#        user = authenticate(email=email, password=password)

#     # Check here if the user is an admin
#        if user is not None and user.is_active:
#            login(self.request, user)
#            return HttpResponseRedirect(self.success_url)
#        else:
#            return self.form_invalid(form)


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile_user.html'
    context_object_name = 'profile'
    slug_url_kwarg = 'username'
    slug_field = "username"


class UpdateProfile(SuccessMessageMixin, UpdateView):
    model = User
    slug_url_kwarg = 'username'
    slug_field = "username"
    form_class = UserUpdateForm
    # fields = ('first_name', 'last_name', 'username', 'image')
    template_name = 'users/signup.html'
    extra_context = {'is_edit': True}
    success_message = 'Профиль обновлен'
