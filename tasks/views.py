from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from tasks.models import Task
from users.models import CustomUser


class HomeView(TemplateView):
    template_name = 'tasks.html'
    def get_context_data(self,*args, **kwargs):
        user = self.request.user
        tasks_active = Task.objects.filter(user=user, is_done=False)
        tasks_done = Task.objects.filter(user=user, is_done=True)
        context = {
            'current_user': user,
            'tasks_active': tasks_active,
            'tasks_done': tasks_done,
        }
        return context


class ProfileView(TemplateView):
    def get_context_data(self,*args,**kwargs):

        current_user = self.request.user
        context = {
            'current_user': current_user,

        }
        return context


class AddTaskView(View):
    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')
        user = request.user
        Task.objects.create(text=text, user=user)
        return redirect('home-url')


class DeleteTaskView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.delete()
        return redirect('home-url')

class MarkDoneView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.is_done = True
        task.save()
        return redirect('home-url')




