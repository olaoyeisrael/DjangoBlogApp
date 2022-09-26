from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangedForm

from django.contrib.auth.views import PasswordChangeView

# Create your views here.



class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangedForm
    # form_class: PasswordChangeForm
    success_url =  reverse_lazy('password_success')
    # success_url: reverse_lazy('home')

def password_success(request):
    return render(request, 'registration/password_success.html', {}) 


class UserRegistrationView(generic.CreateView):

    #This is the one created by django (in-built)
    # form_class = UserCreationForm

    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    # form_class = UserChangeForm

    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user