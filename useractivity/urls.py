from django.contrib import admin
from django.urls import path
from useractivity.views import *
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.signin, name='Login'),
    path('signup',views.signup, name='Signup'),
    path('home',views.home, name='Home'),
    path('edit',views.edit_user, name='Edituser'),
    path('editpage',views.edit_page,name='Editpage'),
    path('changepassword',views.change_password,name='Changepassword'),
    path('userchangepwd',views.user_change_password,name='Userchangepwd'),
    path('viewuser',views.view_all_users,name='Viewuser'),
    path('logout',views.user_logout,name='Logout')

]
