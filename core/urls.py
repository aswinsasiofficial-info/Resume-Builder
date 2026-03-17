from django.contrib import admin
from django.urls import path, include
from home.views import landing, home, builder, gen_resume, profile, login_view, signup_view, logout_view, builder_fullstack, builder_3d_generalist, builder_data_scientist, builder_ux_designer, builder_executive

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name='landing'),
    path('home/', home, name='home'),
    path('builder/', builder, name='builder'),
    path('builder/fullstack/', builder_fullstack, name='builder_fullstack'),
    path('builder/3d-generalist/', builder_3d_generalist, name='builder_3d'),
    path('builder/data-scientist/', builder_data_scientist, name='builder_data'),
    path('builder/ux-designer/', builder_ux_designer, name='builder_ux'),
    path('builder/executive/', builder_executive, name='builder_executive'),
    path('resume/', gen_resume, name='resume'),
    path('profile/', profile, name='profile'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('accounts/', include('allauth.urls')),
]