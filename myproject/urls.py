"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('lesson_01_app.urls')),
    path('random/', include('lesson_01_task_2_app.urls')),
    path('homework1/', include('lesson_01_homework_app.urls')),
    path('lesson2/', include('lesson_02_app.urls')),
    path('lesson2/', include('lesson_02_hw_app.urls')),
    #path('__debug__/', include("debug_toolbar.urls")),
]

#if settings.DEBUG :
#    urlpatterns += patterns('',
#        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#    )
