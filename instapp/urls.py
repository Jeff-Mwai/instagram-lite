from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.index, name = 'index'),
    path('new_post/',views.new_post,name = 'new_post'),
    path('profile/',views.profile,name = 'profile'),
    path('comment/<id>',views.comment,name = 'comment'),
    path('search_results',views.search_results,name = 'search_results'),
    path('register/',views.register, name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('updateprofile/', views.update_profile, name='updateprofile'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)