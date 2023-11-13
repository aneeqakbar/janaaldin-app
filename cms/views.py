from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import View
from authentication.forms import UserUpdateForm
from django.contrib.auth import get_user_model
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from authentication.models import StaffMember
from classes.models import Class, ClassDateTime

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

class StaffMemberListView(ListView):
    model = StaffMember
    template_name = 'cms/staff_member/list.html'
    # context_object_name = 'staff_members'

# class StaffMemberDetailView(DetailView):
#     model = StaffMember
#     template_name = 'cms/staff_member/detail.html'
#     context_object_name = 'staff_member'

class StaffMemberCreateView(CreateView):
    model = StaffMember
    template_name = 'cms/staff_member/create.html'
    fields = ['name']
    success_url = reverse_lazy("cms:StaffMemberListView")

class StaffMemberUpdateView(UpdateView):
    model = StaffMember
    template_name = 'cms/staff_member/update.html'
    fields = ['name']
    success_url = reverse_lazy("cms:StaffMemberListView")

class StaffMemberDeleteView(DeleteView):
    model = StaffMember
    template_name = 'cms/staff_member/delete.html'
    success_url = reverse_lazy('cms:StaffMemberListView')


class ClassListView(ListView):
    model = Class
    template_name = 'cms/classes/list.html'
    success_url = reverse_lazy('cms:ClassListView')

# class ClassDetailView(DetailView):
#     model = Class
#     template_name = 'cms/classes/detail.html'
#     context_object_name = 'class_instance'

class ClassCreateView(CreateView):
    model = Class
    template_name = 'cms/classes/create.html'
    fields = ['name', 'description', 'staff_members']
    success_url = reverse_lazy('cms:ClassListView')

    def form_valid(self, form):
        self.object = form.save()

        class_times = self.request.POST.getlist("class_time[]")

        ClassDateTime.objects.filter(parent__id=self.object.id).delete()

        for time in class_times:
            ClassDateTime.objects.create(parent=self.object, datetime=time)

        return redirect(self.success_url)


class ClassUpdateView(UpdateView):
    model = Class
    template_name = 'cms/classes/update.html'
    fields = ['name', 'description', 'staff_members']
    success_url = reverse_lazy('cms:ClassListView')


    def form_valid(self, form):
        self.object = form.save()

        class_times = self.request.POST.getlist("class_time[]")

        ClassDateTime.objects.filter(parent__id=self.object.id).delete()

        for time in class_times:
            ClassDateTime.objects.create(parent=self.object, datetime=time)

        return redirect(self.success_url)

class ClassDeleteView(DeleteView):
    model = Class
    template_name = 'cms/classes/delete.html'
    success_url = reverse_lazy('cms:ClassListView')