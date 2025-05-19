from django.contrib.auth.decorators import login_required
from django.shortcuts import  redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.contrib import messages
from tasks.models import Task


class HomeView(TemplateView):
    """
    вьюшка для показа домашней страницы
    """

    template_name = 'tasks.html'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login-url')
        return super().dispatch(request, *args, **kwargs)

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
    """
     вьюшка для того что бы показать профиль пользователя
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login-url')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self,*args,**kwargs):

        current_user = self.request.user
        context = {
            'current_user': current_user,

        }
        return context


class AddTaskView(View):
    """
    вьюшка для того что бы добавить задачу
    """

    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')
        user = request.user
        Task.objects.create(text=text, user=user)
        return redirect('home-url')


class DeleteTaskView(View):
    """
    вьюшка для того что бы удалить задачи
    """

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.delete()
        return redirect('home-url')



class MarkDoneView(View):
    """
    вьюшка для того что пометить задачи прочитанными
    """

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        task.is_done = True
        task.save()
        return redirect('home-url')



class UploadAvatarView(View):
    """
    вьюшка для того что бы загрузить фото профиля
    """

    @method_decorator(login_required)
    def post(self, request):
        user = request.user
        avatar = request.FILES.get('avatar')

        if avatar:
            user.avatar = avatar
            user.save()
            return redirect('home-url')
        return messages.error(request,'Файл не был загружен')




