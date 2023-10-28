from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import View
from authentication.forms import UserUpdateForm
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.


def Dashboard(request):
  return render(request, 'cms/dashboard.html')

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        context = {"form": form}
        return render(request, 'cms/profile.html', context)

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'cms/profile.html'
    success_url = reverse_lazy('cms:ProfileView')