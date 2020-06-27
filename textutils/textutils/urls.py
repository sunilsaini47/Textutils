
# code 6 video

# from django.contrib import admin
# from django.urls import path
# from .import views

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', views.index, name= 'index'),
#    path('about', views.about , name= 'about'),
#]

# code video 8
from django.contrib import admin
from django.urls import path
from . import views

# expretion 1
# urlpatterns = [
#
#     path('admin/', admin.site.urls),
#     path('', views.navigation, name='navigation'),
#
# ]



urlpatterns = [
      path('admin/', admin.site.urls),
      path('', views.index, name='index'),
      path('analyze', views.analyze, name='analyze'),
#     # path('capitalizefirst', views.capfirst, name='capfirst'),
#     # path('newlineremove', views.newlineremove, name='newlineremove'),
#     # path('spaceremove', views.spaceremove, name='spaceremove'),
#     # path('charcount', views.charcount, name='charcount'),
]
