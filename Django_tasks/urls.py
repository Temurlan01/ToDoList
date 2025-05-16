from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from tasks.views import HomeView, ProfileView, AddTaskView, DeleteTaskView, MarkDoneView, UploadAvatarView
from users.views import UserRegistrationView, LoginListView, MakeUserRegistrationView, MakeLoginView, MakeLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home-url'),
    path('', UserRegistrationView.as_view(), name='register-url'),
    path('login/', LoginListView.as_view(), name='login-url'),
    path('make-logaut/', MakeLogoutView.as_view(), name='logout-url'),

    path('make-login/', MakeLoginView.as_view(), name="make-login-url"),
    path('make-register/', MakeUserRegistrationView.as_view(), name="make-registration-url"),

    path('profile/<int:pk>/', ProfileView.as_view(), name='profile-url'),

    path('addTask/', AddTaskView.as_view(), name='addTask-url'),
    path('delete/<int:pk>/', DeleteTaskView.as_view(), name='deleteTask-url'),
    path('done/<int:task_id>/', MarkDoneView.as_view(), name='mark-done-url'),

    path('upload-avatar/', UploadAvatarView.as_view(), name='upload-avatar-url'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
