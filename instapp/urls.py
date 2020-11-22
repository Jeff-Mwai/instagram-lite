from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index, name = 'index'),
    path('new_post/',views.new_post,name = 'new_post'),
    path('profile/',views.profile,name = 'profile'),
    path('user_profile/',views.user_profile,name = 'user_profile'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)