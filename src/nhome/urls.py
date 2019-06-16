from django.contrib import admin
from blog import views as blog_views
from django.urls import path, include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', blog_views.home, name='home'),
    path('posts/', include('blog.urls', namespace='posts')),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name='logout'),
    path('register/', accounts_views.register, name='register'),
    path('admin/', admin.site.urls),
]
