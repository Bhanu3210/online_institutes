"""online_institutes1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from online_institutes1 import settings

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ShowIndex, name='ShowIndex'),
    path('Stu_registration', views.Stu_registration.as_view(), name='Stu_registration'),
    path('Student_welcome_page', views.Student_welcome_page, name='Student_welcome_page'),
    path('stu_Login/', views.stu_Login, name='stu_Login'),
    path('admin_login/',views.admin_login,name = "admin_login"),
    path('admin_login_check/',views.admin_login_check,name='admin_login_check'),
    path('admin_welcome_page/', views.admin_welcome_page, name='admin_welcome_page'),
    path('Add_new_class/',views.Add_new_class.as_view(),name='Add_new_class'),
    path('View_all_scheduled_classes/', views.View_all_scheduled_classes, name='View_all_scheduled_classes'),
    path('update_class/<int:id>',views.update_class, name='update_Class'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete_class/<int:id>/',views.delete_class,name='delete_class')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)