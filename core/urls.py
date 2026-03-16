from django.contrib import admin
from django.urls import path, include
from home.views import landing, home, builder, gen_resume, profile, login_view, signup_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('home/', home, name='home'),
    path('builder/', builder, name='builder'),
    path('resume/', gen_resume, name='resume'),
    path('profile/', profile, name='profile'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('accounts/', include('allauth.urls')),
]